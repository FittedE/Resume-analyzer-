from fastapi import FastAPI, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pdf_parser import extract_resume_text
from analyzer import analyze_resume 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/uploadfile")
async def upload_resume(file: UploadFile):
    text = extract_resume_text(file.file)
    return {"extracted_text": text}

@app.post("/analyze")
async def analyze(file:UploadFile,job_description: str = Form(...)):
    resume_text = extract_resume_text(file.file)
    result = analyze_resume(resume_text, job_description)
    return result     