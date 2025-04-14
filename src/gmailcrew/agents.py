from textwrap import dedent
from crewai import Agent,LLM
from .tools import CreateDraftTool,TavilyTool,GetGmailThreadTool
from langchain_community.agent_toolkits import GmailToolkit
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['TAVILY_API_KEY']=os.getenv("TAVILY_API_KEY")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")

llm=LLM(model='groq/llama-3.3-70b-versatile')


class EmailFilterAgents():
    def __init__(self):
        self.gmail=GmailToolkit()

    def email_filter_agent(self):
        return Agent(
            llm=llm,
            role='Senior Email Analyst',
            goal='Filter out non-essential emails like newsletters and promotional content. Excluding the first 10',
            backstory=dedent("As a senior email analyst you have extensive experience in email cotetn analysis."
            "You are adept at distinguishing important emails from spam, newsletters other irrelevant content"),
            verbose=True,
            allow_delegation=False
        )
    
    def email_action_agent(self):
        return Agent(
            llm=llm,
            role='Senior Action Specialist',
            goal='Identify action-required emails and compile a list of their IDs.',
            backstory=dedent("with a keen eye for detail and a knack for understanding content, you specialize in identifying emails that require immediate action."
            "Your skill set includes interpreting the urgency and importance of an email based on its content and context."),
            verbose=True,
            allow_delegation=False,
            tools=[GetGmailThreadTool(),TavilyTool()],
        )
    
    def email_writer_agent(self):
        return Agent(
            llm=llm,
            role='Senior Email Writer',
            goal='Draft a response fro the emails',
            backstory=dedent("With years of expertise as a senior email writer, you are an expert in creating meaningfull and coherent email drafts."),
            verbose=True,
            allow_delegation=False,
            tools=[GetGmailThreadTool(),
                   TavilyTool(),
                   CreateDraftTool()],           
        )