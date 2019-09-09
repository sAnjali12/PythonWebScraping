from pprint import pprint
from allMoviedetails import movieData

def director(data):
        global director
        director = []
        for index in data:
                director.extend(index["director"])
        newDirector = []
        for index1 in director:
                if index1 not in newDirector:
                        newDirector.append(index1)
        return newDirector
newDirector  = director(movieData)

def analyse_movies_directors(directorData):
        directorCount = {}
        for index2 in newDirector:
                count = 0
                for index3 in director:
                        if index2 == index3:
                                count = count+1
                        directorCount[index2] = count
        return directorCount
directorCount = analyse_movies_directors(newDirector)
# pprint (directorCount)