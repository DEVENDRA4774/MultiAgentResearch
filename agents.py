import os
from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.7
)

# 1. Senior Researcher
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in {topic}',
    backstory='You work at a leading tech think tank. Your expertise lies in identifying emerging trends. You have a knack for dissecting complex data and presenting actionable insights.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Tech Summarizer
summarizer = Agent(
    role='Lead Content Synthesizer',
    goal='Distill the raw research data on {topic} into a concise, easily digestible summary',
    backstory='You are a renowned technical writer known for your ability to explain complex concepts in simple terms. You take the dense reports from researchers and turn them into clear, engaging summaries for executives.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. Fact-Checker
fact_checker = Agent(
    role='Fact-Checker and Auditor',
    goal='Review the summary about {topic}, verify the claims using the internet, and provide a final report with citations.',
    backstory='You are a meticulous auditor. You double-check every claim made in reports and find reliable sources to back them up. You ensure that no "fake news" or unverified claims make their way into the final output.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)
