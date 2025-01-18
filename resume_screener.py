import os
from crewai import Agent, Task, Crew
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()

# Define the job description
job_description = """
Job Title: Senior Product Manager - AI Chat Assistant
About the Role:
We're seeking an innovative Product Manager to lead the development of a cutting-edge AI chat assistant that will transform user interaction and engagement. The ideal candidate will drive product strategy, user experience, and feature development for an intelligent conversational AI platform.

Key Responsibilities:
- Define product vision and roadmap for an AI chat assistant
- Conduct user research to identify key features and use cases
- Collaborate with AI/ML engineers to translate technical capabilities into user-centric features
- Design and prioritize product requirements that balance technical feasibility and user needs
- Develop and track key performance indicators (KPIs) for user adoption, engagement, and satisfaction
- Work closely with design, engineering, and data science teams to iteratively improve the product
- Manage the end-to-end product development lifecycle

Required Qualifications:
- 5+ years of product management experience, preferably in AI, SaaS, or conversational technologies
- Strong understanding of AI/ML product development
- Experience in defining product strategies for complex, intelligent software
- Excellent communication and cross-functional collaboration skills
- Proven track record of shipping successful digital products
- Deep curiosity about emerging AI technologies

Preferred Skills:
- Background in natural language processing
- Experience with generative AI products
- Technical understanding of large language models
"""

# List of resumes
resumes = [
    {
        "name": "Sarah Chen",
        "resume": "Sarah Chen leveraged her computer science background to transition into product management at a rapidly growing AI startup. She successfully launched three machine learning products that increased company revenue by 40% within two years. Her expertise in data-driven decision-making and agile methodologies enabled her to streamline product development processes. Sarah holds a Master's degree in Computer Science from Stanford University and has deep experience in user experience design. She has been recognized for her ability to bridge technical and business requirements in high-growth technology environments."
    },
    {
        "name": "Michael Rodriguez",
        "resume": "Michael Rodriguez brings 8 years of enterprise software product management experience from his tenure at Fortune 500 technology companies. He has a proven track record of managing complex SaaS products that serve large-scale business clients across multiple industries. Michael's strategic approach to product development has consistently resulted in double-digit user adoption rates and significant customer satisfaction improvements. He is skilled in conducting comprehensive market research and translating customer insights into actionable product roadmaps. Michael holds an MBA from Northwestern University with a focus on technology innovation."
    },
    {
        "name": "Elena Martinez",
        "resume": "Elena Martinez specialized in healthcare technology product management, driving digital transformation for patient engagement platforms. Her deep understanding of healthcare regulations and user-centered design helped her develop HIPAA-compliant mobile applications that improved patient communication. Elena has successfully managed cross-functional teams to deliver products that integrate complex healthcare systems and improve operational efficiency. She brings a unique blend of technical knowledge and empathy-driven design to her product management approach. Elena completed her Product Management certification from UC Berkeley's Executive Education program."
    },
    {
        "name": "Jason Wang",
        "resume": "Jason Wang has spent the last six years leading product teams in high-growth e-commerce platforms, consistently delivering revenue-generating features. His expertise in conversion optimization and user experience design has directly contributed to increasing online sales by over 60% across multiple companies. Jason is adept at using data analytics to drive product decisions and has extensive experience with A/B testing and user behavior analysis. He has managed global product teams and understands the nuances of creating scalable, user-friendly digital experiences. Jason holds a Bachelor's degree in Business Administration with a minor in Computer Science."
    },
    {
        "name": "Aria Patel",
        "resume": "Aria Patel brings a unique combination of financial expertise and product management skills from her work in fintech startups. She has developed innovative payment solutions and investment tracking tools that have been adopted by over 500,000 users. Aria's ability to understand complex financial regulations while creating intuitive user experiences sets her apart in the product management field. She has experience managing end-to-end product lifecycles and collaborating with engineering, design, and marketing teams. Aria completed her Product Management Professional Certification from MIT Professional Education."
    },
    {
        "name": "Carlos Gomez",
        "resume": "Carlos Gomez has specialized in building products for emerging markets, with extensive experience in Latin American and Southeast Asian technology ecosystems. His product management approach focuses on understanding local user needs and creating solutions that address unique market challenges. Carlos has launched mobile applications that achieved over 1 million downloads across multiple developing countries. He is skilled in conducting grassroots user research and adapting global product strategies to local contexts. Carlos holds a dual degree in International Business and Digital Innovation."
    },
    {
        "name": "Rebecca Liu",
        "resume": "Rebecca Liu has dedicated her career to transforming educational experiences through technology product management. She has developed adaptive learning platforms used by over 100 school districts, improving student engagement and learning outcomes. Rebecca's background in educational psychology enables her to create products that genuinely address learning challenges. She is experienced in managing complex stakeholder relationships, including educators, administrators, and technology teams. Rebecca completed her Master's in Learning Technologies from Columbia University's Teachers College."
    },
    {
        "name": "Alex Rodriguez",
        "resume": "Alex Rodriguez brings dynamic product management experience from the competitive gaming and entertainment technology sector. He has launched multiple gaming platforms and digital experiences that reached millions of users worldwide. Alex is expert in managing agile development teams, conducting player feedback analysis, and creating compelling digital product roadmaps. His understanding of user engagement mechanics has been critical in developing successful interactive platforms. Alex holds a Bachelor's degree in Interactive Media Design."
    },
    {
        "name": "Samira Khan",
        "resume": "Samira Khan focuses on developing technology products that address critical sustainability challenges. Her product management experience includes creating software solutions for renewable energy tracking, carbon footprint management, and sustainable supply chain optimization. Samira has a holistic approach to product development, considering environmental impact alongside traditional business metrics. She has managed international product teams and successfully launched products in European and North American markets. Samira completed her Sustainable Business Strategy certification from Harvard Business School."
    },
    {
        "name": "Daniel Park",
        "resume": "Daniel Park specializes in product management for artificial intelligence and machine learning platforms. He has extensive experience translating complex AI capabilities into user-friendly products across various industries, including healthcare, finance, and customer service. Daniel's technical background in computer science allows him to effectively communicate between engineering teams and business stakeholders. He has managed the development of AI-driven products that have significantly improved operational efficiency for enterprise clients. Daniel holds a Ph.D. in Machine Learning from Carnegie Mellon University."
    }
]

