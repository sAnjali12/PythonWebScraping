from pprint import pprint
from oneMoviedetails import*
from movieDetails import*
from movieCast import*
import pathlib
import json



def all_movieurls(data):
        movieUrl = []
        for index in data:
                urls  = index["url"]
                allUrl = urls[27:36]
                movieUrl.append(allUrl)
        return movieUrl
movieUrl = all_movieurls(movieDetaile)
# pprint(movieUrl)

def writeData(data,fileName):
    with open(fileName, "w") as writeIt: 
	    writeIt.write(json.dumps(data))
    writeIt.close()

def readData(fileName):
    with open(fileName, "r") as readIt: 
        readJson = json.load(readIt)
    return readJson


def movieurl_data(urls):
    allMovies = []
    for url in urls:
        oneUrl = "https://www.imdb.com/title/"+str(url)+"/"
        fileName = ("allMovies/"+str(url)+".json")
        file = pathlib.Path(fileName)
        if file.exists ():
            readmovieData = readData(fileName)
            allMovies.append(readmovieData)
        else:
            movie = scrape_movie_details(oneUrl)
            cast_data = scrape_movie_cast(oneUrl)
            movie["cast"]=cast_data
            writeData(movie,fileName)
    return allMovies
allMovies = movieurl_data(movieUrl)
# pprint(allMovies)




