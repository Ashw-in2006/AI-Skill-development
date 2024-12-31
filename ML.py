courses_data = {
    'Course Name': ['Python for Beginners', 'Advanced Data Science', 'SEO Mastery'],
    'Skills Developed': [
        ['Python', 'Data Structures'],
        ['Machine Learning', 'Data Science', 'Statistics'],
        ['SEO', 'Google Analytics', 'Content Marketing']
    ]
}

course_df = pd.DataFrame(courses_data)

# Match the skills developed by the courses to the skills needed for the job
def recommend_courses(job_skills):
    recommended_courses = []
    for _, row in course_df.iterrows():
        match_score = len(set(row['Skills Developed']).intersection(set(job_skills)))
        if match_score > 0:
            recommended_courses.append((row['Course Name'], match_score))
    
    # Sort courses by match score
    recommended_courses.sort(key=lambda x: x[1], reverse=True)
    return recommended_courses

recommended_courses = recommend_courses(['Python', 'SQL', 'Machine Learning'])
for course in recommended_courses:
    print(f"Recommended Course: {course[0]}")