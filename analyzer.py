import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert technical recruiter.

Analyze this candidate's resume against the following job description.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Evaluate:

1. Technical skill match
2. Relevant experience
3. Project relevance
4. Education
5. Overall role fit

Return exactly:

MATCH_SCORE: <number from 0 to 100>

MATCHED_SKILLS:
- skill 1
- skill 2

MISSING_SKILLS:
- skill 1
- skill 2

STRENGTHS:
- strength 1
- strength 2

WEAKNESSES:
- weakness 1
- weakness 2

RECOMMENDATION:
<SHORTLIST / CONSIDER / REJECT>

EXPLANATION:
<brief explanation>
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text