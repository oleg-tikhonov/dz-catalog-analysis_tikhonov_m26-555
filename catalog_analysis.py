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
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {duration}, жанры: {genres_sorted}' # noqa: E501

#Проверка примером
print("\nПроверка 4 этапа")
print(normalize_title("silent hours"))
print(make_slug("Silent Hours"))
print(format_report_line(movies[7]))

#Этап 5

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

#Проверка примером 
print("\nПроверка 5 этапа")
print(top_n_by_rating(movies, 3))

#Этап 6

def count_by_genre(movies):
    genre_count = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, []) + [movie["title"]]
    return filmography

avg_rating = average_rating(movies)
high_rated_movies = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > avg_rating
}

#Проверка примером
print("\nПроверка 6 этапа")
print(count_by_genre(movies))

#Этап 7

def all_genres(movies):
    unique_genres = set()
    for movie in movies:
        unique_genres.update(movie["genres"])
    return unique_genres

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)

#Проверка примером
print("\nПроверка 7 этапа")
print(common_actors(movies[0], movies[3]))
print(genres_only_in_one(movies[5:6], movies[:5]))

#Этап 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] > min_rating:
            yield movie

#Демонстрация генератора циклом for c выводом 
print("\nВысокооцененные фильмы:")
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

#Генераторное выражение внутри sum()
total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)

#Этап 9 - ОТЧЁТ ПО КАТАЛОГУ

def build_report(movies):
    print("\nОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет\n")
    print("Топ-3 фильма:")
    top_3_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)[:3]
    for movie in top_3_movies:
        print(f"{format_report_line(movie)}")
    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    for genre, count in sorted_genres:
        print(f"{genre} - {count}")
    all_unique = sorted(all_genres(movies))
    print("\nВсе жанры каталога:", ", ".join(all_unique))

if __name__ == "__main__":
    build_report(movies)

    
