def city_country(city_name , country_name):
    city = f"{city_name}, {country_name}"
    return city.title()


city1 = city_country ("accra", "ghana")
city2= city_country ("tamale", "ghana")
city3 = city_country ("kumasi", "ghana")

print(city1)
print(city2)
print(city3)

print(" ")

print("This is a music album\n")

def make_album(artist_name, album_title, songs = None):
    if songs is not None:
     album = {"name":artist_name,
             "title":album_title,
             "songs":songs
             }
    else:
       album =  {"name":artist_name,
                    "title":album_title
                    }
      
    return album

album1 = make_album("shatta wale","The crown")
album2 = make_album("Kwesi author","son of  Job")
album3 = make_album("Black Sherif","The vallian I never was",30)

print(album1)
print(album2)
print(album3)
