from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

from decouple import config

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

class CustomAgents():
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="mixtral",
            base_url=config("ollama_url"),
            api_key="NA"
        )        
    
    def youtube_url_getter(self):
        return Agent(
            role="Get URLs of youtube videos",
            backstory=dedent(f"""
                             You receieve the URL of youtube videos in a Youtube playlist and pass it to another agent.
                             """),
            goal=dedent(f"""
                        Looping through the youtube playlist, get the URL of each video in the playlist and pass the URL to another agent.
                        You only pass 1 URL at a time to the next agent.
                        """),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
    
    def youtube_transcriber(self):
        return Agent(
            role="Transcribe youtube videos",
            backstory=dedent(f"""
                             You are an expert in extracting transcriptions from youtube videos.
                             """),
            goal=dedent(f"""
                        You recieve an URL of a youtube video and extraxt the transcription out of it. Afterwards you pass it to another agent.
                        """),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
        
    def transcription_summarizer(self):
        return Agent(
            role="Summarize transcriptions",
            backstory=dedent(f"""
                             You are an expert in extracting transcriptions from youtube videos.
                             """),
            goal=dedent(f"""
                        You recieve an URL of a youtube video and extraxt the transcription out of it. Afterwards you pass it to another agent.
                        """),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
    
    def passive_income_billionaire(self):
        return Agent(
            role="Passive Income Billionaire",
            backstory=dedent(f"""
                             You became a passive income dollar billionaire using highly automated strategies.
                             You can stay all over the world in your properties wherever you like and have all the luxury you can dream of.
                             In parallel your businesses and income streams keep running online on auto pilot. You make so much money every day,
                             you don't know how to spend all of it for the rest of your life.
                             
                             """),
            goal=dedent(f"""
                        You now want to give away your knowlege and experience how to become a passive income billionaire to other people.
                        You want to do this in a way that everybody can understand step by step how become a passive income billioniare.
                        """),
            allow_delegation=True,
            verbose=True,
            llm=self.llm
        )

    def interviewer(self):
        return Agent(
            role="Interviewer",
            backstory=dedent(f"""
                             You are one of the world's best known interviewers with countless years of experience. Your specialty is intervieweing very famous people
                             and being able to tease everything out of them. Even their deepest secrets that they have never told anyone before. 
                             You can present these findings from the interviews to others in such an understandable way 
                             that they can immediately grasp the content and apply it themselves.
                             """),
            goal=dedent(f"""
                        Interviewing famous people and writing down the insights and anecdotes how they became famous and successful so that other people can also become successful.
                        """),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
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
        

