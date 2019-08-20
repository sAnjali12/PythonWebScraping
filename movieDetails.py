import requests
from pprint import pprint
from bs4 import BeautifulSoup
URL = " https://www.imdb.com/india/top-rated-indian-movies/"
getData = requests.get(URL).text
soup = BeautifulSoup(getData,"html.parser") # iss object ke throw hum kahi bhi khel sakte hai
movielist = []
title = soup.find("tbody",class_ = "lister-list")
trs = title.findAll("tr")
def scrape_top_list(trs):
        for name in  trs:
                movieData = {}
                movieName = name.find("td",class_ = "titleColumn").a.get_text()
                year = name.find("span",class_ = "secondaryInfo").get_text()
                rating = name.find("td",class_ = "ratingColumn imdbRating").strong.get_text()
                url  = name.find("a")
                movieUrl = "https://www.imdb.com"+url["href"]
                movieData["name"] = movieName
                movieData["year"] = int(year[1:5])
                movieData["Rating"]= float(rating)
                movieData["url"]=movieUrl
                movielist.append((movieData))
        return (movielist)
movieDetaile = scrape_top_list(trs)
# pprint (movieDetaile)