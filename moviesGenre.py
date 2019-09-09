from pprint import pprint
from allMoviedetails import movieData

def genre(data):
        global genre
        genre = []
        for index in data:
                genre.extend(index["genre"])
        newGenre = []
        for index1 in genre:
                if index1 not in newGenre:
                        newGenre.append(index1)
        return newGenre
newGenre  = genre(movieData)

def analyse_movies_genres(genreData):
        genreCount = {}
        for index2 in genreData:
                count = 0
                for index3 in genre:
                        if index2 == index3:
                                count = count+1
                        genreCount[index2] = count
        return genreCount
genreCount = analyse_movies_genres(newGenre)
pprint (genreCount)