# Create Candidate Screening Agent
candidate_screener = Agent(
    role="Senior Talent Acquisition Specialist",
    goal="Identify the top 3 candidates who best match the job description for a Senior Product Manager in AI Chat Assistant development",
    backstory="""You are an experienced talent acquisition specialist with deep expertise in tech recruiting, 
    particularly in AI and product management roles. Your keen eye for detail allows you to match candidate 
    backgrounds precisely to job requirements.""",
    verbose=True,
    llm="gpt-4"
)

# Create Screening Task
screening_task = Task(
    description=f"""Carefully review the job description and each candidate's resume:
    1. Analyze how each candidate's experience aligns with the job requirements
    2. Pay special attention to:
       - Experience in AI/ML product management
       - Technical understanding of complex software products
       - Track record of successful product launches
    3. Rank the candidates and provide a detailed rationale for the top 3 selections
    4. Explain why these candidates stand out for this specific AI Chat Assistant Product Manager role

    Job Description:
    {job_description}

    Candidate Resumes:
    {', '.join([f"{candidate['name']}: {candidate['resume']}" for candidate in resumes])}
    """,
    expected_output="",
    agent=candidate_screener
)

# Instantiate the Crew
crew = Crew(
    agents=[candidate_screener],
    tasks=[screening_task],
    verbose=False,
)

# Kickoff the task
result = crew.kickoff()

print(result)
