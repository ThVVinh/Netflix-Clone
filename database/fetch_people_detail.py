import requests
from people_ids import people_id_list

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzgzODU2ZWZjYWY4ZGY3YmVmODdlNmUxMDEzOTMwNiIsIm5iZiI6MTY4OTc0Mzk5MC4zNDgsInN1YiI6IjY0Yjc3Mjc2YjFmNjhkMDBhZTMzY2M2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.suktXkUgGb8v4gLebOo36vnTiS5kLMbWfPUIu_eOn54"
}

base_url = "https://image.tmdb.org/t/p/w500"
people_details = []

for person_id in people_id_list:
    url = f"https://api.themoviedb.org/3/person/{person_id}?language=en-US"
    response = requests.get(url, headers=headers).json()
    
    birthday = response.get("birthday", "''")
    biography = response.get("biography", "").replace("'", "''")
    photo_url = base_url + response.get("profile_path") if response.get("profile_path") else ""
    
    sql = f"""
    UPDATE [dbo].[people]
    SET biography = N'{biography}', dob = '{birthday}', photo_url = '{photo_url}'
    WHERE id = {people_id_list.index(person_id) + 1};
    """.strip()

    people_details.append(sql)
    print(sql)
    
        
with open("database/sql_people_detail.sql", "w", encoding="utf-8") as file:
    for info in people_details:
        file.write(info + "\n")