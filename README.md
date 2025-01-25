# Sales Pipeline Automation with CrewAI

This project automates the sales pipeline process using CrewAI and provides a user-friendly interface via Streamlit. The app enriches lead information, scores leads based on alignment with provided services, and generates personalized emails for qualified leads.

## Features

- **Lead Enrichment:** Scrapes the web and company websites to gather additional lead information.
- **Lead Scoring:** Evaluates leads based on alignment with provided services and assigns a score (0-100).
- **Personalized Email Generation:** Creates tailored emails for qualified leads (score >= 70).
- **Streamlit Interface:** Provides an interactive web interface for inputting lead details and viewing results.

## How It Works

### Lead Enrichment:

The app scrapes the web and the company website to gather additional information about the lead (e.g., social profiles, recent news).

### Lead Scoring:

The app evaluates the enriched lead data and assigns a score (0-100) based on alignment with the services you provide. A score of 70 or above qualifies the lead.

### Personalized Email:

For qualified leads, the app generates a personalized email tailored to the lead's needs, referencing the services you offer.

## Installation

### Prerequisites

- Python 3.10 or higher
- Streamlit
- CrewAI
- CrewAI Tools (SerperDevTool, ScrapeWebsiteTool)

### Steps

#### Clone the Repository:

```bash
git clone https://github.com/noumaanahamed/sales-pipeline-agent.git
cd sales-pipeline-agent
```

#### Set Up a Virtual Environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

#### Install Dependencies:

```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables:

Create a `.env` file in the root directory and add the following:

```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

## Usage

### Run the Streamlit App:

```bash
streamlit run ui.py
```

### Input Lead Details:

- Enter the lead's company, name, role, and website in the sidebar.
- Provide the services you offer as a comma-separated list.

### Run the Pipeline:

- Click the **Run Sales Pipeline** button to execute the pipeline.

### View Results:

- The app will display the enriched lead data, lead score, and personalized email.
- Use the **Download Email as Markdown** button to download the email.

## Example

### Input

**Lead Information:**

- Company Name: Crew AI
- Lead Name: Joao Moura
- Lead Role: Founder
- Company Website: https://crewai.com

**Services Offered:**

- Generative AI services, AI-driven analytics

### Output

#### Enriched Lead Data:

```json
{
  "company": "Crew AI",
  "name": "Joao Moura",
  "role": "Founder",
  "website": "https://crewai.com",
  "additional_data": {
    "social_profiles": ["https://linkedin.com/in/joaomoura"],
    "recent_news": ["Crew AI raises $10M in funding"]
  }
}
```

#### Lead Score:

```json
{
  "lead_score": 85,
  "qualification_status": "Qualified"
}
```

#### Personalized Email:

```markdown
# Personalized Email for Joao Moura

Hi Joao,

I hope this message finds you well. I came across your profile and noticed that you're the Founder of Crew AI. I wanted to reach out because I believe our **Generative AI services** and **AI-driven analytics** could greatly benefit your company, especially in streamlining your AI-driven workflows.

Would you be open to a brief call next week to discuss how we can help Crew AI achieve its goals?

Looking forward to your response!

Best regards,  
[Your Name]  
[Your Position]  
[Your Company]
```

## Technologies Used

- **CrewAI:** Framework for building AI agents.
- **Streamlit:** Web framework for creating interactive apps.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
