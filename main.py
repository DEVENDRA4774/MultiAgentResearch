import sys
from crewai import Crew, Process
from tasks import research_task, summarize_task, fact_check_task
from agents import researcher, summarizer, fact_checker

def main():
    print("Welcome to the Multi-Agent Research Assistant!")
    print("---------------------------------------------")
    
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = "Latest trends in generative AI in 2026"

    # Assemble the crew
    crew = Crew(
        agents=[researcher, summarizer, fact_checker],
        tasks=[research_task, summarize_task, fact_check_task],
        process=Process.sequential, 
        memory=True, # Uses vector db explicitly
        verbose=True
    )

    print(f"\nStarting the research process for: '{topic}'...\n")
    
    # Kickoff the process
    result = crew.kickoff(inputs={'topic': topic})

    print("\n---------------------------------------------")
    print("Research Process Complete!")
    print("---------------------------------------------")
    print("\nFinal Output saved to final_research_report.md\n")

if __name__ == "__main__":
    main()
