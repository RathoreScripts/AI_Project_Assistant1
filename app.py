import streamlit as st
import pandas as pd
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

st.set_page_config(
    page_title="AI Project & Hackathon Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Project & Hackathon Assistant")
st.subheader("AI-generated project ideas with success prediction and implementation guidance")

# Sidebar for filters
with st.sidebar:
    st.header("⚙️ Filters")
    course = st.text_input("Enter your course", value="BTech CSE", help="Example: BTech CSE, AIML, ECE")
    academic_year = st.selectbox("Academic Year", [None, 1, 2, 3, 4], format_func=lambda x: "All Years" if x is None else f"Year {x}")
    difficulty_level = st.selectbox("Difficulty Level", ["All", "Beginner", "Medium", "Advanced"])
    project_type = st.selectbox("Project Type", ["both", "hackathon", "academic"])

# Main content
if st.button("Get Project Ideas", type="primary"):
    try:
        projects = get_project_ideas(
            course=course,
            academic_year=academic_year,
            difficulty_level=difficulty_level if difficulty_level != "All" else None,
            project_type=project_type
        )

        if projects:
            st.success(f"🎉 Found {len(projects)} project ideas!")
            
            for idx, project in enumerate(projects, 1):
                with st.expander(f"📌 {project['title']} - {project['difficulty']} ({project['success_percentage']}% Success Rate)", expanded=(idx == 1)):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Success Rate", f"{project['success_percentage']}%")
                    with col2:
                        st.metric("Difficulty", project['difficulty'])
                    with col3:
                        st.metric("Time Estimate", project.get('estimated_time', 'N/A'))
                    
                    st.markdown("---")
                    st.write(f"**Description:** {project['description']}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("**Tech Stack:**")
                        st.write(", ".join(project['tech_stack']))
                        st.write("**Software Required:**")
                        st.write(", ".join(project.get('software', ['N/A'])))
                    with col2:
                        st.write("**Hardware Required:**")
                        st.write(project.get('hardware', 'None'))
                        st.write("**Job Relevance:**")
                        st.write(project.get('job_relevance', 'N/A'))
                    
                    if st.button(f"Get Implementation Guide", key=f"guide_{idx}"):
                        guidance = get_implementation_guidance(project['title'], course)
                        st.session_state[f'guidance_{idx}'] = guidance
                    
                    if f'guidance_{idx}' in st.session_state:
                        guidance = st.session_state[f'guidance_{idx}']
                        st.markdown("### 📋 Implementation Steps:")
                        for step_num, step in enumerate(guidance.get('implementation_steps', []), 1):
                            st.write(f"{step_num}. {step}")
                        
                        if 'guidance' in guidance:
                            st.markdown("### 💡 Best Practices:")
                            for practice in guidance['guidance'].get('best_practices', []):
                                st.write(f"• {practice}")
        else:
            st.warning("No projects found. Try adjusting your filters.")

    except Exception as e:
        st.error("Something went wrong")
        st.code(str(e))
        st.exception(e)

# ---------- HACKATHONS SECTION ----------
st.markdown("---")
st.header("🏆 Upcoming Hackathons")

try:
    hackathons_df = pd.read_csv("hackathons.csv")
    if not hackathons_df.empty:
        # Filter by date (next 3 months)
        from datetime import datetime, timedelta
        today = datetime.now()
        future_date = today + timedelta(days=90)
        
        hackathons_df['date'] = pd.to_datetime(hackathons_df['date'], errors='coerce')
        upcoming = hackathons_df[hackathons_df['date'] <= future_date].sort_values('date')
        
        if not upcoming.empty:
            st.dataframe(
                upcoming[['name', 'organizer', 'date', 'location', 'prize_pool']],
                use_container_width=True
            )
        else:
            st.info("No upcoming hackathons in the next 3 months. Check back later!")
    else:
        st.warning("No hackathon data available")
except Exception as e:
    st.warning(f"Could not load hackathons: {str(e)}")

# ---------- SIH DATA ----------
st.markdown("---")
st.header("🏆 Smart India Hackathon Problems")

try:
    sih_df = pd.read_csv("sih.csv")
    if not sih_df.empty:
        # Add filters for SIH
        col1, col2 = st.columns(2)
        with col1:
            domain_filter = st.selectbox("Filter by Domain", ["All"] + list(sih_df['domain'].unique()))
        with col2:
            year_filter = st.selectbox("Filter by Year", ["All"] + sorted(sih_df['year'].unique().tolist(), reverse=True))
        
        filtered_sih = sih_df.copy()
        if domain_filter != "All":
            filtered_sih = filtered_sih[filtered_sih['domain'] == domain_filter]
        if year_filter != "All":
            filtered_sih = filtered_sih[filtered_sih['year'] == year_filter]
        
        st.dataframe(filtered_sih, use_container_width=True)
    else:
        st.warning("No SIH data available")
except Exception as e:
    st.warning(f"Could not load SIH data: {str(e)}")

# ---------- SUCCESS PREDICTOR ----------
st.markdown("---")
st.header("🔮 Project Success Predictor")

col1, col2 = st.columns(2)
with col1:
    pred_course = st.text_input("Course", value="BTech CSE", key="pred_course")
    pred_project = st.text_input("Project Title", key="pred_project")
with col2:
    pred_difficulty = st.selectbox("Difficulty", ["Beginner", "Medium", "Advanced"], key="pred_difficulty")
    pred_hardware = st.text_input("Hardware Required", value="None", key="pred_hardware")

if st.button("Predict Success", key="predict"):
    if pred_project:
        try:
            success_pct = predict_success(pred_course, pred_project, pred_difficulty, pred_hardware)
            st.metric("Predicted Success Percentage", f"{success_pct}%")
            
            if success_pct >= 75:
                st.success("✅ Highly Recommended! This project has excellent success potential.")
            elif success_pct >= 60:
                st.info("👍 Recommended. Good project with solid success potential.")
            else:
                st.warning("⚠️ Moderate Success Expected. Consider refining the idea or adjusting difficulty.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a project title")
