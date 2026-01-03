from typing import List

def predict_success(course: str, project_name: str, difficulty: str, hardware_required: str) -> float:
    """
    Predict success percentage of a project idea based on multiple factors.
    Returns a value between 0 and 100.
    This is a fallback method when AI is not available.
    """
    # Base score by difficulty
    base_score = {
        "Beginner": 75,
        "beginner": 75,
        "Medium": 60,
        "medium": 60,
        "Advanced": 45,
        "advanced": 45
    }.get(difficulty, 50)
    
    score = base_score
    
    # Course relevance check
    course_lower = course.lower()
    project_lower = project_name.lower()
    
    # Check if project keywords match course
    course_keywords = {
        "ai": ["ai", "artificial intelligence", "machine learning", "deep learning", "neural", "nlp", "computer vision"],
        "cse": ["web", "app", "software", "system", "database", "api", "cloud"],
        "ece": ["iot", "sensor", "arduino", "raspberry", "embedded", "hardware", "circuit"]
    }
    
    # Determine course type
    if any(kw in course_lower for kw in ["ai", "artificial", "aiml"]):
        relevant_keywords = course_keywords["ai"]
    elif any(kw in course_lower for kw in ["cse", "computer science", "cs"]):
        relevant_keywords = course_keywords["cse"]
    elif any(kw in course_lower for kw in ["ece", "electronics"]):
        relevant_keywords = course_keywords["ece"]
    else:
        relevant_keywords = course_keywords["cse"]  # Default
    
    # Check project relevance
    if any(keyword in project_lower for keyword in relevant_keywords):
        score += 10
    
    # Hackathon-friendly keywords (increase success chance)
    hackathon_keywords = [
        "smart", "ai", "ml", "automation", "health", "traffic", 
        "security", "iot", "blockchain", "ar", "vr", "sustainability",
        "education", "agriculture", "finance"
    ]
    
    hackathon_bonus = sum(5 for keyword in hackathon_keywords if keyword in project_lower)
    score += min(hackathon_bonus, 15)  # Cap at 15 points
    
    # Software-only bonus (easier to implement)
    if hardware_required.lower() == "none" or hardware_required.lower() == "":
        score += 5
    
    # Industry relevance keywords
    industry_keywords = [
        "cloud", "microservices", "api", "rest", "docker", "kubernetes",
        "react", "angular", "node", "python", "java", "spring",
        "tensorflow", "pytorch", "aws", "azure", "gcp"
    ]
    
    industry_bonus = sum(2 for keyword in industry_keywords if keyword in project_lower)
    score += min(industry_bonus, 10)  # Cap at 10 points
    
    # Ensure score is within bounds
    score = max(30, min(score, 95))  # Between 30% and 95%
    
    return round(score, 2)

def predict_success_ai(
    course: str,
    project_name: str,
    difficulty: str,
    description: str = "",
    tech_stack: List[str] = None
) -> float:
    """
    AI-powered success prediction.
    Falls back to regular prediction if AI is not available.
    """
    try:
        from ai_generator import ai_calculate_success_percentage
        return ai_calculate_success_percentage(course, project_name, difficulty, description, tech_stack or [])
    except Exception:
        # Fallback to regular prediction
        return predict_success(course, project_name, difficulty, "None")
