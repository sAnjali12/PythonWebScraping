# import movieDetailes fime for all movies detele. 
from movieDetails import  movieDetaile
from pprint import pprint

def group_by_year(movies):
        years = []
        for YearName in movies:
                # print (YearName)
                year = YearName["year"]
                if year not in years:
                        years.append(year)
                        years.sort()
        return (years)
years = group_by_year(movieDetaile)
# pprint(years)


def sameYear(years,movies):
        allYear = {}
        index = 0
        while index < len(years):
                sameYear = years[index]
                movieYear = []
                for moviesYear in movies:
                        if sameYear == moviesYear["year"]:
                                movieYear.append(moviesYear)
                allYear[sameYear] = movieYear
                index = index+1
        return (allYear)
allSame_year = sameYear(years,movieDetaile)
# pprint (allSame_year)

