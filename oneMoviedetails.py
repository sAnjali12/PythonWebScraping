import requests
from bs4 import BeautifulSoup
from movieCast import*
from pprint import pprint

# url = ("https://www.imdb.com/title/tt0367495/")
def responceData(url1):
        responce = requests.get(url1)
        soup_data = BeautifulSoup(responce.text, "html.parser")
        return soup_data
# soup = responceData(url)

def movieName(data):
        div = data.find("div",class_= "title_wrapper").h1.get_text()
        name = div.split()
        movieName = ("").join(name[:-1])
        return movieName

def posterImage(data):
        try:
                div = data.find("div",class_="poster")
                image = div.img["src"]
                return image
        except AttributeError:
                print("---------")


# divBio = soup.find("div",class_="plot_summary")
def movieBio(data):
        divBio = data.find("div",class_="plot_summary")
        movieBio = divBio.find("div",class_="summary_text").get_text()
        summaryText = movieBio.strip("\n ")
        return summaryText


def moveiDirector(data):
        divBio = data.find("div",class_="plot_summary")
        divDirector = divBio.find("div",class_="credit_summary_item")
        directorData = divDirector.find_all("a")
        directorName = []
        for divIndex in directorData:
                movieDirector = divIndex.get_text()
                directorName.append(movieDirector)
        return directorName



def movietime(data):
        divRuntime = data.find("div",class_="subtext").time["datetime"]
        movieRuntime = divRuntime[2:5]
        runTime = (movieRuntime)
        return runTime


def movieGenre(data):
        divGenre =  data.find("div",class_="subtext")
        genreData = divGenre.find_all("a")
        genreName = []
        for genreIndex in genreData:
                movieGenre = genreIndex.get_text()
                genreName.append(movieGenre)
        genre = genreName[0:2]
        return genre


def movieLanguage(data):
        divArticle = data.find("div",class_="article",id="titleDetails")
        divCountry = divArticle.find_all("div",class_="txt-block")
        for index in divCountry:
                if "Country" in index.text:
                        global country
                        country = index.a.get_text()
                if "Language" in index.text:
                        language = index.find_all("a")
                        movieLanguage = []
                        for languageIndex in language:
                                languageData = languageIndex.get_text()
                                movieLanguage.append(languageData)
                        return movieLanguage

        

def scrape_movie_details(moviUrl):
        soup = responceData(moviUrl)
        name = movieName(soup)
        image = posterImage(soup)
        bio = movieBio(soup)
        director = moveiDirector(soup)
        runtime = movietime(soup)
        genre = movieGenre(soup)
        language = movieLanguage(soup)

        movieDetails = {}
        movieDetails["name"] = name
        movieDetails["country"] = country
        movieDetails["director"] = director
        movieDetails["language"] = language
        movieDetails["poster_image_url"] = image
        movieDetails["runtime"] = runtime
        movieDetails["bio"] = bio
        movieDetails["genre"] = genre
        return movieDetails
url = ("https://www.imdb.com/title/tt0367495/")
movie = scrape_movie_details(url)
# pprint(movie)
