import requests
from movie_ids import movieIds

url = "https://api.themoviedb.org/3/movie/movie_id/reviews?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzgzODU2ZWZjYWY4ZGY3YmVmODdlNmUxMDEzOTMwNiIsIm5iZiI6MTY4OTc0Mzk5MC4zNDgsInN1YiI6IjY0Yjc3Mjc2YjFmNjhkMDBhZTMzY2M2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.suktXkUgGb8v4gLebOo36vnTiS5kLMbWfPUIu_eOn54"
}

review_queries = []

for movie_id in movieIds:
    response = requests.get(url.replace("movie_id", str(movie_id)), headers=headers)
    reviews = response.json().get("results", [])
    for review in reviews:
        user_name = review.get("author_detail", {}).get("username", "Unknown")
        created_at = review.get("created_at", None)
        content = review.get("content", "").replace("'", "''")
        rating = review.get("author_detail", {}).get("rating", None)
        query = f"INSERT INTO [dbo].[review] (created_at, movie_id, user_name, rating, content) VALUES ('{created_at}', {movieIds.index(movie_id)}, '{user_name}', {rating}, N'{content}');\n"
        review_queries.append(query)
        
        print(query)
        
        
# Export file of person IDs to a text file
with open("database/sqlInsertReview.sql", "w", encoding="utf-8") as f:
    for query in review_queries:
        f.write(query + "\n")