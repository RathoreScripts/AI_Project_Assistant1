"""
AI-powered project idea generator.
Uses AI to generate all content dynamically instead of hardcoded data.
"""
import json
import random
from typing import List, Optional, Dict
import os

# Check if AI generation is enabled
USE_AI = os.getenv("USE_AI", "true").lower() == "true"

# Try to import AI generator
try:
    from ai_generator import ai_generate_project_ideas, ai_generate_implementation_guidance
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    USE_AI = False

# Fallback project bank (used only if AI is not available)
PROJECT_BANK = {
    "ai": {
        "beginner": [
            {
                "title": "Fake News Detection System",
                "description": "Detects fake news using NLP techniques and machine learning classifiers.",
                "tech_stack": ["Python", "NLP", "Scikit-learn", "Pandas", "NLTK"],
                "hardware": "None",
                "software": ["Python 3.8+", "Jupyter Notebook", "VS Code"],
                "implementation_steps": [
                    "Collect dataset of news articles (real and fake)",
                    "Preprocess text data (tokenization, stemming, stopword removal)",
                    "Extract features using TF-IDF or word embeddings",
                    "Train classification model (Naive Bayes, SVM, or Logistic Regression)",
                    "Create web interface using Flask/Streamlit",
                    "Deploy and test with new articles"
                ],
                "estimated_time": "2-3 weeks",
                "job_relevance": "High - NLP skills are in high demand in tech companies"
            },
            {
                "title": "Chatbot for Customer Support",
                "description": "Build an intelligent chatbot using NLP to answer customer queries.",
                "tech_stack": ["Python", "NLTK", "TensorFlow", "Flask", "Dialogflow"],
                "hardware": "None",
                "software": ["Python 3.8+", "Flask", "TensorFlow"],
                "implementation_steps": [
                    "Define intents and entities for your domain",
                    "Create training dataset with question-answer pairs",
                    "Train intent classification model",
                    "Implement response generation logic",
                    "Create API endpoints for chatbot",
                    "Build frontend interface",
                    "Test and refine responses"
                ],
                "estimated_time": "3-4 weeks",
                "job_relevance": "High - Chatbots are widely used in industry"
            },
            {
                "title": "Image Classification with CNN",
                "description": "Classify images using Convolutional Neural Networks (e.g., cats vs dogs, handwritten digits).",
                "tech_stack": ["Python", "TensorFlow", "Keras", "OpenCV", "NumPy"],
                "hardware": "GPU (optional, for faster training)",
                "software": ["Python 3.8+", "TensorFlow/Keras", "Jupyter Notebook"],
                "implementation_steps": [
                    "Collect and organize image dataset",
                    "Preprocess images (resize, normalize)",
                    "Split data into train/validation/test sets",
                    "Design CNN architecture",
                    "Train model with data augmentation",
                    "Evaluate model performance",
                    "Create prediction interface"
                ],
                "estimated_time": "3-4 weeks",
                "job_relevance": "Very High - Computer Vision is a core AI skill"
            }
        ],
        "medium": [
            {
                "title": "AI-Based Traffic Management System",
                "description": "Uses computer vision and ML to optimize traffic signals in real time based on vehicle density.",
                "tech_stack": ["Python", "OpenCV", "YOLO", "TensorFlow", "Flask", "Raspberry Pi"],
                "hardware": "Cameras, Raspberry Pi (optional for demo)",
                "software": ["Python 3.8+", "OpenCV", "TensorFlow", "Flask"],
                "implementation_steps": [
                    "Set up camera system or use video feeds",
                    "Implement vehicle detection using YOLO or similar",
                    "Count vehicles in each lane",
                    "Develop traffic optimization algorithm",
                    "Create real-time signal control system",
                    "Build dashboard for monitoring",
                    "Test with real or simulated traffic data"
                ],
                "estimated_time": "6-8 weeks",
                "job_relevance": "Very High - Combines AI, IoT, and real-world problem solving"
            },
            {
                "title": "Sentiment Analysis for Social Media",
                "description": "Analyze sentiment of tweets/posts in real-time using advanced NLP and deep learning.",
                "tech_stack": ["Python", "Transformers", "BERT", "Flask", "Twitter API", "PostgreSQL"],
                "hardware": "None",
                "software": ["Python 3.8+", "Hugging Face Transformers", "Flask", "PostgreSQL"],
                "implementation_steps": [
                    "Set up Twitter API access",
                    "Collect and preprocess social media data",
                    "Fine-tune BERT or RoBERTa for sentiment analysis",
                    "Implement real-time data streaming",
                    "Create database to store results",
                    "Build visualization dashboard",
                    "Deploy with API endpoints"
                ],
                "estimated_time": "5-6 weeks",
                "job_relevance": "High - Social media analytics is a growing field"
            },
            {
                "title": "Recommendation System",
                "description": "Build a recommendation engine for movies/products using collaborative filtering and content-based methods.",
                "tech_stack": ["Python", "Scikit-learn", "Pandas", "Flask", "SQLite"],
                "hardware": "None",
                "software": ["Python 3.8+", "Scikit-learn", "Flask"],
                "implementation_steps": [
                    "Collect or use existing dataset (MovieLens, etc.)",
                    "Preprocess and clean data",
                    "Implement collaborative filtering algorithm",
                    "Implement content-based filtering",
                    "Combine both approaches (hybrid)",
                    "Create user interface",
                    "Evaluate using metrics (RMSE, MAE)"
                ],
                "estimated_time": "4-5 weeks",
                "job_relevance": "Very High - Used by Netflix, Amazon, Spotify"
            }
        ],
        "advanced": [
            {
                "title": "Autonomous Vehicle Simulation",
                "description": "Simulate self-driving car behavior using reinforcement learning and computer vision.",
                "tech_stack": ["Python", "TensorFlow", "PyTorch", "OpenAI Gym", "Unity/Unreal", "ROS"],
                "hardware": "GPU (required for training)",
                "software": ["Python 3.8+", "PyTorch", "OpenAI Gym", "Unity ML-Agents"],
                "implementation_steps": [
                    "Set up simulation environment (CARLA or Unity)",
                    "Implement sensor data processing (camera, LiDAR)",
                    "Design deep RL agent (DQN, PPO, or SAC)",
                    "Train agent in simulation",
                    "Implement path planning and control",
                    "Test in various scenarios",
                    "Optimize for real-time performance"
                ],
                "estimated_time": "10-12 weeks",
                "job_relevance": "Extremely High - Cutting-edge AI research area"
            },
            {
                "title": "Medical Image Analysis with Deep Learning",
                "description": "Detect diseases from medical images (X-rays, CT scans) using advanced CNN architectures.",
                "tech_stack": ["Python", "PyTorch", "Medical Imaging Libraries", "DICOM", "Flask"],
                "hardware": "GPU (required)",
                "software": ["Python 3.8+", "PyTorch", "Pydicom", "Flask"],
                "implementation_steps": [
                    "Obtain medical imaging dataset (with proper permissions)",
                    "Preprocess DICOM images",
                    "Implement data augmentation for medical images",
                    "Design and train CNN (ResNet, DenseNet, or custom)",
                    "Implement transfer learning",
                    "Add explainability (Grad-CAM)",
                    "Create secure API for predictions",
                    "Ensure HIPAA compliance considerations"
                ],
                "estimated_time": "8-10 weeks",
                "job_relevance": "Very High - Healthcare AI is rapidly growing"
            },
            {
                "title": "Natural Language Generation System",
                "description": "Generate human-like text using GPT-style models for specific domains (news, stories, code).",
                "tech_stack": ["Python", "Transformers", "GPT-2/GPT-3", "PyTorch", "FastAPI"],
                "hardware": "GPU (required for training)",
                "software": ["Python 3.8+", "Hugging Face Transformers", "PyTorch", "FastAPI"],
                "implementation_steps": [
                    "Collect domain-specific text corpus",
                    "Preprocess and tokenize text data",
                    "Fine-tune pre-trained GPT model",
                    "Implement text generation pipeline",
                    "Add controls (temperature, top-k sampling)",
                    "Create API for text generation",
                    "Evaluate using BLEU, ROUGE metrics",
                    "Deploy with optimization"
                ],
                "estimated_time": "8-10 weeks",
                "job_relevance": "Extremely High - NLP is one of the hottest AI fields"
            }
        ]
    },
    "cse": {
        "beginner": [
            {
                "title": "E-Commerce Website",
                "description": "Build a full-stack e-commerce platform with user authentication, product catalog, and payment integration.",
                "tech_stack": ["HTML", "CSS", "JavaScript", "React", "Node.js", "MongoDB"],
                "hardware": "None",
                "software": ["VS Code", "Node.js", "MongoDB"],
                "implementation_steps": [
                    "Design database schema",
                    "Set up backend API with Node.js/Express",
                    "Implement user authentication (JWT)",
                    "Create product catalog and search",
                    "Build shopping cart functionality",
                    "Integrate payment gateway (Stripe/PayPal)",
                    "Design responsive frontend",
                    "Deploy to cloud (Heroku/AWS)"
                ],
                "estimated_time": "4-5 weeks",
                "job_relevance": "High - Full-stack development is essential"
            },
            {
                "title": "Task Management App",
                "description": "Create a task management application with features like to-do lists, reminders, and collaboration.",
                "tech_stack": ["React", "Node.js", "Express", "MongoDB", "Socket.io"],
                "hardware": "None",
                "software": ["VS Code", "Node.js", "MongoDB"],
                "implementation_steps": [
                    "Design database schema for tasks and users",
                    "Create RESTful API",
                    "Implement real-time updates with WebSockets",
                    "Build React frontend with components",
                    "Add authentication and authorization",
                    "Implement task filtering and sorting",
                    "Add notification system",
                    "Deploy application"
                ],
                "estimated_time": "3-4 weeks",
                "job_relevance": "High - Demonstrates full-stack skills"
            }
        ],
        "medium": [
            {
                "title": "Distributed File Storage System",
                "description": "Build a distributed file storage system similar to Dropbox with replication and fault tolerance.",
                "tech_stack": ["Python", "Django", "PostgreSQL", "Redis", "Docker", "AWS S3"],
                "hardware": "Multiple servers (or cloud instances)",
                "software": ["Python 3.8+", "Django", "PostgreSQL", "Docker"],
                "implementation_steps": [
                    "Design system architecture",
                    "Implement file upload/download APIs",
                    "Add file chunking and replication",
                    "Implement load balancing",
                    "Add encryption for security",
                    "Create web interface",
                    "Implement version control",
                    "Add monitoring and logging"
                ],
                "estimated_time": "8-10 weeks",
                "job_relevance": "Very High - System design skills are crucial"
            }
        ],
        "advanced": [
            {
                "title": "Microservices Architecture Platform",
                "description": "Build a scalable microservices platform with service discovery, API gateway, and container orchestration.",
                "tech_stack": ["Docker", "Kubernetes", "Spring Boot", "React", "MongoDB", "Redis", "Kafka"],
                "hardware": "Cloud infrastructure (AWS/GCP)",
                "software": ["Docker", "Kubernetes", "Java/Spring Boot", "Node.js"],
                "implementation_steps": [
                    "Design microservices architecture",
                    "Implement service discovery (Consul/Eureka)",
                    "Set up API Gateway",
                    "Containerize services with Docker",
                    "Deploy with Kubernetes",
                    "Implement inter-service communication",
                    "Add monitoring and logging (Prometheus, ELK)",
                    "Implement CI/CD pipeline"
                ],
                "estimated_time": "12-14 weeks",
                "job_relevance": "Extremely High - Modern software architecture"
            }
        ]
    },
    "ece": {
        "beginner": [
            {
                "title": "IoT Home Automation System",
                "description": "Control home appliances remotely using IoT sensors and mobile app.",
                "tech_stack": ["Arduino/ESP32", "Python", "Flask", "React Native", "MQTT"],
                "hardware": "Arduino/ESP32, Sensors, Relays",
                "software": ["Arduino IDE", "Python 3.8+", "Flask", "MQTT Broker"],
                "implementation_steps": [
                    "Set up Arduino/ESP32 with sensors",
                    "Implement MQTT communication",
                    "Create backend API for device control",
                    "Build mobile app for control",
                    "Add authentication and security",
                    "Implement scheduling features",
                    "Add data logging"
                ],
                "estimated_time": "4-5 weeks",
                "job_relevance": "High - IoT is growing rapidly"
            }
        ],
        "medium": [
            {
                "title": "Smart Health Monitoring System",
                "description": "Monitor vital signs using sensors and send alerts to doctors.",
                "tech_stack": ["Arduino", "Python", "Flask", "Machine Learning", "Mobile App"],
                "hardware": "Arduino, Heart Rate Sensor, Temperature Sensor, ESP32",
                "software": ["Arduino IDE", "Python 3.8+", "Flask", "TensorFlow"],
                "implementation_steps": [
                    "Interface sensors with Arduino",
                    "Collect and transmit sensor data",
                    "Implement anomaly detection using ML",
                    "Create alert system",
                    "Build dashboard for doctors",
                    "Add data visualization",
                    "Implement secure data transmission"
                ],
                "estimated_time": "6-8 weeks",
                "job_relevance": "Very High - Healthcare IoT is in demand"
            }
        ],
        "advanced": [
            {
                "title": "Autonomous Drone with Computer Vision",
                "description": "Build a drone that can navigate autonomously using computer vision and obstacle avoidance.",
                "tech_stack": ["Raspberry Pi", "Python", "OpenCV", "ROS", "Arduino", "PID Control"],
                "hardware": "Drone Frame, Motors, ESC, Raspberry Pi, Camera, IMU",
                "software": ["Raspberry Pi OS", "Python 3.8+", "OpenCV", "ROS"],
                "implementation_steps": [
                    "Assemble drone hardware",
                    "Implement flight control system",
                    "Add computer vision for navigation",
                    "Implement obstacle detection and avoidance",
                    "Add GPS for waypoint navigation",
                    "Implement PID controllers for stability",
                    "Test and optimize flight performance"
                ],
                "estimated_time": "12-14 weeks",
                "job_relevance": "Extremely High - Robotics and autonomous systems"
            }
        ]
    }
}

