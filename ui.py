__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit App Title
st.title("Sales Pipeline Automation with CrewAI")
st.markdown("This app automates the sales pipeline process, including lead enrichment, scoring, and personalized email generation.")

# User Inputs
st.sidebar.header("Lead Information")
company = st.sidebar.text_input("Company Name", "Crew AI")
name = st.sidebar.text_input("Lead Name", "Joao Moura")
role = st.sidebar.text_input("Lead Role", "Founder")
website = st.sidebar.text_input("Company Website", "https://crewai.com")

st.sidebar.header("Services Offered")
services = st.sidebar.text_area("Services (comma-separated)", "Generative AI services, AI-driven analytics")

# Convert services to a list
services_list = [s.strip() for s in services.split(",")]

# Define the lead dictionary
lead = {
    "company": company,
    "name": name,
    "role": role,
    "website": website
}

# Define tools
search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()

# Define LLM
llm = LLM(model="gemini/gemini-1.5-flash", temperature=0.7)

# Define Agents
lead_enricher = Agent(
    role="Lead Enrichment Specialist",
    goal="Enrich lead information with additional data from external sources",
    backstory="You are a data-savvy specialist who knows how to find and append relevant information to leads, such as company details, social profiles, and recent news.",
    llm=llm,
    verbose=True,
    tools=[search_tool, scraper_tool]
)

lead_scorer = Agent(
    role="Lead Scoring Analyst",
    goal="Score leads based on their likelihood to convert, considering the services provided",
    backstory="You are an analytical expert who evaluates leads based on their engagement, company size, and alignment with the services provided.",
    llm=llm,
    verbose=True
)

email_personalizer = Agent(
    role="Email Personalization Specialist",
    goal="Write personalized emails for qualified leads, referencing the services provided",
    backstory="You are a creative writer who crafts compelling and personalized emails that resonate with the lead's specific needs and interests, while highlighting the services provided.",
    llm=llm,
    verbose=True
)

# Define Tasks
enrich_lead_task = Task(
    description=f"""
    Enrich the lead information with additional data from external sources.
    Lead Info:
    - Company: {lead['company']}
    - Name: {lead['name']}
    - Role: {lead['role']}
    - Website: {lead['website']}
    """,
    expected_output="A JSON object containing enriched lead information, including company details and website data.",
    agent=lead_enricher
)

score_lead_task = Task(
    description=f"""
    Score the lead based on enriched data and alignment with the services provided: {services_list}.
    Lead Info:
    - Company: {lead['company']}
    - Name: {lead['name']}
    - Role: {lead['role']}
    Assign a score from 0 to 100, where 70 or above qualifies the lead.
    """,
    expected_output="A JSON object containing the lead's score, qualification status, and a brief explanation of the score.",
    agent=lead_scorer,
    context=[enrich_lead_task]  # Depends on the output of enrich_lead_task
)

personalize_email_task = Task(
    description=f"""
    Write a personalized email for qualified leads (score >= 70).
    Lead Info:
    - Company: {lead['company']}
    - Name: {lead['name']}
    - Role: {lead['role']}
    Reference the services provided: {services_list}.
    """,
    expected_output="A personalized email in markdown format, tailored to the lead's needs and highlighting the services provided.",
    agent=email_personalizer,
    context=[score_lead_task]  # Depends on the output of score_lead_task
)

# Define Crew
sales_pipeline_crew = Crew(
    agents=[lead_enricher, lead_scorer, email_personalizer],
    tasks=[enrich_lead_task, score_lead_task, personalize_email_task],
    process="sequential",  # Tasks will be executed in sequence
    verbose=True
)

# Run the Crew when the user clicks the button
if st.sidebar.button("Run Sales Pipeline"):
    st.write("Running the sales pipeline...")

    # Run the crew
    result = sales_pipeline_crew.kickoff(inputs={"lead": lead, "services": services_list})

    # Display the result
    st.subheader("Pipeline Execution Result")
    st.markdown(result.raw)

    st.success("Pipeline execution completed!")