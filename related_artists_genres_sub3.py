import sys
import spotipy
import pprint

''' shows recommendations for the given artist
'''

from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='6c4376a0c26b47509b76f2a2d64c49f8', client_secret='0d2f67fc349241a28b2451aa71c86455')
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

if __name__ == '__main__':
    artists_names_short = ['R.E.M',
                     'Guns N\' Roses']
    artists_names = ['Herbie Hancock',
                     'Hoobastank',
                     'Howlin Wolf',
                     'Hoyt Axton',
                     'Huey Lewis & The News',
                     'The Human LeagueHumble Pie',
                     '2Pac',
                     '50 Cent',
                     'ABC',
                     'Agnetha Fältskog',
                     'Alan Jackson',
                     'Albert King',
                     'Alice Cooper',
                     'Alison Krauss',
                     'The All-American Rejects',
                     'The Allman Brothers Band',
                     'Heart',
                     'Gong',
                     'Guns N\' Roses',
                     'Gregory Isaacs',
                     'Graham Parker',
                     'Anthrax',
                     'Humble Pie',
                     'Arcade Fire',
                     'INXS',
                     'Ice Cube',
                     'Poco',
                     'Poison',
                     'The Police',
                     'Paul Simon',
                     'Paul Weller',
                     'Pearl Jam',
                     'Peggy Lee',
                     'Phil Collins',
                     'Pink Floyd',
                     'Placebo',
                     'Prince',
                     'Pulp',
                     'Queen',
                     'Iggy Pop',
                     'Imagin Dragons',
                     'Iron Maiden',
                     'Aswad',
                     'The Band',
                     'Jack Johnson',
                     'Jack Bruce',
                     'Beck',
                     'Redman',
                     'R.E.M',
                     'James Taylor',
                     'Rick Nelson']
    if len(sys.argv) < 2:
        print((('Usage: {0} artist name'.format(sys.argv[0]))))
    else:
        name = ' '.join(sys.argv[1:])
        try:
            artist = get_artist(name)
            if artist:
                results = show_related_artists(artist)
                print('Related artists for', results[0])
                for artist in results[1:]:
                    print(artist)
                print()
        except:
            print ("Can't find that artist", name)
            
    
    #for name in artists_names_short:
    #    artist = get_artist(name)
    #   if artist:
    #        results = show_related_artists(artist)
    #        print('Related artists for', results[0])
    #        for artist in results[1:]:
    #            print(artist)
    #        print()
    #    else:
    #        print ("Can't find that artist", name)
