# 🚀 Deployment Guide

## Quick Deployment Steps

### 1. GitHub Setup (First Time)

```bash
# Navigate to your project folder
cd AI_Project_Asistant

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: AI Project & Hackathon Assistant"

# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/AI_Project_Asistant.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 2. Streamlit Cloud Deployment (Free)

1. **Push code to GitHub** (see step 1)

2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
   - Sign in with GitHub
   - Click "New app"

3. **Configure:**
   - Repository: Select `AI_Project_Asistant`
   - Branch: `main`
   - Main file: `app.py`
   - Click "Deploy"

4. **Your app is live!** 🎉
   - URL: `https://your-app-name.streamlit.app`

### 3. API Deployment (Render - Free)

1. **Go to [Render](https://render.com)**
   - Sign up with GitHub

2. **Create New Web Service:**
   - Connect repository: `AI_Project_Asistant`
   - Name: `ai-project-api`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api:app --host 0.0.0.0 --port $PORT`

3. **Deploy!**
   - Your API will be at: `https://ai-project-api.onrender.com`

### 4. API Deployment (Railway - Free)

1. **Go to [Railway](https://railway.app)**
   - Sign up with GitHub

2. **New Project:**
   - Deploy from GitHub repo
   - Select `AI_Project_Asistant`

3. **Configure:**
   - Add start command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
   - Deploy!

## Updating Your Deployment

After making changes:

```bash
# Add changes
git add .

# Commit
git commit -m "Your update message"

# Push to GitHub
git push
```

Streamlit Cloud and other platforms will automatically redeploy!

## Environment Variables (if needed)

If you need to add environment variables:

1. **Streamlit Cloud**: Settings → Secrets
2. **Render**: Environment → Environment Variables
3. **Railway**: Variables tab

## Troubleshooting

### Import Errors
- Make sure all files are in the same directory
- Check `requirements.txt` has all dependencies

### CSV File Errors
- Ensure `hackathons.csv` and `sih.csv` are in the root directory
- Check file paths in code

### Port Issues
- For local: Use default ports (8501 for Streamlit, 8000 for API)
- For deployment: Use `$PORT` environment variable

## Need Help?

Open an issue on GitHub or check the main README.md file.

