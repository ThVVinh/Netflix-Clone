import requests

movieIds = [1025527, 507244, 755898, 1197137, 1218925, 861451, 1511789, 1311031, 1305717, 1284120, 
            1280450, 1156594, 354912, 1038392, 1519168, 803796, 1072699, 7451, 1290159, 338969, 
            604079, 270655, 196259, 1242898, 1007840, 617126, 1169210, 1306525, 1571470, 1272166, 
            1380998, 154400, 1257009, 1086910, 793387, 997113, 1078605, 100042, 1328402, 120, 
            1186350, 873967, 13, 1010581, 285, 272490, 1107216, 85430, 533533, 99861, 
            1327862, 9902, 49521, 283566, 166428, 575265, 138130, 810693, 1061474, 206647, 
            146, 215, 936245, 8467, 589761, 22843, 68341, 646, 414770, 63311, 
            1585, 11075, 338953, 75629, 939335, 329996, 15383, 1198426, 660, 974453, 
            652837, 10545, 10764, 3981, 1255788, 9836, 30843, 668, 297608, 738652, 
            707, 1234821, 709, 695089, 1151949, 15907, 23155, 187033, 362057, 23153]

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzgzODU2ZWZjYWY4ZGY3YmVmODdlNmUxMDEzOTMwNiIsIm5iZiI6MTY4OTc0Mzk5MC4zNDgsInN1YiI6IjY0Yjc3Mjc2YjFmNjhkMDBhZTMzY2M2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.suktXkUgGb8v4gLebOo36vnTiS5kLMbWfPUIu_eOn54"
}

ids = []
sqlqueries = []

for movieId in movieIds:
    url = f"https://api.themoviedb.org/3/movie/{movieId}/credits?language=en-US"
    response = requests.get(url, headers=headers).json()
    
    for person in response.get("cast", []):
        person_id = person.get("id")
        name = person.get("name")
        gender = 'Female' if person.get("gender") == 1 else 'Male'
        query = f"INSERT INTO people (id_actor, name, biography, dob, photo_url, gender) VALUES ({person_id}, N'{name.replace("'", "''")}', '{'PlaceHolder'}', '{'2025-01-01'}', '{'http:Placeholder'}', '{gender}');"
        sqlqueries.append(query)
        
        # character = person["character"]
        
    for person in response.get("crew", []):
        person_id = person.get("id")
        name = person.get("name")
        gender = 'Female' if person.get("gender") == 1 else 'Male'
        query = f"INSERT INTO people (id_actor, name, biography, dob, photo_url, gender) VALUES ({person_id}, N'{name.replace("'", "''")}', '{'PlaceHolder'}', '{'2025-01-01'}', '{'http:Placeholder'}', '{gender}');"
        sqlqueries.append(query)
        
        # character = person["character"]

# Export file of person IDs to a text file
with open("database/sqlInsertPeople.txt", "w", encoding="utf-8") as f:
    for query in sqlqueries:
        f.write(query + "\n")