from allMoviedetails import*
from pprint import pprint 
from movieDirector import newDirector

director_language = {}
def analyse_language_and_directors(directors,data):
    for index in directors:
        languages = []
        language_count = {}
        for oneMovie in data:
            director = oneMovie["director"]
            if index in director:
                languages.extend(oneMovie["language"])
        allLanguage = []
        for language in languages:
            if language not in allLanguage:
                allLanguage.append(language)
        count = 0
        for movieLanguage in allLanguage:
            for oneLanguage in languages:
                if movieLanguage == oneLanguage:
                    count = count+1
            language_count[movieLanguage] = count
        director_language[index] = language_count
    pprint(director_language)

allDirector = analyse_language_and_directors(newDirector,movieData)