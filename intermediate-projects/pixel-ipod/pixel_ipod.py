## Tiny retro music player
## Music library
import random
import json
import os 
folder_pathway = os.path.dirname(os.path.abspath(__file__))

class MusicLibrary():
    def __init__(self):
        self.songs = []
        self.current_song = None
        self.current_index = 0
        self.is_playing = False
        self.playlists = []
        self.history = []

    def get_history(self):
        return self.history

    def create_playlists(self, name):
        playlists = Playlist(name)
        self.playlists.append(playlists)
        return playlists

    def shuffle(self):
        random.shuffle(self.songs)
        self.current_index = 0
        self.current_song = self.songs[self.current_index]
        self.is_playing = True
        self.history.append(self.current_song)
        
    def play(self):
        if not self.songs:
            raise ValueError("Song not found in the library")
        self.is_playing = True
        self.current_song = self.songs[self.current_index]
        self.history.append(self.current_song)

    def pause(self):
        self.is_playing = False

    def next_track(self):
         if not self.songs:
            raise ValueError("NO song in the music library")
         self.current_index = (self.current_index + 1) % len(self.songs)
         self.current_song = self.songs[self.current_index]
         self.history.append(self.current_song)

    def previous_track(self):
        if not self.songs:
           raise ValueError("No song in the music library")
        self.current_index = (self.current_index - 1) % len(self.songs)
        self.current_song = self.songs[self.current_index]
        self.history.append(self.current_song)

    def add_song(self, song):
       self.songs.append(song)

    def play_song(self , song):
          if song not in self.songs:
             raise ValueError("Song is not in the music library")
          self.current_song = song
          self.history.append(self.current_song)

    def show_now_playing(self):
        if self.current_song is None:
            return "No song is currently playing"
        return str(self.current_song)
    

    def remove_song(self, song):
        try:
           self.songs.remove(song)
        except ValueError:
            print("Song not found in the library")
     

    def get_all_songs(self):
       return self.songs

    def save_to_file(self, filename):
        data = {
            "history" : [song.to_dict() for song in self.history],
            "playlists" : [
                {"name": pl.name, "songs": [song.to_dict() for song in pl.songs]}
                for pl in self.playlists 
            ]
        }
        with open(filename, "w") as f:
          json.dump(data,f)
          print("Library saved! ")

     ## Clears then reloads
    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)

        # Rebuild history
        self.history = [Songs(s["title"], s["artist"] , s["album"] , s["duration"]) for s in data["history"]]

        # Rebuild playlists
        self.playlists = []
        for pl_data in data["playlists"]:
            new_playlist = Playlist(pl_data["name"])
            new_playlist.songs = [Songs(s["title"], s["artist"] , s["album"] , s["duration"]) for s in pl_data["songs"]]
            self.playlists.append(new_playlist)


class Songs():
        def __init__(self, title, artist , album , duration ):
          self.title = title
          self.artist = artist
          self.album = album
          self.duration = duration
        def __str__(self):
            return f"{self.title} by {self.artist} (Album: {self.album}, Duration: {self.duration})"
## JSON can't store a songs object directly , but it can store a plan dict
        def to_dict(self):
            return{
                "title": self.title,
                "artist": self.artist,
                "album": self.album,
                "duration": self.duration       
            }

class Playlist():
    def __init__(self, name):
        self.name = name
        self.songs = []


    def add_song(self, song):
        self.songs.append(song)


    def remove_song(self, song):
        try:
            self.songs.remove(song)
        except ValueError:
           print("Song not found in the playlist")

    def get_all_songs(self):
        return self.songs  
    
def show_intro():
      width = 40 
      intro = "Welcome to the Pixel ipod"
      print("+" + "-" * width + "+")
      print("|" + intro.center(width) + "|")
      print("+" + "-" * width + "+")
show_intro()

def display_screen(title, content):
    width = 70
    controls = "<<       [>]/[||]       >>"
    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("+" + "-" * width + "+")
    print("|" + str(content).center(width) + "|")
    print("+" + "-" * width + "+")
    print("|" + controls.center(width) + "|")
    print("+" + "-" * width + "+")

## Create the library that hold songs
library = MusicLibrary()
##Create songs
song = Songs("Pop it" , "Gunna" ,"N/A" , "2:18")
song1 = Songs("Creepin" , "Metro Boomin" , "N/A" , "3:30")
song2 = Songs("Rich Flex" , "Drake" , "N/A" , "3:16")
song3 = Songs("Super Freaky Girl" , "Nick Mianj" , "N/A" , "2:45")
song4 = Songs("So Good" , "Jhene Aiko" , "Westside Whimsy" , "3:57")
## Add the songs to the library.
library.add_song(song)
library.add_song(song1)
library.add_song(song2)
library.add_song(song3)
library.add_song(song4)
## Get all songs from the library
all_songs = library.get_all_songs()
## My playlist
my_playlist = library.create_playlists("My Playlist")
my_playlist.add_song(song)
my_playlist.add_song(song1)
my_playlist.add_song(song3)

while True:
    print("******* Pixel ipod Menu *******")
    print("1. Play")
    print("2. Pause")
    print("3. Next Track")
    print("4. Previous Track")
    print("5. Shuffle")
    print("6. Show Now Playing")
    print("7. View History")
    print("8. View Playlist")
    print("9. Save Library")
    print("10. Load Library")
    print("11. Quit")

    choice = input("Choose an option: ")
    try:
        if choice == "1":
            library.play()
            print("Play[>]:", library.show_now_playing())
        elif choice == "2":
            library.pause()
            print(f"Music Paused[||]: {library.current_song}")
        elif choice == "3":
            library.next_track()
            print("Next track >>:", library.show_now_playing())
        elif choice == "4":
            library.previous_track()
            print("Previous track <<:", library.show_now_playing())
        elif choice == "5":
            library.shuffle()
            print("After shuffling:" , library.show_now_playing())
        elif choice == "6":
            display_screen("Now Playing" , library.show_now_playing())
        elif choice == "7":
            print("My History: ")
            library.get_history()
            for song in library.get_history():
             print(song)
        elif choice == "8":
            print("Songs in my playlist:") 
            for song in my_playlist.get_all_songs():
               print(song)
        elif  choice == "9":
            library.save_to_file(os.path.join(folder_pathway,"my_library.json"))
        elif choice == "10":
             library.load_from_file(os.path.join(folder_pathway,"my_library.json"))
             print("Library loaded!")
        elif choice == "11":
            print("Goodbye")
            break
        else:
            print("Invaild choice")
    except ValueError as e:
           print("Error:", e)