def get_project_ideas(
    course: str,
    academic_year: Optional[int] = None,
    difficulty_level: Optional[str] = None,
    project_type: Optional[str] = None
) -> List[dict]:
    """
    Get project ideas based on course, academic year, and difficulty level.
    Uses AI generation if available, otherwise falls back to hardcoded data.
    """
    # Use AI generation if enabled and available
    if USE_AI and AI_AVAILABLE:
        try:
            return ai_generate_project_ideas(
                course=course,
                academic_year=academic_year,
                difficulty_level=difficulty_level,
                project_type=project_type,
                num_projects=5
            )
        except Exception as e:
            # If AI fails, fall back to hardcoded data
            # Silently fall back - don't print in production
            pass
    
    # Fallback to hardcoded data
    course_lower = course.lower()
    
    # Determine course category
    if "ai" in course_lower or "artificial intelligence" in course_lower or "aiml" in course_lower:
        category = "ai"
    elif "cse" in course_lower or "computer science" in course_lower or "cs" in course_lower:
        category = "cse"
    elif "ece" in course_lower or "electronics" in course_lower:
        category = "ece"
    else:
        category = "cse"  # Default
    
    # Get projects based on difficulty
    if difficulty_level and difficulty_level.lower() != "all":
        difficulty = difficulty_level.lower()
        if difficulty not in ["beginner", "medium", "advanced"]:
            difficulty = "beginner"
        projects = PROJECT_BANK.get(category, {}).get(difficulty, [])
    else:
        # Return projects from all difficulty levels
        projects = []
        for diff in ["beginner", "medium", "advanced"]:
            projects.extend(PROJECT_BANK.get(category, {}).get(diff, []))
    
    # Track which difficulty level each project came from and add difficulty field
    from predictor import predict_success
    result = []
    
    beginner_projects = PROJECT_BANK.get(category, {}).get("beginner", [])
    medium_projects = PROJECT_BANK.get(category, {}).get("medium", [])
    advanced_projects = PROJECT_BANK.get(category, {}).get("advanced", [])
    
    # First, add difficulty to all projects
    for project in projects:
        # Determine difficulty based on which list it came from
        if project in beginner_projects:
            difficulty = "Beginner"
        elif project in medium_projects:
            difficulty = "Medium"
        elif project in advanced_projects:
            difficulty = "Advanced"
        else:
            difficulty = "Beginner"  # Default
        
        success_pct = predict_success(course, project["title"], difficulty, project.get("hardware", "None"))
        
        project_copy = project.copy()
        project_copy["difficulty"] = difficulty
        project_copy["success_percentage"] = success_pct
        result.append(project_copy)
    
    # Filter by academic year if specified (after adding difficulty)
    if academic_year:
        if academic_year == 1:
            result = [p for p in result if p["difficulty"].lower() == "beginner"]
        elif academic_year == 2:
            result = [p for p in result if p["difficulty"].lower() in ["beginner", "medium"]]
        elif academic_year == 3:
            result = [p for p in result if p["difficulty"].lower() in ["medium", "advanced"]]
        elif academic_year == 4:
            result = [p for p in result if p["difficulty"].lower() in ["medium", "advanced"]]
    
    # Shuffle and return (limit to 10 if too many)
    random.shuffle(result)
    return result[:10] if len(result) > 10 else result

