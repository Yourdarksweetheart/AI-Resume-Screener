# AI Resume Screener: Recruitment Screening System

## Overview

This project leverages **CrewAI** to create an intelligent recruitment screening system designed to identify the best candidates for an **AI Education Product Manager** position. The system automates the resume screening process, analyzes both technical and soft skills, and ranks candidates based on their qualifications and experience.

### Key Features:
- **Automated Screening:** Automatically screens resumes against predefined job requirements.
- **AI-Powered Analysis:** Evaluates technical skills, AI/ML knowledge, and product management experience.
- **Ranking & Rationale:** Provides a detailed ranking of top candidates with clear rationales for selection.
- **Focus on AI Education Product Management Experience:** Tailored to evaluate candidates for the AI Education Product Manager role.

## Prerequisites

Before running this project, ensure you have the following:

- **Python 3.11 or higher** installed
- **OpenAI API Key** (with GPT-4 access)
- **pip** (Python package installer)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sb529/crewai.git
cd crewai

### 2. Install the required packages
pip install crewai python-dotenv

3. Set up the environment
Create a .env file in the project root directory to store your OpenAI API key:

touch .env
Add your OpenAI API key to the .env file:

OPENAI_API_KEY=your-api-key-here

4. Security Note
Never commit your .env file or expose your API key publicly. The .gitignore file is configured to ensure that sensitive information is not pushed to the repository.

Usage

Running the Screening System
Once everything is set up, you can run the screening system with the following command:

python recruitment_screening.py
What happens when you run the system:
The system will analyze each candidate's resume.
It will compare candidates' qualifications against the job requirements.
A ranked list of top 3 candidates will be generated based on the evaluation criteria.
A detailed rationale will be provided for each selection, helping you understand why each candidate was chosen.

How It Works

The AI Resume Screener uses CrewAI to:

Process the job description and extract key requirements.
Analyze each candidate’s resume, focusing on relevant experience, technical skills, AI/ML expertise, and product management background.
Generate a ranked list of candidates based on how well they meet the job requirements and their qualifications.
Provide a rationale for each selection, making the recruitment process more transparent and objective.
File Structure

The repository consists of the following files:

.
├── README.md                  # Project overview and instructions
├── .env                        # Contains OpenAI API key (not committed to the repository)
├── .gitignore                  # Files to be excluded from version control
└── recruitment_screening.py    # Main script that handles the recruitment screening logic
Future Improvements

Extend the screening system to evaluate other roles in the AI/EdTech industry.
Incorporate additional data sources, such as LinkedIn profiles, for more comprehensive analysis.
Add functionality for real-time feedback and further personalization of candidate evaluations.
License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

Acknowledgements

CrewAI for providing the AI framework used in this project.
OpenAI for the GPT-4 API, powering the AI-driven analysis.
