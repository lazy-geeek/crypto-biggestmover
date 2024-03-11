from crewai import Crew, Process
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from decouple import config

class Billionaire_Interview_Crew:
    def __init__(self):
        pass

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        passive_income_billionaire = agents.passive_income_billionaire()
        interviewer = agents.interviewer()

        # Custom tasks include agent name and variables as input
        interview_billionaire = tasks.interview_people(
            agent=passive_income_billionaire,
            interviewed_person=passive_income_billionaire
        )        

        # Define your custom crew here
        crew = Crew(
            agents=[passive_income_billionaire,
                    interviewer                                      
            ],
            tasks=[
                interview_billionaire                
            ],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Billionaire Interview Crew")
    print('-------------------------------')
    
    crew = Billionaire_Interview_Crew()
    result = crew.run()
    print("\n\n########################")
    print("## Here are your insights:")
    print("########################\n")
    print(result)