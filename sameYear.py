# import movieDetailes fime for all movies detele. 
from movieDetails import  movieDetaile
from pprint import pprint

def group_by_year(movies):
        yearList = []
        for YearName in movies:
                # print (YearName)
                year = YearName["year"]
                if year not in yearList:
                        yearList.append(year)
                        yearList.sort()
        return (yearList)
yearList = group_by_year(movieDetaile)


def sameYear(yearlist,movies):
        myDic = {}
        index = 0
        while index < len(yearList):
                yearS = yearList[index]
                myList = []
                for movieYear in movies:
                        if yearS == movieYear["year"]:
                                myList.append(movieYear)
                myDic[yearS] = myList
                index = index+1
        return (myDic)
allSame_year = sameYear(yearList,movieDetaile)
pprint(allSame_year)

