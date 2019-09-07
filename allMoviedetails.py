from oneMoviedetails import*
from movieDetails import*
from pprint import pprint

def get_movie_list_details(data):
        onemovie = []
        for index in data:
                urls  = index["url"]
                movie = scrape_movie_details(urls)
                onemovie.append(movie)
        return onemovie
movieData = get_movie_list_details(movieDetaile)
# pprint(movieData)