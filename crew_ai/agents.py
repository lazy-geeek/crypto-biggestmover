from crewai import Agent
from textwrap import dedent

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a growing list of ideas how to make passive income over the internet using AI tools

Captain/Manager/Boss:
- Passive Income Master

Employees/Experts to hire:
- Idea Researcher 
- Idea Reviewer
- Idea Tester

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""

class YoutubeAutomationAgents():
    def passive_income_billionaire(self):
        return Agent(
            role="Passive Income Billionaire",
            backstory=dedent(f"""
                             You became a passive income dollar billionaire over the last years using highly automated strategies.
                             You can stay all over the world in your properties wherever you like. In parallel your businesses 
                             and income streams keep running online on auto pilot. You make so much money every day,
                             you don't know how to spend all of it for the rest of your life.
                             
                             """),
            goal=dedent(f"""
                        You now want to give away your knowlege and experience how to become a passive income billionaire other people through suitable media.                        
                        """)
        )

    def interviewer(self):
        return Agent(
            role="Idea Researcher"
        )
        
    def biographer(self):
        return Agent(
            role="Idea Researcher"
        )
    
    def idea_researcher(self):
        return Agent(
            role="Idea Researcher"
        )
        
    def idea_reviewer(self):
        return Agent(
            role="Idea Reviewer"
        )