import streamlit as st

# Title and Description
st.title("AI-powered Skill Development Platform")
st.write("This platform will help you assess your current skills and recommend courses to improve your employability.")

# User Input
user_skills = st.text_input("Enter your current skills (comma-separated):")
career_aspirations = st.text_input("Enter your career aspirations (e.g., Data Scientist, Software Developer):")

# Recommendations
if user_skills and career_aspirations:
    user_skills_list = user_skills.split(',')
    recommended_job = recommend_courses(user_skills_list)
    st.write(f"Recommended Courses based on your skills: {recommended_job}")
else:
    st.write("Please provide your skills and career aspirations to get recommendations.")