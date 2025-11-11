import requests

url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=5"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzgzODU2ZWZjYWY4ZGY3YmVmODdlNmUxMDEzOTMwNiIsIm5iZiI6MTY4OTc0Mzk5MC4zNDgsInN1YiI6IjY0Yjc3Mjc2YjFmNjhkMDBhZTMzY2M2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.suktXkUgGb8v4gLebOo36vnTiS5kLMbWfPUIu_eOn54"
}

response = requests.get(url, headers=headers).json()

ids = []
base_img_url = "https://image.tmdb.org/t/p/w500"
for movie in response["results"]:
    id = movie.get("id", None)
    title = movie.get("title", "").replace("'", "''")  # escape dấu nháy
    description = movie.get("overview", "").replace("'", "''")
    release_date = movie.get("release_date", None)
    rater_count = movie.get("vote_count", 0)
    rating = round(movie.get("vote_average", 0) / 2, 1)
    price = round((rating * 1.50), 2)
    poster_path = movie.get("poster_path", None) 
    poster_url = f"{base_img_url}{poster_path}" if poster_path else ""

    url1 = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    response1 = requests.get(url1, headers=headers).json()
    duration = response1.get("runtime", 0)

    sql = f"""
    INSERT INTO movie (title, description, release_date, raterCount, rating, poster_url, price, duration)
    VALUES (N'{title}', N'{description}', '{release_date}', {rater_count}, {rating}, '{poster_url}', {price}, {duration});
    """.strip()
    ids.append(id)
    print(sql)
    
    
print(ids)