import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
import collections
import queue
import random

scope = 'user-library-read'
client_id = "91f224b0e56d405cb6c2c10bb9961405"
client_secret = "2c0ec20e82774410be39c1862bf6c821"
redirect_uri = "http://www.google.com/"

#Get the username from the terminal
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')

    return results

def show_related_artists(artist):
    results = []
    albums = []

    name = artist['artists']['items'][0]['name']
    uri = artist['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    results.append(name)
    for related_artist in related['artists'][:50]:
        results.append(related_artist['name'])


    return results

# Loop
while True:
    # Main Menu
    print("============================")
    print(">>> Welcome to SpotiFind! <<<")
    print("============================")
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        name = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = sp.search(name,1,0,"artist")

        # Artist details
        print("================")
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print("================")
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print("----------------")
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        print()
        print()

        # Print related artists
        artist = get_artist(name)
        if artist:
            results = show_related_artists(artist)
            print("=================================================")
            print('Related artists for:', results[0], "\n=================================================")
            for artist in results[1:]:
                print(artist)

        print("-------------------------------------------------")
        print()

        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = sp.artist_albums(artistID)
        print()
        albumResults = albumResults['items']

        # Print out by albums
        for item in albumResults:
            print("=================================================")
            print("ALBUM: " + item['name'])
            print("=================================================")
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = sp.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print("-------------------------------------------------")
            print()
            print()

        # Open album art
        while True:
            songSelection = input("Enter a song number to see album art or press 'x' to exit): ")
            if songSelection == "x":
                break

            webbrowser.open(trackArt[int(songSelection)])
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])


    # Exit SpotiFind
    if choice == "1":
        break

