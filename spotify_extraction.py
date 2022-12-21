import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

cid = os.getenv("cid") #Give your Client Id from Spotify API
secret = os.getenv("secret")#Give your Client secret key from Spotify API

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def call_playlist(creator, playlist_id):
    # step1 - create list of features needed

    playlist_features_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
                              "time_signature"]

    playlist_df = pd.DataFrame(columns=playlist_features_list)

    # step2

    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["releasedate"] = track["track"]["album"]["release_date"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["popularity"] = track["track"]["popularity"]
        playlist_features["track_id"] = track["track"]["id"]

        # Get audio features - ex: liveness,danceability, valence etc
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]

        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index=[0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)

    # Step 3

    return playlist_df

