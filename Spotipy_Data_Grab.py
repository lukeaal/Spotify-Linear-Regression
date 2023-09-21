import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv

# client side things
client_id= '5cdf4a70ac434426be81eab32cfcf4de'
client_pass= '7f5b86d4a8664a0eacfe5660f92593f6'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_pass))
# artist Id's of Megan The Stallion, Father John Misty, Foo Fighters
megan, fjMisty, fooFight = '181bsRPaVXVlUKXrxwZfHK', '2kGBy2WHvF0VdZyqiVCkDT','7jy3rLJdDQY21OgRLCZ9sD'

# megan the stallion...
megans = sp.artist_albums(artist_id=megan, country = 'US')
mItems = megans['items']
meganSongIDs = []

# iterate over the albums of the artists or any type, this includes singles and mixtapes
for i in mItems:
   albumID = i['id']
   tracks = sp.album_tracks(album_id=albumID)
   # create a list of the song id's
   for j in range(len(tracks['items'])):
        meganSongIDs.append((tracks['items'][j]['id']))
mfeature = [sp.audio_features(meganSongIDs[id])[0] for id in range(len(meganSongIDs))]  

# fj mist...
fjMistys = sp.artist_albums(artist_id=fjMisty, country = 'US')
fjItems = fjMistys['items']
fjIDs = []

for i in fjItems:
   albumID = i['id']
   tracks = sp.album_tracks(album_id=albumID)
   # create a list of the song id's
   for j in range(len(tracks['items'])):
        fjIDs.append((tracks['items'][j]['id']))
fjfeature = [sp.audio_features(fjIDs[id])[0] for id in range(len(fjIDs))] 

# foo fighters...
foos = sp.artist_albums(artist_id=fooFight, country = 'US')
fooItems = foos['items']
fooIDs = []

for i in fooItems:
   albumID = i['id']
   tracks = sp.album_tracks(album_id=albumID)
   # create a list of the song id's
   for j in range(len(tracks['items'])):
        fooIDs.append((tracks['items'][j]['id']))
foofeature = [sp.audio_features(fooIDs[id])[0] for id in range(len(fooIDs))]





# change the dictionaries, add the populatry index, and write them to csv files for all the artisist
feats = [mfeature,fjfeature,foofeature]
artIds = [lizzoSongIDs,fjIDs,fooIDs]
# remove non continuous numerical data
indez = 0
for art in feats:
    for idx, song in enumerate(art,0):
        song.pop('type')
        song.pop('id')
        song.pop('uri')
        song.pop('mode')
        song.pop('key')
        song.pop('track_href')
        song.pop('analysis_url')
        song.pop('time_signature')
        song['popularity'] = sp.track(artIds[indez][idx])['popularity']
    indez += 1
# turn list of dictionaries into csv files, three, one for each artist

keys = mfeature[0].keys()

# write to csv file
with open('MeganTheStallion.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(mfeature)

with open('FatherJohnMisty.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(fjfeature)

with open('FooFighters.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(foofeature)