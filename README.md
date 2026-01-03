# 🤖 AI Project & Hackathon Assistant

A comprehensive AI-powered platform that helps students discover project ideas, hackathon opportunities, and get implementation guidance. The platform provides beginner, medium, and advanced level project suggestions with success percentage predictions.

## ✨ Features

- **🤖 100% AI-Generated Content**: All project ideas, descriptions, tech stacks, and guidance are generated dynamically by AI
- **🎯 Project Ideas**: Get personalized, unique project suggestions based on your course (CSE, AI/ML, ECE)
- **📊 AI Success Prediction**: Intelligent AI-powered success percentage calculation for each project idea
- **📚 AI Implementation Guidance**: Step-by-step AI-generated guidance for both hardware and software projects
- **🏆 Hackathon Information**: View upcoming hackathons from universities and companies (Microsoft, Google, etc.)
- **🇮🇳 SIH Problems**: Access Smart India Hackathon problem statements
- **🎓 Academic Year Projects**: Get project suggestions tailored to your academic year for job preparation
- **🔮 Success Predictor**: Predict success percentage for your custom project ideas using AI

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- **OpenAI API Key** (for AI generation) - Get free credits at https://platform.openai.com
  - Or use Hugging Face API (free alternative)
  - Or disable AI to use hardcoded data

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI_Project_Asistant.git
   cd AI_Project_Asistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up AI (Optional but Recommended)**
   - Get OpenAI API key: https://platform.openai.com/api-keys
   - Create `.env` file (copy from `env_example.txt`)
   - Add your API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     USE_AI=true
     ```
   - **Or** set environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     export USE_AI="true"
     ```
   - See `AI_SETUP.md` for detailed instructions

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **Or run the API server**
   ```bash
   python start_api.py
   ```
   API will be available at `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

## 📁 Project Structure

```
AI_Project_Asistant/
├── app.py                 # Streamlit web application
├── api.py                 # FastAPI REST API
├── ai_brain.py            # Core AI logic for project suggestions
├── predictor.py           # Success percentage prediction algorithm
├── start_api.py           # API server startup script
├── test_api.py            # API testing script
├── requirements.txt       # Python dependencies
├── hackathons.csv         # Hackathon database
├── sih.csv                # SIH problem statements
└── README.md              # This file
```

## 🎯 Usage

### Streamlit Web App

1. Start the app: `streamlit run app.py`
2. Open your browser to `http://localhost:8501`
3. Enter your course (e.g., "BTech CSE", "AIML", "ECE")
4. Select filters (academic year, difficulty level, project type)
5. Click "Get Project Ideas" to see suggestions
6. Click "Get Implementation Guide" for detailed steps

### API Endpoints

#### Get Project Ideas
```bash
POST http://localhost:8000/projects
Content-Type: application/json

{
  "course": "BTech CSE",
  "academic_year": 3,
  "difficulty_level": "All",
  "project_type": "both"
}
```

#### Get Implementation Guidance
```bash
GET http://localhost:8000/guidance/Fake%20News%20Detection%20System?course=BTech%20CSE
```

#### Get Upcoming Hackathons
```bash
GET http://localhost:8000/hackathons?months_ahead=3
```

#### Add a Hackathon
```bash
POST http://localhost:8000/hackathons/add
Content-Type: application/json

{
  "name": "University Hackathon",
  "organizer": "Your University",
  "date": "2025-10-15",
  "location": "Online",
  "prize_pool": "INR 5 Lakhs"
}
```

#### Get SIH Problems
```bash
GET http://localhost:8000/sih?domain=AI&year=2024
```

## 🌐 Hosting on GitHub

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right → "New repository"
3. Name it: `AI_Project_Asistant` (or your preferred name)
4. Choose Public or Private
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Initialize Git in Your Project

Open terminal/command prompt in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI Project & Hackathon Assistant"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/AI_Project_Asistant.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Update Remote URL (if needed)

If you need to update the remote URL:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/AI_Project_Asistant.git
```

### Step 4: Future Updates

Whenever you make changes:

```bash
# Check status
git status

# Add changed files
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub
git push
```

## 🚀 Deploy to Streamlit Cloud (Free Hosting)

1. **Push your code to GitHub** (follow steps above)

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
   - Sign in with your GitHub account
   - Click "New app"

3. **Configure deployment**
   - Select your repository: `AI_Project_Asistant`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Your app will be live!**
   - URL format: `https://your-app-name.streamlit.app`

## 🚀 Deploy API to Render/Railway (Free Hosting)

### Option 1: Render

1. Go to [Render](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `ai-project-assistant-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn api:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"

### Option 2: Railway

1. Go to [Railway](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect Python
5. Add start command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
6. Deploy!

## 📝 API Documentation

Once the API is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit** - Web application framework
- **FastAPI** - Modern REST API framework
- **Pandas** - Data manipulation
- **Pydantic** - Data validation

## 📊 Project Categories

### AI/ML Projects
- Fake News Detection
- Chatbot for Customer Support
- Image Classification with CNN
- Traffic Management System
- Sentiment Analysis
- Recommendation System
- And more...

### CSE Projects
- E-Commerce Website
- Task Management App
- Distributed File Storage
- Microservices Architecture
- And more...

### ECE Projects
- IoT Home Automation
- Smart Health Monitoring
- Autonomous Drone
- And more...

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Smart India Hackathon for problem statements
- All hackathon organizers for their events
- The open-source community

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

⭐ If you find this project helpful, please give it a star on GitHub!