def get_implementation_guidance(project_title: str, course: str, description: str = "") -> dict:
    """
    Get detailed implementation guidance for a specific project.
    Uses AI generation if available, otherwise falls back to hardcoded data.
    """
    # Use AI generation if enabled and available
    if USE_AI and AI_AVAILABLE:
        try:
            return ai_generate_implementation_guidance(project_title, course, description)
        except Exception as e:
            # If AI fails, fall back to hardcoded data
            # Silently fall back - don't print in production
            pass
    
    # Fallback to hardcoded data
    course_lower = course.lower()
    
    # Determine course category
    if "ai" in course_lower or "artificial intelligence" in course_lower:
        category = "ai"
    elif "cse" in course_lower or "computer science" in course_lower:
        category = "cse"
    elif "ece" in course_lower or "electronics" in course_lower:
        category = "ece"
    else:
        category = "cse"
    
    # Search for project in all difficulty levels
    for difficulty in ["beginner", "medium", "advanced"]:
        projects = PROJECT_BANK.get(category, {}).get(difficulty, [])
        for project in projects:
            if project_title.lower() in project["title"].lower() or project["title"].lower() in project_title.lower():
                return {
                    "project_title": project["title"],
                    "description": project["description"],
                    "hardware_requirements": project["hardware"],
                    "software_requirements": project["software"],
                    "tech_stack": project["tech_stack"],
                    "implementation_steps": project["implementation_steps"],
                    "estimated_time": project["estimated_time"],
                    "job_relevance": project["job_relevance"],
                    "guidance": {
                        "hardware_setup": f"For hardware setup: {project['hardware']}. Follow manufacturer documentation for installation.",
                        "software_setup": f"Install required software: {', '.join(project['software'])}. Set up development environment.",
                        "best_practices": [
                            "Start with a small prototype",
                            "Test each component separately",
                            "Use version control (Git)",
                            "Document your code",
                            "Deploy incrementally"
                        ],
                        "common_challenges": [
                            "Integration issues between components",
                            "Performance optimization",
                            "Error handling and debugging",
                            "Scalability concerns"
                        ]
                    }
                }
    
    # If project not found, return generic guidance
    return {
        "project_title": project_title,
        "message": "Project not found in database. Here's generic guidance:",
        "general_guidance": {
            "hardware": "Identify required hardware components, order them, and set up according to specifications.",
            "software": "Install development tools, set up environment, and configure dependencies.",
            "implementation": "Break down into modules, implement incrementally, test thoroughly.",
            "deployment": "Choose appropriate hosting platform, configure deployment pipeline."
        }
    }
