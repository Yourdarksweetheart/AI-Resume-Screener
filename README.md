# AI-Resume-Screener
AI Recruitment Screening System

This project uses CrewAI to create an intelligent recruitment screening system that helps identify the best candidates for a AI Education Product Manager position.

Features

Automated screening of candidate resumes against job requirements
AI-powered analysis of technical and soft skills
Detailed ranking and rationale for top candidates
Focus on AI Education product management experience evaluation
Prerequisites

Before running this project, you need to have:

Python 3.11 or higher
An OpenAI API key (with GPT-4 access)
pip (Python package installer)
Installation

Clone the repository:
git clone https://github.com/sb529/crewai.git
cd crewai
Install the required packages:
pip install crewai python-dotenv
Create a .env file in the project root directory:
touch .env
Add your OpenAI API key to the .env file:
OPENAI_API_KEY=your-api-key-here
Usage

The main script contains:

A detailed job description for a AI Education Product Management role
A collection of sample candidate resumes
An AI agent configured to screen candidates
Run the screening system:

python recruitment_screening.py
The system will:
Analyze each candidate's qualifications
Compare them against job requirements
Provide a ranked list of top 3 candidates
Include detailed rationales for selections
How It Works

The system uses CrewAI to:

Process the job description and identify key requirements
Analyze each candidate's resume for relevant experience
Evaluate technical skills and AI/ML background
Consider product management track record
Generate comprehensive screening results
File Structure

.
├── README.md
├── .env                    # Contains API key (not in repo)
├── .gitignore
└── recruitment_screening.py # Main script with recruitment logic
Security Note

Never commit your .env file or expose your API key
The .gitignore file is configured to exclude sensitive information
