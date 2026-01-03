from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
from datetime import datetime, timedelta
import json
import os

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, use system env vars

from ai_brain import get_project_ideas, get_implementation_guidance
from predictor import predict_success

app = FastAPI(
    title="AI Project & Hackathon Assistant API",
    description="Comprehensive API for project ideas, hackathon information, and academic guidance",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class ProjectIdea(BaseModel):
    title: str
    difficulty: str  # Beginner, Medium, Advanced
    success_percentage: float
    description: str
    tech_stack: List[str]
    hardware: str
    software: List[str]
    implementation_steps: List[str]
    estimated_time: str
    job_relevance: str

class Hackathon(BaseModel):
    name: str
    organizer: str
    date: str
    location: str
    registration_link: Optional[str] = None
    prize_pool: Optional[str] = None
    description: Optional[str] = None

class SIHProblem(BaseModel):
    year: int
    problem_statement: str
    domain: str
    difficulty: Optional[str] = None
    tech_stack: Optional[List[str]] = None

class ProjectRequest(BaseModel):
    course: str
    academic_year: Optional[int] = None  # 1, 2, 3, 4 for BTech
    difficulty_level: Optional[str] = None  # Beginner, Medium, Advanced, or All
    project_type: Optional[str] = None  # hackathon, academic, both

class HackathonRequest(BaseModel):
    name: str
    organizer: str
    date: str
    location: str
    registration_link: Optional[str] = None
    prize_pool: Optional[str] = None
    description: Optional[str] = None

# Load data from CSV files
def load_hackathons():
    try:
        df = pd.read_csv("hackathons.csv")
        return df.to_dict('records')
    except:
        return []

def load_sih_problems():
    try:
        df = pd.read_csv("sih.csv")
        records = df.to_dict('records')
        # Convert tech_stack string to list if it exists
        for record in records:
            if 'tech_stack' in record and isinstance(record['tech_stack'], str):
                # Parse comma-separated string to list
                record['tech_stack'] = [t.strip() for t in record['tech_stack'].split(',') if t.strip()]
        return records
    except:
        return []

def save_hackathons(hackathons):
    df = pd.DataFrame(hackathons)
    df.to_csv("hackathons.csv", index=False)

@app.get("/")
async def root():
    return {
        "message": "AI Project & Hackathon Assistant API",
        "version": "1.0.0",
        "endpoints": {
            "/projects": "Get project ideas based on course and preferences",
            "/hackathons": "Get upcoming hackathons",
            "/hackathons/add": "Add a new hackathon",
            "/sih": "Get SIH problem statements",
            "/guidance/{project_title}": "Get implementation guidance for a project"
        }
    }

@app.post("/projects", response_model=List[ProjectIdea])
async def get_projects(request: ProjectRequest):
    """
    Get project ideas based on course, academic year, and difficulty level.
    Returns beginner, medium, and advanced level suggestions with success percentages.
    """
    try:
        projects = get_project_ideas(
            course=request.course,
            academic_year=request.academic_year,
            difficulty_level=request.difficulty_level,
            project_type=request.project_type
        )
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/guidance/{project_title}")
async def get_guidance(project_title: str, course: str = Query(..., description="Student's course")):
    """
    Get detailed implementation guidance for a specific project.
    Includes both hardware and software implementation steps.
    """
    try:
        guidance = get_implementation_guidance(project_title, course)
        return guidance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/hackathons", response_model=List[Hackathon])
async def get_hackathons(
    months_ahead: int = Query(3, description="Number of months ahead to show hackathons")
):
    """
    Get upcoming hackathons for the next N months.
    Default is 3 months.
    """
    try:
        hackathons = load_hackathons()
        # Filter by date (next N months)
        today = datetime.now()
        future_date = today + timedelta(days=months_ahead * 30)
        
        filtered = []
        for hack in hackathons:
            try:
                hack_date = datetime.strptime(hack.get('date', ''), '%Y-%m-%d')
                if today <= hack_date <= future_date:
                    filtered.append(hack)
            except:
                continue
        
        return filtered
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/hackathons/add")
async def add_hackathon(hackathon: HackathonRequest):
    """
    Add a new hackathon. Universities and companies can use this to update hackathon information.
    """
    try:
        hackathons = load_hackathons()
        new_hackathon = hackathon.dict()
        hackathons.append(new_hackathon)
        save_hackathons(hackathons)
        return {"message": "Hackathon added successfully", "hackathon": new_hackathon}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/sih", response_model=List[SIHProblem])
async def get_sih_problems(
    domain: Optional[str] = Query(None, description="Filter by domain (AI, IoT, Web, etc.)"),
    year: Optional[int] = Query(None, description="Filter by year")
):
    """
    Get Smart India Hackathon problem statements.
    Students can discover SIH problems and get inspired.
    """
    try:
        problems = load_sih_problems()
        
        if domain:
            problems = [p for p in problems if p.get('domain', '').lower() == domain.lower()]
        
        if year:
            problems = [p for p in problems if p.get('year') == year]
        
        return problems
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predict-success")
async def predict_project_success(
    course: str = Query(..., description="Student's course"),
    project_title: str = Query(..., description="Project title"),
    difficulty: str = Query(..., description="Difficulty level: Beginner, Medium, or Advanced"),
    hardware_required: str = Query("None", description="Hardware requirements")
):
    """
    Predict the success percentage of a project idea.
    """
    try:
        success_percentage = predict_success(course, project_title, difficulty, hardware_required)
        return {
            "project_title": project_title,
            "course": course,
            "difficulty": difficulty,
            "success_percentage": success_percentage,
            "recommendation": "Highly Recommended" if success_percentage >= 75 else 
                            "Recommended" if success_percentage >= 60 else 
                            "Moderate Success Expected"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/academic-projects")
async def get_academic_projects(
    course: str = Query(..., description="Student's course"),
    academic_year: int = Query(..., description="Academic year (1-4 for BTech)"),
    focus: str = Query("job_preparation", description="Focus: job_preparation, portfolio, or both")
):
    """
    Get academic year-based project suggestions for job preparation.
    Projects are tailored to help students build skills relevant to their course and career.
    """
    try:
        projects = get_project_ideas(
            course=course,
            academic_year=academic_year,
            difficulty_level="All",
            project_type="academic"
        )
        
        # Filter and enhance with job relevance
        academic_projects = []
        for project in projects:
            if focus == "job_preparation" or focus == "both":
                project['job_relevance'] = f"Builds skills in {', '.join(project['tech_stack'][:3])} - highly valued in industry"
            academic_projects.append(project)
        
        return {
            "course": course,
            "academic_year": academic_year,
            "focus": focus,
            "projects": academic_projects,
            "career_advice": f"For {course} students in year {academic_year}, focus on building projects that demonstrate practical skills in your core subjects."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

