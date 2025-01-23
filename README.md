# AI Recruitment Screening System

This project uses CrewAI to create an intelligent recruitment screening system that helps identify the best candidates for a AI Education Product Manager position in AI Chat Assistant development.

## Features

- Automated screening of candidate resumes against job requirements
- AI-powered analysis of technical and soft skills
- Detailed ranking and rationale for top candidates
- Focus on AI/ML product management experience evaluation

## Prerequisites

Before running this project, you need to have:

- Python 3.11 or higher
- An OpenAI API key (with GPT-4 access)
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
https://github.com/Yourdarksweetheart/AI-Resume-Screener.git
cd crewai
```

2. Install the required packages:
```bash
pip install crewai python-dotenv
```

3. Create a `.env` file in the project root directory:
```bash
touch .env
```

4. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. The main script contains:
   - A detailed job description for a AI Education Product Manager role
   - A collection of sample candidate resumes
   - An AI agent configured to screen candidates

2. Run the screening system:
```bash
python recruitment_screening.py
```

3. The system will:
   - Analyze each candidate's qualifications
   - Compare them against job requirements
   - Provide a ranked list of top 3 candidates
   - Include detailed rationales for selections

## How It Works

The system uses CrewAI to:
1. Process the job description and identify key requirements
2. Analyze each candidate's resume for relevant experience
3. Evaluate technical skills and AI/ML background
4. Consider product management track record
5. Generate comprehensive screening results

## File Structure

```
.
├── README.md
├── .env                    # Contains API key (not in repo)
├── .gitignore
└── recruitment_screening.py # Main script with recruitment logic
```

## Security Note

- Never commit your `.env` file or expose your API key
- The `.gitignore` file is configured to exclude sensitive information
