import os
import pymysql
from spotify_extraction import call_playlist
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("password") #give your Mysql password

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password=password,
                             db='songextraction_schema') #database name

# create cursor
cursor = connection.cursor()

#give a playlist's URI part as input
data = call_playlist("spotify", "37i9dQZF1DX3w2Hr9f5Urj")

# creating column list for insertion
cols = "`,`".join([str(i) for i in data.columns.tolist()])

# Insert DataFrame records one by one.
for i, row in data.iterrows():
    sql = "INSERT INTO `songs_list` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)" #song_list is the table name od the database
    cursor.execute(sql, tuple(row))
    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()
