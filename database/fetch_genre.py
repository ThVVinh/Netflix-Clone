import requests

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzgzODU2ZWZjYWY4ZGY3YmVmODdlNmUxMDEzOTMwNiIsIm5iZiI6MTY4OTc0Mzk5MC4zNDgsInN1YiI6IjY0Yjc3Mjc2YjFmNjhkMDBhZTMzY2M2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.suktXkUgGb8v4gLebOo36vnTiS5kLMbWfPUIu_eOn54"
}

response = requests.get(url, headers=headers)

for genre in response.json()["genres"]:
    name = genre["name"].replace("'", "''")  # xử lý dấu nháy đơn nếu có
    print(f"INSERT INTO genre (name) VALUES ('{name}');")
    
