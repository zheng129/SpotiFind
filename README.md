# SpotiFind

For the CPSC 353 Class project

### Team Members:
[Ali Ahmadnejad](https://github.com/aliahmadnejad)

[Johnny Chapman](https://github.com/johnnycchapman)

#### Setup:
* Open terminal and install Spotipy using "pip install spotipy command"
* If pip is not installed, install pip by downloading the get-pip.py file from: https://bootstrap.pypa.io/get-pip.py
* Then run: "python get-pip.py" in the terminal
* To verify if Pip was installed correctly type "pip -V"

#### Runing the program:

* Go to the directory that the file is stored
* `python related_artists_genres_sub3.py [artist_name]` insert artist name as argument
* Note that the spelling of the artist is critical, might need space/dot in between words

* example: 
  - `python related_artists_genres_sub3.py micheal jackson` returns correct result
  - `python related_artists_genres_sub3.py michealjackson` returns `Can't find that artist michealjackson`
