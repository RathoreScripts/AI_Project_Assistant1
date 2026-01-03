# 🚀 Streamlit Cloud Deployment - Step by Step

## ✅ Correct Steps for Streamlit Cloud

### Step 1: Make sure your code is on GitHub
- Your repository should be: `AI_Project_Asistant`
- Your main file should be: `app.py` (in the root folder)

### Step 2: Go to Streamlit Cloud
1. Visit: https://share.streamlit.io/
2. Sign in with your GitHub account

### Step 3: Create New App
1. Click **"New app"** button
2. You'll see a form with these fields:

---

## 📝 What to Enter in Each Field:

### Field 1: "Repository" (Dropdown)
- **What to do**: Click the dropdown
- **Select**: `YOUR_USERNAME/AI_Project_Asistant`
- **NOT a URL** - just select from the list

### Field 2: "Branch" (Text field)
- **What to enter**: `main`
- **Or**: `master` (if your default branch is master)

### Field 3: "Main file path" (Text field) ⚠️ THIS IS THE KEY!
- **What to enter**: `app.py`
- **NOT a URL!** Just the file name: `app.py`
- **If your file is in a subfolder**: `folder/app.py` (but yours is in root, so just `app.py`)

---

## ❌ Common Mistakes:

### ❌ DON'T Enter:
- `https://github.com/username/repo/blob/main/app.py` (URL)
- `https://github.com/username/repo` (Repository URL)
- Full file path with GitHub URL

### ✅ DO Enter:
- Just: `app.py` (in the "Main file path" field)
- Select repository from dropdown (not enter URL)

---

## 🎯 Complete Example:

When you fill the form, it should look like this:

```
Repository: [Dropdown] → Select "yourusername/AI_Project_Asistant"
Branch: main
Main file path: app.py
```

Then click **"Deploy"**

---

## 🔍 Verify Your File Structure

Make sure your GitHub repository has this structure:

```
AI_Project_Asistant/
├── app.py          ← This is your main file
├── api.py
├── ai_brain.py
├── predictor.py
├── requirements.txt
├── hackathons.csv
└── sih.csv
```

If `app.py` is in the root folder, just enter: `app.py`

---

## 🆘 Still Getting Error?

### Check These:

1. **Is `app.py` in your GitHub repository?**
   - Go to: `https://github.com/YOUR_USERNAME/AI_Project_Asistant`
   - You should see `app.py` in the file list

2. **Is the file in the root folder?**
   - If yes: Enter `app.py`
   - If in a folder: Enter `folder/app.py`

3. **Did you select the repository from dropdown?**
   - Don't type the repository name
   - Click the dropdown and select it

4. **Is your branch name correct?**
   - Usually `main` or `master`
   - Check your GitHub repository to see the branch name

---

## 📸 Visual Guide:

```
┌─────────────────────────────────────┐
│  Streamlit Cloud - New App          │
├─────────────────────────────────────┤
│                                     │
│  Repository:                        │
│  [Dropdown ▼]                      │
│  └─ yourusername/AI_Project_Asistant│
│                                     │
│  Branch:                            │
│  [main        ]                     │
│                                     │
│  Main file path:                    │
│  [app.py      ]  ← Just this!       │
│                                     │
│  [Deploy]                           │
└─────────────────────────────────────┘
```

---

## ✅ Quick Checklist:

- [ ] Code is pushed to GitHub
- [ ] Repository is public (or you've given Streamlit access)
- [ ] `app.py` exists in the root folder
- [ ] Selected repository from dropdown (not typed URL)
- [ ] Entered `app.py` in "Main file path" (not a URL)
- [ ] Branch is `main` or `master`

---

**The key is: Enter just `app.py` in the "Main file path" field, NOT a GitHub URL!**


