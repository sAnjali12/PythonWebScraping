from pprint import pprint
from sameYear import*
from movieDetails import movieDetaile

def yearDecade(years,movies):
        decades = []
        for year in years:
                yearModual = year%10
                decade = year-yearModual
                if decade not in decades:
                        decades.append(decade)
        return decades
allDecades = yearDecade(years,movieDetaile)
# pprint (allDecades)

def group_by_decade(list1):
        for index in allDecades:
                oneYear = index
                allYear = oneYear+10
                allDecade = {}
                allDecadeyear = []
                for index1 in range(oneYear,allYear):
                        if index1 in years:
                                allDecadeyear.extend(allSame_year[index1])
                allDecade[oneYear] = allDecadeyear
                        
                pprint (allDecade)
group_by_decade(allDecades)
