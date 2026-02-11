from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_description):

    texts = [resume_text, job_description]

    cv = CountVectorizer(stop_words='english')
    matrix = cv.fit_transform(texts)

    similarity = cosine_similarity(matrix)[0][1]

    return round(similarity * 100, 2)


def missing_skills(resume_text, job_description):

    resume_words = set(resume_text.split())
    jd_words = set(job_description.lower().split())

    missing = jd_words - resume_words

    return list(missing)[:15]
