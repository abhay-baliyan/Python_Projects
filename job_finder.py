from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
job_roles = {
    "Data Scientist": ["python", "machine learning", "statistics", "pandas", "numpy"],
    "Web Developer": ["html", "css", "javascript", "react", "django"],
    "Data Analyst": ["excel", "sql", "power bi", "tableau", "python"],
    "Backend Developer": ["python", "django", "api", "flask", "sql"],
    "Software Engineer": ["java", "python", "oops", "git", "problem solving"]
}
resume = input("Paste your resume text:\n").lower()
job_texts = []
job_names = []
for job, skills in job_roles.items():
    job_names.append(job)
    job_texts.append(" ".join(skills))
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume] + job_texts)
scores = cosine_similarity(vectors[0:1], vectors[1:])[0]
best_index = scores.argmax()
best_job = job_names[best_index]
best_score = scores[best_index] * 100
print("\n🔍 Best Matched Job Role:", best_job)
print(f"📊 Match Score: {best_score:.2f}%")
required_skills = job_roles[best_job]
missing = [skill for skill in required_skills if skill not in resume]
print("\n❌ Missing Skills for this role:")
if missing:
    for skill in missing:
        print("-", skill)
else:
    print("None 🎉 You're a perfect fit!")