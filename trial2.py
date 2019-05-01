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
    #items = results['artists']['items']
    #if len(items) > 0:
    #    return items[0]
    #else:
    #    return None
    return results

def show_recommendations_for_artist(artist):
    albums = []
    results = sp.recommendations(seed_artists = [artist['id']], limit = 3)
    for track in results['tracks']:
        print (track['name'], '-', track['artists'][0]['name'])

def show_related_artists(artist):
    results = []
    albums = []

    name = artist['artists']['items'][0]['name']
    uri = artist['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    results.append(name)
    for related_artist in related['artists'][:3]:
        results.append(related_artist['name'])

        # print out the first three genres
        for idx, genre in enumerate(related_artist['genres'][:3], start = 1):
            results.append('Genre {}: {}'.format(idx, genre))

        top_tracks = sp.artist_top_tracks(related_artist['uri'])
        for idx, track in enumerate(top_tracks['tracks'][:3], start = 1):
            results.append('Song {}: {}'.format(idx, track['name']))

        #tracks = sp.recommendations(seed_artists = [related_artist['id']], limit = 3)
        #for idx, track in enumerate(tracks['tracks'], start = 1):
        #    results.append('Song {}: {}'.format(idx, track['name'] + ' - ' + track['artists'][0]['name']))

    return results

#name = input("Who is the Artist you would like to search for? ")

#artist = get_artist(name)
#if artist:
    #results = show_related_artists(artist)
    #print('Related artists for', results[0])
    #for artist in results[1:]:
        #print(artist)

print()
print()

# Loop
while True:
    # Main Menu
    print("============================")
    print(">>> Welcome to Spotipy! <<<")
    print("----------------------------")
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = sp.search(searchQuery,1,0,"artist")

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


        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = sp.artist_albums(artistID)
        print()
        albumResults = albumResults['items']

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

        # See album art
        while True:
            songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
            if songSelection == "x":
                break

            webbrowser.open(trackArt[int(songSelection)])
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            #sp.start_playback(deviceID, None, trackSelectionList) # added


    if choice == "1":
        break

    # print(json.dumps(trackResults, sort_keys=True, indent=4))
