from pprint import pprint
from oneMoviedetails import*
from movieDetails import*
import pathlib
import json
import random
import time


def writeData(data,fileName):
    with open(fileName, "w") as writeIt: 
	    writeIt.write(json.dumps(data))
    writeIt.close()

def readData(fileName):
    with open(fileName, "r") as readIt: 
        readJson = json.load(readIt)
    return readJson




def movieurl_data(data):
        allMovies = []
        for index in data:
                urls  = index["url"]
                fileName = ("allMovies/"+ urls[27:36]+".json")
                file = pathlib.Path(fileName)
                if file.exists ():
                    readmovieData = readData(fileName)
                    allMovies.append(readmovieData)
                else:
                    movie = scrape_movie_details(oneUrl)
                    writeData(movie,fileName)
                    movietime = random.randint(1,3)
                    time.sleep(movietime)
        return allMovies

movieDetail = movieurl_data(movieDetaile)
pprint(movieDetail)