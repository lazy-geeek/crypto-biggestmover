from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""

class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def interview_people(self, agent, interviewed_person):
        return Task(
            description=dedent(
                f"""
                **Task**: 
                Interview a person
                **Description**:
                You are interviewing a famous person who wants to give away his knowlege and experience how he became successful.
                You write down the insights and anecdotes how he became famous and successful.
                You can present these findings from the interviews to others in such an understandable way so that other people can also become successful.
                Your write it down in a very detailed form that another person can follow it step by step.
                Get at least 3 ways how to become successful.

                **Parameters**: 
                - Interviewed person: {interviewed_person}
                
                **Note**: {self.__tip_section()}

                """
            ),
            agent=agent,
        )