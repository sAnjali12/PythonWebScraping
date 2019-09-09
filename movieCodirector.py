from task8 import allMovies
from pprint import pprint
names = []
all_names = []

def co_actors(moviData):
    for index in moviData:
        a = index["cast"][:5]
        all_names.append(a)
    return all_names
all_names = co_actors(allMovies)
# pprint (all_names)

def lead_actor(one_name):
    for allData in one_name:
        for name in allData[:1]:
            actor_name = name["name"]
            if actor_name not in names:
                names.append(actor_name)
    return names
actor_names = lead_actor(all_names)


movie_all_data = []
def particular_actor(name_data,actor_name):
    for actor in actor_names:
        movie_actors = []
        for all_actor in name_data:
            if actor in all_actor[0]["name"]:
                movie_actors.append(all_actor)
        movie_all_data.append(movie_actors)
    return movie_all_data
movie_all_data = particular_actor(all_names,actor_names)
# pprint(movie_all_data)

def analyse_co_actors(data,name_data):
    all_movie_datas = {}
    for co_actors_name in name_data:
        for main_name in data:
            movie_count = {}
            all_name = main_name[0][0]["name"]
            all_id  = main_name[0][0]["imdb_id"]
            co_actors_duplicate = []
            co_actor_list = []
            without_duplicate_co_actor = []
            for co_actor in main_name:
                for particular_actor in co_actor[1:]:
                    co_actors_duplicate.append(particular_actor["name"])
                    if particular_actor not in without_duplicate_co_actor:
                        co_actor_list.append(particular_actor)
                        without_duplicate_co_actor.append(particular_actor["name"])
            frequent_co_actors = []
            # pprint (without_duplicate_co_actor)
            for movie_actor in without_duplicate_co_actor:

                count = 0
                for duplicate_name in co_actors_duplicate:
                    if movie_actor == duplicate_name:
                        count = count+1
                if count>1:
                    for index1 in co_actor_list:
                        if index1 not in frequent_co_actors:
                            # pprint (movie_actor)
                            if index1["name"] == movie_actor:
                                index1["num_movies"] = count

                                frequent_co_actors.append(index1)
                    # pprint (frequent_co_actors)
                if frequent_co_actors != []:
                    movie_count["name"] = all_name
                    movie_count["frequent_co_actor"] = frequent_co_actors
                    all_movie_datas[all_id] = movie_count
    return all_movie_datas  
a = analyse_co_actors(movie_all_data,actor_names)
# pprint(a)