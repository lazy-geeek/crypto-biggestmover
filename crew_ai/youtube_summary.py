from crewai import Crew, Process
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from decouple import config

class Youtube_Summarizer_Crew:
    def __init__(self,video_url):
        self.video_url = video_url

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        youtube_transcriber = agents.youtube_transcriber()
        transcription_summarizer = agents.transcription_summarizer()        

        # Custom tasks include agent name and variables as input
        summarize_video = tasks.summarize_youtube_video(
            agent=youtube_transcriber,
            video_url=self.video_url
        )        

        # Define your custom crew here
        crew = Crew(
            agents=[youtube_transcriber                                                  
            ],
            tasks=[
                summarize_video
            ],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Youtube Summary Crew")
    print('-------------------------------')
    video_url = input(
        dedent("""
      Give me a youtube video URL !
    """))
    
    crew = Youtube_Summarizer_Crew(video_url)
    result = crew.run()
    print("\n\n########################")
    print("## Here are your insights:")
    print("########################\n")
    print(result)