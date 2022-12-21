# Connecting Spotify API and MySQL workbench
This repo consist of 2 python files describing on how to extract songs from SpotipyAPI and store these in MySQL Database.
This is part of my project. Hope this is useful for the spotify begginer devlopers.


# About SpotifyAPI
Based on simple REST principles, the Spotify Web API endpoints return JSON metadata about music artists, albums, and tracks, directly from the Spotify Data Catalogue.

For more : https://developer.spotify.com/documentation/web-api/

<ins>*1. STEPS TO  CREATE PROJECT VIA SPOTFY API*<ins>
  
      Step 1: Go to https://developer.spotify.com/dashboard/login and login
      Step 2: Click create an app and give a title
      Step 3: A Client ID and Secret Key will be provided and save them for later.

<ins>*2. STEPS TO EXTRACT SONGS VIA SPOTIFY WEB API (Ref spotify_extraction.py)*<ins>
      
      Step 1: Install spotipy package.
      Step 2: Using SpotifyClientCredentials(), enter your client id and secret key.
      Step 3: In user defined function 'call_playlist()', pass 2 arguments (spotify-creator and playlist URI)
      Step 4: Using user_playlist_tracks() and audio_features() functions, extract the playlist's information and return as concatenated dataframes
      Step 5: return the final dataframe 
      
<ins>*3. STEPS TO DOWNLOAD IN MySQL WORKBENCH*<ins>

If Mysql workbench not installed, follow the steps https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation

<ins>*4. STEPS TO CREATE SCHEMA AND TABLE*<ins>

     Step 1: Click 'New Connection + '. Give new connection name and click enter.
     Step 2: In Tables, create new table (in my rep the table name is 'songs_list').
     Step 3: Right CLick on the table and click 'Alter Table' and create columns and datatype.
     
<p align="center">
  <img width="300" height="400" src="https://user-images.githubusercontent.com/82230179/208829184-f76cdef7-a256-434d-b131-69993dba2575.png">
</p>

<ins>*5. CONNECT PYTHON AND MySQL (Ref connect_t_mysql.py)*<ins>
     
     Step 1: Install pymysql using !pip install pymysql
     Step 2: Connect to the database created by using pymysql.connect().
     Step 3: Import the above spotify_extraction,py as a module.
     Step 4: Create column list for insertion of each records to table from dataframe.
     Step 4: The Sql query 'INSERT' is used and executed.
     Step 5: Save the changes and commit().
     
  <ins>**OUTPUT**<ins>
  
  [output.csv](https://github.com/anush-933/Spotipy-song-extraction-connect-with-mysqldatabase/files/10274842/output.csv)
