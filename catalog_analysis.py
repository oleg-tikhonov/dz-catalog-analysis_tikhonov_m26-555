import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

#Этап 1
def average_rating(movies):
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1) 

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie['year'] for movie in movies]
    oldest_movie_age = max(ages)
    newest_movie_age = min(ages)
    avg_age = sum(ages) / len(ages)
    return (oldest_movie_age, newest_movie_age, math.ceil(avg_age))

def duration_in_hours(minutes):
    hours = minutes // 60
    leftover_minutes = minutes % 60 
    return f"{hours}ч {leftover_minutes}м"

#Этап 2

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "cлабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"

 #Этап 3

print("Фильмы (не комедии):")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

print("\nПоиск шедевра")
i = 0
while i < len(movies):
    if movies[i]["rating"] > 9:
        print(f"Найден шедевр: {movies[i]['title']}")
        break
    i += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

#Этап 4

def normalize_title(title):
    words = title.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return " ".join(capitalized_words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres_sorted = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {duration}, жанры: {genres_sorted}'

#Проверка примером
print("\nПроверка 4 этапа")
print(normalize_title("silent hours"))
print(make_slug("Silent Hours"))
print(format_report_line(movies[7]))

