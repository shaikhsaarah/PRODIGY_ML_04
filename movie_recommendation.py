import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
data = {
    "Movie": ["Avengers", "Iron Man", "Thor", "Hulk", "Batman", "Superman"],
    "Action": [1, 1, 1, 1, 1, 1],
    "Comedy": [0, 1, 0, 0, 0, 0],
    "Drama": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
df
features = df[["Action", "Comedy", "Drama"]]

similarity = cosine_similarity(features)
def recommend(movie_name):
    movie_index = df[df["Movie"] == movie_name].index[0]
    scores = list(enumerate(similarity[movie_index]))
    
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print("Recommended Movies:")
    for i in scores[1:4]:
        print(df.iloc[i[0]]["Movie"])
      recommend("Avengers")
movie_name = "Batman"  # change this manually

recommend(movie_name)
