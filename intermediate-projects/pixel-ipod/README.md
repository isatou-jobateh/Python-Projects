# Pixel iPod 🎧

Pixel iPod is a text-based music player I built with Python, inspired by the classic portable music players. I wanted to create something a little different from the usual practice projects while using the Python concepts I had learned.

The program lets users browse a small music library, play and pause songs, skip between tracks, shuffle the collection, view listening history, and manage a playlist. I also created a retro-style terminal display to give it the feel of a small music player.

## 1. What Problem I Wanted to Solve

I wanted to build a small music-player experience that was interactive and fun to use, while giving myself a chance to practice  Python through a project rather than individual exercises.

I was also interested in recreating some of the simple features that made older music players enjoyable, especially being able to move through a music collection and let shuffle choose what to listen to next.

## 2. Who Experiences the Problem and Why It Matters

This project is mainly for people who enjoy music and want a simple way to explore a collection, choose tracks, create a playlist, and look back at what they have listened to.

It is also a learning project for me. I wanted to understand how different parts of a program can work together, from representing individual songs to managing playback state and keeping a record of listening activity.

Although Pixel iPod is not a real audio player yet, it gave me an opportunity to explore how the basic logic behind one could work.

## 3. What I Researched and Which Alternatives I Considered

While building Pixel iPod, I worked with Python classes and objects, lists, methods, randomisation, exception handling, and file handling.

I used separate classes for the music library, individual songs, and playlists. This helped me organise the information and behaviour instead of keeping everything in one long section of code.

For saving data, I used JSON. I learned that Python objects need to be converted into a suitable data structure before they can be stored as JSON, so I added a method to convert song information into a dictionary.

I kept the project text-based rather than starting with a graphical interface or actual audio playback. That allowed me to focus on the underlying logic before considering more advanced features.

Error handling: I had to decide between methods silently printing an error message versus raising an exception and letting the calling code decide what to do. I went with raise inside my methods, paired with try/except around my menu's action dispatch — that way my methods stay honest about reporting problems, and the program never crashes from one bad menu choice.

File paths: My save file kept landing in the wrong folder depending on where I ran the script from. I learned the difference between a script's working directory and its own file location, and switched to building the save path from __file__ so it always saves next to the script itself, regardless of where it's run from.


## 4. Why I Chose This Solution

I chose this approach because I wanted Pixel iPod to be more than a menu with a few options. I wanted the songs, playlists, playback controls, and listening history to work together as parts of one system.

The shuffle feature is one of my favourite parts because it makes the experience less predictable. I like being able to let the program choose a song for me, so I decided to keep that behaviour.

The retro terminal display was another design choice I made to give the project its own identity. I wanted it to feel like a small, nostalgic music player even though it runs in the terminal.

## 5. How I Tested It, What Happened, and Bugs I Fixed

I tested almost everything manually before building the final menu — calling each method directly with print statements to confirm behavior, rather than trusting it worked just because it didn't error.


During development, I encountered a few problems that required me to look at how the code was behaving and make changes.

### Bug 1: Next Track skipped a song

The Next Track option was advancing more than once because the track-navigation method was being called twice. I corrected the menu logic so that choosing Next Track calls the method once, allowing the program to advance by one track per selection.

### Bug 2: The Quit option did not exit the program

The program initially printed a goodbye message but continued displaying the menu. I fixed this by making the Quit option break out of the main loop, so the program can finish when the user chooses to exit.

### Bug 3: Removing a song that wasn't in the library

Trying to remove a song that wasn't present could raise a `ValueError`. I added exception handling to the library's removal method so it displays a message when the song cannot be found instead of allowing that error to interrupt the program.

## Bug 4: File path

My save file kept appearing in the wrong folder. I debugged this with os.getcwd() to see exactly where Python thought it was running from, which showed me the mismatch between my assumed folder and the real one.

## Bug 5: "Now Playing showing twice

My show_now_playing() and a display_screen() border function were both prepending "Now Playing" text, so the screen displayed it twice. I caught this by actually reading the output carefully rather than just checking that it ran.


### Testing the listening history and shuffle

I also checked the listening history and confirmed that it records songs as I use the playback controls. I decided to keep the shuffle behaviour because I enjoy the randomised listening experience it creates.

These problems helped me practise debugging and understand that small mistakes in program logic can change how an entire feature behaves. Fixing them myself was an important part of completing the project.

Once the menu was built, I tested the full save/load cycle by saving my library, manually clearing history and playlists in memory, then loading from the file and confirming the data reappeared — proving the round-trip actually worked, not just that the code ran without errors.


## 6. What I Would Improve or Do Differently Next Time

Listening history currently logs every song change, even consecutive repeats (e.g., if shuffle lands on the same song twice in a row). I'd add a check so history only logs a new entry when the song actually changes from the last one, rather than logging every raw event.

I would build the menu loop earlier in the process, instead of testing every feature manually first and puting the menu on at the end. Having the interactive menu from the start would have made testing feel more like using the actual app.

Input handling is currently strongest around empty-library checks (Next/Previous Track). I'd go back and apply the same try/except discipline more consistently to every method, like remove_song on playlists, rather than just the ones I happened to test first.

I would also consider adding more options for managing playlists, improving input validation, and eventually exploring actual audio playback or a graphical interface.

For now, I am happy with the text-based version because it allowed me to focus on the logic and practise the Python concepts I had learned.

## Technologies Used

* Python
* Object-oriented programming
* Lists and dictionaries
* Methods and class attributes
* `random` module
* Exception handling
* JSON
* File handling
* `os.path` for file paths

## Project Status

**Completed:** Text-based music-player prototype.

Pixel iPod is part of my Python learning portfolio. It represents my effort to apply Python concepts to a creative project, work through bugs, and build something that reflects my own ideas.
