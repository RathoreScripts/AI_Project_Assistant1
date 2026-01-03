# 🤖 AI Setup Guide

## Overview

Your project now uses **AI to generate all content dynamically** instead of hardcoded data:
- ✅ AI-generated project ideas
- ✅ AI-generated descriptions
- ✅ AI-generated tech stacks
- ✅ AI-generated implementation steps
- ✅ AI-calculated success percentages
- ✅ AI-generated guidance

## Setup Instructions

### Option 1: OpenAI (Recommended)

1. **Get OpenAI API Key:**
   - Go to: https://platform.openai.com/api-keys
   - Sign up or log in
   - Create a new API key
   - Copy the key

2. **Set Environment Variable:**
   
   **Windows (PowerShell):**
   ```powershell
   $env:OPENAI_API_KEY="your-api-key-here"
   $env:USE_AI="true"
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   set OPENAI_API_KEY=your-api-key-here
   set USE_AI=true
   ```
   
   **Linux/Mac:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   export USE_AI="true"
   ```

3. **Or Create .env file:**
   - Copy `.env.example` to `.env`
   - Add your API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   USE_AI=true
   AI_PROVIDER=openai
   ```

4. **Install dependencies:**
   ```bash
   pip install python-dotenv openai
   ```

5. **Update your code to load .env:**
   Add this at the top of `app.py` and `api.py`:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Option 2: Hugging Face (Free Alternative)

1. **Get Hugging Face API Key:**
   - Go to: https://huggingface.co/settings/tokens
   - Create a new token
   - Copy the token

2. **Set Environment Variables:**
   ```bash
   export HUGGINGFACE_API_KEY="your-token-here"
   export AI_PROVIDER="huggingface"
   export USE_AI="true"
   ```

### Option 3: Use Hardcoded Data (No API Key Needed)

If you don't want to use AI:
```bash
export USE_AI="false"
```

Or in `.env`:
```
USE_AI=false
```

## Testing AI Generation

### Test Locally:

1. **Set your API key:**
   ```bash
   export OPENAI_API_KEY="your-key"
   export USE_AI="true"
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Test:**
   - Enter a course name
   - Click "Get Project Ideas"
   - You should see AI-generated projects!

### Test API:

```bash
python start_api.py
```

Then test with:
```bash
python test_api.py
```

## Cost Considerations

### OpenAI:
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens (very cheap)
- **GPT-4**: More expensive but better quality
- For this project, GPT-3.5-turbo is sufficient and cost-effective

### Hugging Face:
- **Free tier**: Limited requests
- **Paid**: More requests available

## Troubleshooting

### "OpenAI API key not set"
- Make sure you set the environment variable
- Or create `.env` file with your key
- Restart your terminal/app after setting

### "AI generation failed"
- Check your API key is correct
- Check you have API credits (OpenAI)
- Check internet connection
- Falls back to hardcoded data automatically

### "Module not found: openai"
- Run: `pip install openai python-dotenv`

### Want to disable AI?
- Set `USE_AI=false` in environment or `.env`
- Project will use hardcoded data

## Deployment with AI

### Streamlit Cloud:
1. Go to your app settings
2. Click "Secrets"
3. Add:
   ```
   OPENAI_API_KEY=your-key-here
   USE_AI=true
   ```

### Render/Railway:
1. Go to Environment Variables
2. Add:
   - `OPENAI_API_KEY` = your key
   - `USE_AI` = true

## Security Notes

⚠️ **Never commit your API key to GitHub!**

- ✅ Use `.env` file (already in `.gitignore`)
- ✅ Use environment variables
- ✅ Use platform secrets (Streamlit Cloud, Render, etc.)
- ❌ Never put API keys in code
- ❌ Never commit `.env` file

## Next Steps

1. Get your OpenAI API key
2. Set it as environment variable or in `.env`
3. Run the app and see AI-generated projects!
4. Deploy with API key in platform secrets

---

**Your project now generates unique, AI-powered project ideas every time! 🚀**

