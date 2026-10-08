def make_album(artist_name, album_title):
    album = {"name":artist_name,
             "title":album_title
             }
    return album

while True:
  print("Enter the artist name and title , type 'quit' to stop the program")

  artistName =input("Enter the artist name : ")
  if artistName.lower() == 'quit':
     break
  
  album_title =input("Enter the album title : ")
  if album_title.lower() == 'quit':
       break

  result = make_album(artistName,album_title)
  print(result)  