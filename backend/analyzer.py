from anthropic import Anthropic
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY is missing")
client = Anthropic(api_key=api_key)
tools = [
    {
        "name": "submit_resume_analysis",
        "description": "Submit strcuted analysis of a resume agaisnt a job description",
        "input_schema": {
            "type": "object",
            "properties": {
                "match_score": {"type": "integer", "description": "0-100 score"},
                "matched_keywords": {"type": "array", "items": {"type": "string"}},
                "missing_keywords": {"type": "array", "items": {"type": "string"}},
                "strengths": {"type": "array", "items": {"type": "string"}},
                "weaknesses": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["match_score", "matched_keywords", "missing_keywords", "strengths", "weaknesses"],
        },
    }
        
]
def analyze_resume(resume_text, job_description):
    message = client.messages.create (
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "tool", "name": "submit_resume_analysis"},
    messages= [
        {"role": "user", "content": f"Analyze this reusme against this job description. \n\nResume:\n{resume_text}\n{job_description}"}
    ],
)
    return message.content[0].input