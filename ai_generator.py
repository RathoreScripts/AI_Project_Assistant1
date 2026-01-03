"""
AI-powered project idea generator using LLM APIs.
Generates all content dynamically using AI instead of hardcoded data.
"""
import json
import os
from typing import List, Optional, Dict
import requests

# Try to import OpenAI, fallback to other options
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Configuration
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")  # openai, huggingface, or local
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

def call_openai_api(prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 2000) -> str:
    """Call OpenAI API to generate content."""
    if not OPENAI_AVAILABLE:
        raise ImportError("OpenAI library not installed. Run: pip install openai")
    
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_openai_api_key_here":
        raise ValueError("OPENAI_API_KEY not set. Set it as environment variable or in .env file")
    
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert project advisor for students. Generate detailed, practical project ideas with complete information."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content
    except openai.AuthenticationError:
        raise ValueError("Invalid OpenAI API key. Please check your API key.")
    except openai.RateLimitError:
        raise Exception("OpenAI API rate limit exceeded. Please try again later.")
    except Exception as e:
        raise Exception(f"OpenAI API error: {str(e)}")

def call_huggingface_api(prompt: str, model: str = "mistralai/Mistral-7B-Instruct-v0.2") -> str:
    """Call Hugging Face API to generate content."""
    if not HUGGINGFACE_API_KEY:
        raise ValueError("HUGGINGFACE_API_KEY not set")
    
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    try:
        response = requests.post(api_url, headers=headers, json={"inputs": prompt}, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("generated_text", "")
        return str(result)
    except Exception as e:
        raise Exception(f"Hugging Face API error: {str(e)}")

def generate_with_ai(prompt: str) -> str:
    """Generate content using configured AI provider."""
    if AI_PROVIDER == "openai":
        return call_openai_api(prompt)
    elif AI_PROVIDER == "huggingface":
        return call_huggingface_api(prompt)
    else:
        raise ValueError(f"Unknown AI provider: {AI_PROVIDER}")

def ai_generate_project_ideas(
    course: str,
    academic_year: Optional[int] = None,
    difficulty_level: Optional[str] = None,
    project_type: Optional[str] = None,
    num_projects: int = 5
) -> List[Dict]:
    """
    Generate project ideas using AI based on user input.
    All content is AI-generated, not from hardcoded data.
    """
    # Build prompt for AI
    difficulty_text = difficulty_level if difficulty_level and difficulty_level != "All" else "Beginner, Medium, and Advanced"
    year_text = f"for {academic_year} year students" if academic_year else "for all academic years"
    type_text = f"for {project_type}" if project_type else "for both hackathon and academic projects"
    
    prompt = f"""Generate {num_projects} unique and innovative project ideas for a student pursuing {course} {year_text}.

Requirements:
- Difficulty levels: {difficulty_text}
- Project type: {type_text}
- Each project should be practical and implementable
- Include projects suitable for hackathons and academic submissions

For each project, provide:
1. title: A catchy project title
2. difficulty: One of "Beginner", "Medium", or "Advanced"
3. description: A detailed 2-3 sentence description
4. tech_stack: List of 5-7 relevant technologies/tools
5. hardware: Hardware requirements (or "None" if software-only)
6. software: List of 3-5 software tools/IDEs needed
7. implementation_steps: List of 6-8 step-by-step implementation steps
8. estimated_time: Time estimate (e.g., "3-4 weeks", "2 months")
9. job_relevance: How this project helps in job preparation (1-2 sentences)

Return ONLY a valid JSON array. Each project should be a JSON object with these exact keys:
title, difficulty, description, tech_stack (array), hardware, software (array), implementation_steps (array), estimated_time, job_relevance

Example format:
[
  {{
    "title": "AI-Powered Study Planner",
    "difficulty": "Beginner",
    "description": "An intelligent study planner that uses machine learning to optimize study schedules based on learning patterns and deadlines.",
    "tech_stack": ["Python", "Flask", "SQLite", "Scikit-learn", "React"],
    "hardware": "None",
    "software": ["Python 3.8+", "VS Code", "Node.js"],
    "implementation_steps": [
      "Set up development environment",
      "Design database schema for users and tasks",
      "Implement ML model for schedule optimization",
      "Create REST API endpoints",
      "Build frontend interface",
      "Add user authentication",
      "Test and deploy"
    ],
    "estimated_time": "3-4 weeks",
    "job_relevance": "High - Demonstrates full-stack development and ML integration skills"
  }}
]

Generate {num_projects} unique projects now:"""

    try:
        # Call AI to generate projects
        ai_response = generate_with_ai(prompt)
        
        # Parse JSON response
        # Sometimes AI adds markdown code blocks, remove them
        ai_response = ai_response.strip()
        if ai_response.startswith("```json"):
            ai_response = ai_response[7:]
        if ai_response.startswith("```"):
            ai_response = ai_response[3:]
        if ai_response.endswith("```"):
            ai_response = ai_response[:-3]
        ai_response = ai_response.strip()
        
        projects = json.loads(ai_response)
        
        # Validate and add success percentage
        from predictor import predict_success_ai
        
        result = []
        for project in projects:
            if not isinstance(project, dict):
                continue
            
            # Ensure all required fields exist
            project.setdefault("title", "Untitled Project")
            project.setdefault("difficulty", "Beginner")
            project.setdefault("description", "")
            project.setdefault("tech_stack", [])
            project.setdefault("hardware", "None")
            project.setdefault("software", [])
            project.setdefault("implementation_steps", [])
            project.setdefault("estimated_time", "N/A")
            project.setdefault("job_relevance", "")
            
            # Calculate success percentage using AI
            success_pct = predict_success_ai(
                course=course,
                project_name=project["title"],
                difficulty=project["difficulty"],
                description=project["description"],
                tech_stack=project["tech_stack"]
            )
            
            project["success_percentage"] = success_pct
            result.append(project)
        
        return result[:num_projects]
        
    except json.JSONDecodeError as e:
        raise Exception(f"AI returned invalid JSON. Response: {ai_response[:200]}... Error: {str(e)}")
    except Exception as e:
        raise Exception(f"Error generating projects with AI: {str(e)}")

def ai_generate_implementation_guidance(project_title: str, course: str, description: str = "") -> Dict:
    """
    Generate detailed implementation guidance using AI.
    All guidance is AI-generated.
    """
    prompt = f"""Generate comprehensive implementation guidance for a project: "{project_title}"

Student's course: {course}
Project description: {description if description else "Not provided"}

Provide detailed guidance including:

1. hardware_setup: Detailed steps for hardware setup (if hardware is needed, otherwise explain it's software-only)
2. software_setup: Step-by-step software installation and environment setup
3. implementation_steps: Detailed 8-10 step implementation guide
4. best_practices: List of 5-7 best practices for this project
5. common_challenges: List of 5-7 common challenges students might face
6. resources: List of 3-5 helpful resources (tutorials, documentation, etc.)
7. testing_strategy: How to test the project
8. deployment_guide: How to deploy the project

Return ONLY a valid JSON object with these exact keys:
hardware_setup, software_setup, implementation_steps (array), best_practices (array), common_challenges (array), resources (array), testing_strategy, deployment_guide

Example format:
{{
  "hardware_setup": "This is a software-only project. No hardware setup required...",
  "software_setup": "1. Install Python 3.8+...",
  "implementation_steps": ["Step 1", "Step 2", ...],
  "best_practices": ["Practice 1", "Practice 2", ...],
  "common_challenges": ["Challenge 1", "Challenge 2", ...],
  "resources": ["Resource 1", "Resource 2", ...],
  "testing_strategy": "Testing approach...",
  "deployment_guide": "Deployment steps..."
}}

Generate the guidance now:"""

    try:
        ai_response = generate_with_ai(prompt)
        
        # Clean response
        ai_response = ai_response.strip()
        if ai_response.startswith("```json"):
            ai_response = ai_response[7:]
        if ai_response.startswith("```"):
            ai_response = ai_response[3:]
        if ai_response.endswith("```"):
            ai_response = ai_response[:-3]
        ai_response = ai_response.strip()
        
        guidance = json.loads(ai_response)
        
        # Add project title
        guidance["project_title"] = project_title
        guidance["description"] = description
        
        return guidance
        
    except json.JSONDecodeError as e:
        raise Exception(f"AI returned invalid JSON. Error: {str(e)}")
    except Exception as e:
        raise Exception(f"Error generating guidance with AI: {str(e)}")

def ai_calculate_success_percentage(
    course: str,
    project_title: str,
    difficulty: str,
    description: str,
    tech_stack: List[str]
) -> float:
    """
    Use AI to calculate success percentage based on project details.
    """
    prompt = f"""Analyze this project idea and calculate its success percentage (0-100):

Course: {course}
Project Title: {project_title}
Difficulty: {difficulty}
Description: {description}
Tech Stack: {', '.join(tech_stack)}

Consider factors:
- Difficulty level appropriateness for the course
- Project feasibility
- Tech stack relevance and learning curve
- Market demand and job relevance
- Implementation complexity
- Hackathon/portfolio appeal

Return ONLY a JSON object with this format:
{{
  "success_percentage": 75.5,
  "reasoning": "Brief explanation of the score"
}}

Calculate now:"""

    try:
        ai_response = generate_with_ai(prompt)
        
        # Clean response
        ai_response = ai_response.strip()
        if ai_response.startswith("```json"):
            ai_response = ai_response[7:]
        if ai_response.startswith("```"):
            ai_response = ai_response[3:]
        if ai_response.endswith("```"):
            ai_response = ai_response[:-3]
        ai_response = ai_response.strip()
        
        result = json.loads(ai_response)
        return float(result.get("success_percentage", 70.0))
        
    except Exception as e:
        # Fallback to default calculation
        from predictor import predict_success
        return predict_success(course, project_title, difficulty, "None")

