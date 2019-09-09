from pprint import pprint
from allMoviedetails import movieData

def language(data):
        global language
        language = []
        for index in data:
                language.extend(index["language"])
        newLanguage = []
        for index1 in language:
                if index1 not in newLanguage:
                        newLanguage.append(index1)
        return newLanguage
newLanguage = language(movieData)


def analyse_movies_language(languageData):
        languageCount = {}
        for index2 in languageData:
                count = 0
                for index3 in language:
                        if index2 == index3:
                                count = count+1
                        languageCount[index2] = count
        return languageCount
languageCount = analyse_movies_language(newLanguage)
pprint(languageCount)