def make_album(artist_name, album_title,songs = None):
    if songs is not None:
        album = {
            "name": artist_name,
            "title": album_title,
            "songs": songs
        }
    else:
        album =  {
            "name": artist_name,
            "title": album_title,

        }

    return album

prompt = "Enter an artist name and title , you can add the number of songs if you want to \n"
prompt+= "type 'quit' to stop the program\n"

active =True

while active:

 message = input(prompt) 

if message.lower() == 'quit':
 active = False

else:
   print( make_album(message)
)
