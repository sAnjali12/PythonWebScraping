from task8 import allMovies
from pprint import pprint


total_data = {}
def  analyse_actors(movie_data):
    duplicate_name_data = []
    for data in movie_data:
        cast = data["cast"]
        for index in cast:
                names = index["name"]
                ids = index["imdb_id"]
                duplicate_name_data.append(names)
        particular_name = []
        for index2 in duplicate_name_data:
                if index2 not in particular_name:
                    particular_name.append(index2)
        
        actors_name = {}
        for name_data in particular_name:
                actors = name_data
                count = 0
                for duplicate_name in duplicate_name_data:
                    if actors == duplicate_name:
                        count = count+1
                actors_name["num_movie"] = count
                actors_name["name"] = actors
                
                total_data[ids] = actors_name
    pprint(total_data)
analyse_actors(allMovies)            
        
