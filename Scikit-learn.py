# Sample progress tracker for a student
progress = {
    'Python for Beginners': 50,  # 50% completion
    'Advanced Data Science': 20,  # 20% completion
    'SEO Mastery': 10            # 10% completion
}

def provide_feedback(course_progress):
    for course, progress_percentage in course_progress.items():
        if progress_percentage < 50:
            print(f"Keep going with {course}. You're almost there!")
        else:
            print(f"Great job on completing {course}. Time to take the next step!")
            
provide_feedback(progress)