import requests

dict = {"Action": 17, "Adventure": 19, "Animation": 18, "Children": 5, "Comedy": 4, "Crime": 10, "Documentary": 11,
        "Drama": 1, "Fantasy": 13, "Film-Noir": 15, "History": 20, "Horror": 2, "IMAX": 16,
        "Musical": 3, "Mystery": 9, "Romance": 7, "Science Fiction": 21, "Sci-Fi": 12,
        "Thriller": 8, "TV Movie": 22, "War": 14, "Western": 6}
movieIds = [1025527, 507244, 755898, 1197137, 1218925, 861451, 1511789, 1311031, 1305717, 1284120, 1280450, 1156594, 354912, 1038392, 1519168, 803796, 1072699, 7451, 1290159, 338969, 604079, 270655, 196259, 1242898, 1007840, 617126, 1169210, 1306525, 1571470, 1272166, 1380998, 154400, 1257009, 1086910, 793387, 997113, 1078605, 100042, 1328402, 120, 1186350, 873967, 13, 1010581, 285, 272490, 1107216, 85430, 533533, 99861, 1327862, 9902, 49521, 283566, 166428, 575265, 138130, 810693, 1061474, 206647, 146, 215, 936245, 8467, 589761, 22843, 68341, 646, 414770, 63311, 1585, 11075, 338953, 75629, 939335, 329996, 15383, 1198426, 660, 974453, 652837, 10545, 10764, 3981, 1255788, 9836, 30843, 668, 297608, 738652, 707, 1234821, 709, 695089, 1151949, 15907, 23155, 187033, 362057, 23153]

film_dict = {
    "Abyss": 1,
    "Afterburn": 2,
    "War of the Worlds": 3,
    "Black Phone 2": 4,
    "Chainsaw Man - The Movie: Reze Arc": 5,
    "Martin": 6,
    "Captain Hook - The Cursed Tides": 7,
    "Demon Slayer: Kimetsu no Yaiba Infinity Castle": 8,
    "Hunting Grounds": 9,
    "The Ugly Stepsister": 10,
    "Stolen Girl": 11,
    "Our Fault": 12,
    "Coco": 13,
    "The Conjuring: Last Rites": 14,
    "The Jester 2": 15,
    "KPop Demon Hunters": 16,
    "Inside Furioza": 17,
    "xXx": 18,
    "A House of Dynamite": 19,
    "The Toxic Avenger Unrated": 20,
    "The Long Walk": 21,
    "People: A Musical Celebration": 22,
    "Beyond the Curtain": 23,
    "Predator: Badlands": 24,
    "Three Jolly Fellows": 25,
    "The Fantastic 4: First Steps": 26,
    "The Mannequin": 27,
    "The Elixir": 28,
    "The Rats: A Witcher Tale": 29,
    "Ballad of a Small Player": 30,
    "The Drop": 32,
    "Primitive War": 33,
    "The Lost Princess": 34,
    "Holy Night: Demon Hunters": 35,
    "Hedda": 36,
    "Weapons": 37,
    "Dumb and Dumber To": 38,
    "The People In The Walls": 39,
    "The Lord of the Rings: The Fellowship of the Ring": 40,
    "Marco": 41,
    "The Devil’s Trap": 42,
    "Forrest Gump": 43,
    "My Fault": 44,
    "Pirates of the Caribbean: At World's End": 45,
    "Pets on a Train": 47,
    "Girl Play": 48,
    "TRON: Ares": 49,
    "Avengers: Age of Ultron": 50,
    "Regretting You": 51,
    "Wrong Turn": 52,
    "Man of Steel": 53,
    "Evangelion: 3.0+1.0 Thrice Upon a Time": 54,
    "How to Train Your Dragon: The Hidden World": 55,
    "Mission: Impossible - The Final Reckoning": 56,
    "Kelly + Victor": 57,
    "Jujutsu Kaisen 0": 58,
    "Superman": 59,
    "Spectre": 60,
    "Crouching Tiger, Hidden Dragon": 61,
    "Saw II": 62,
    "Hidden Face": 63,
    "Dumb and Dumber": 64,
    "Chernobyl: Abyss": 65,
    "Evangelion: 2.0 You Can (Not) Advance": 66,
    "Cold Fish": 67,
    "Dr. No": 68,
    "Antiporno": 69,
    "The Skin I Live In": 70,
    "It's a Wonderful Life": 71,
    "Audition": 72,
    "Fantastic Beasts: The Secrets of Dumbledore": 73,
    "Evangelion: 3.0 You Can (Not) Redo": 74,
    "Muzzle": 75,
    "Dumbo": 76,
    "Army of Shadows": 77,
    "Captain Avispa": 78,
    "Thunderball": 79,
    "Absolution": 80,
    "Josee, the Tiger and the Fish": 81,
    "The Hunchback of Notre Dame": 82,
    "Quantum of Solace": 83,
    "What Women Want": 84,
    "The Gardener": 85,
    "Happy Feet": 86,
    "Antique": 87,
    "On Her Majesty's Secret Service": 88,
    "The Taking of Deborah Logan": 89,
    "Copshop": 90,
    "A View to a Kill": 91,
    "Jurassic World Rebirth": 92,
    "Licence to Kill": 93,
    "Onoda: 10,000 Nights in the Jungle": 94,
    "The Shadow Strays": 95,
    "Duma": 96,
    "The Garden of Sinners: Paradox Spiral": 97,
    "Women": 98,
    "Martyrs": 99,
    "The Garden of Sinners: Remaining Sense of Pain": 100
}

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYzgzODU2ZWZjYWY4ZGY3YmVmODdlNmUxMDEzOTMwNiIsIm5iZiI6MTY4OTc0Mzk5MC4zNDgsInN1YiI6IjY0Yjc3Mjc2YjFmNjhkMDBhZTMzY2M2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.suktXkUgGb8v4gLebOo36vnTiS5kLMbWfPUIu_eOn54"
}


for movie_id in movieIds:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers).json()
    movie_id = film_dict.get(response.get("title", None), None)
    
    for genreDetail in response["genres"]:
        genre_name = genreDetail.get("name", "")
        genre_id = dict.get(genre_name, None)

        sql = f"""
        INSERT INTO movie_genre (movie_id, genre_id)
        VALUES ({movie_id}, {genre_id});
        """.strip()
        print(sql)

