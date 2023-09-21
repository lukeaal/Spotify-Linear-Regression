import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv

# Client credentials
client_id = '5cdf4a70ac434426be81eab32cfcf4de'
client_pass = '7f5b86d4a8664a0eacfe5660f92593f6'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_pass))

# Artist Id's of Megan The Stallion, Father John Misty, Foo Fighters
megan, fjMisty, fooFight = '181bsRPaVXVlUKXrxwZfHK', '2kGBy2WHvF0VdZyqiVCkDT', '7jy3rLJdDQY21OgRLCZ9sD'

# Get Megan The Stallion's albums
megans = sp.artist_albums(artist_id=megan, country='US')
mItems = megans['items']
meganSongIDs = []

# Iterate over the albums of the artist
for i in mItems:
    albumID = i['id']
    tracks = sp.album_tracks(album_id=albumID)
    # Create a list of the song id's
    for j in range(len(tracks['items'])):
        meganSongIDs.append((tracks['items'][j]['id']))

# Get audio features for Megan The Stallion's songs
mfeature = [sp.audio_features(meganSongIDs[id])[0] for id in range(len(meganSongIDs))]

# Get albums and audio features for Father John Misty
fjMistys = sp.artist_albums(artist_id=fjMisty, country='US')
fjItems = fjMistys['items']
fjIDs = []

for i in fjItems:
    albumID = i['id']
    tracks = sp.album_tracks(album_id=albumID)
    # Create a list of the song id's
    for j in range(len(tracks['items'])):
        fjIDs.append((tracks['items'][j]['id']))

fjfeature = [sp.audio_features(fjIDs[id])[0] for id in range(len(fjIDs))]

# Get albums and audio features for Foo Fighters
foos = sp.artist_albums(artist_id=fooFight, country='US')
fooItems = foos['items']
fooIDs = []

for i in fooItems:
    albumID = i['id']
    tracks = sp.album_tracks(album_id=albumID)
    # Create a list of the song id's
    for j in range(len(tracks['items'])):
        fooIDs.append((tracks['items'][j]['id']))

foofeature = [sp.audio_features(fooIDs[id])[0] for id in range(len(fooIDs))]

# Modify dictionaries, add the 'popularity' index, and write them to CSV files for all the artists
feats = [mfeature, fjfeature, foofeature]
artIds = [meganSongIDs, fjIDs, fooIDs]

# Remove non-continuous numerical data
indez = 0
for art in feats:
    for idx, song in enumerate(art, 0):
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

# Turn list of dictionaries into CSV files, one for each artist
keys = mfeature[0].keys()

# Write to CSV file for Megan The Stallion
with open('MeganTheStallion.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(mfeature)

# Write to CSV file for Father John Misty
with open('FatherJohnMisty.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(fjfeature)

# Write to CSV file for Foo Fighters
with open('FooFighters.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(foofeature)
