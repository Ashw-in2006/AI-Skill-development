import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Sample dataset of job roles and required skills
data = {
    'Job Role': ['Software Developer', 'Data Scientist', 'Digital Marketer'],
    'Skills': [
        ['Python', 'JavaScript', 'SQL'],
        ['Python', 'Statistics', 'Machine Learning'],
        ['SEO', 'Google Ads', 'Social Media Marketing']
    ]
}

df = pd.DataFrame(data)

# Convert skills into a format that can be used for similarity calculation
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
X = vectorizer.fit_transform(df['Skills'].apply(','.join))

# Find the closest match for the user profile
user_profile = ['Python', 'SQL', 'Machine Learning']  # Example user skills

user_vector = vectorizer.transform([','.join(user_profile)])

# Nearest Neighbors for recommendation
nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(user_vector)

# Recommended job role
recommended_job = df.iloc[indices[0][0]]['Job Role']
print(f"Recommended Job Role: {recommended_job}")
