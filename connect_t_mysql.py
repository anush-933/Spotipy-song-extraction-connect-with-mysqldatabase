import pymysql
from DBcreation import call_playlist

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Anuaids03',
                             db='songextraction_schema')

# create cursor
cursor = connection.cursor()

data = call_playlist("spotify", "37i9dQZF1DX3w2Hr9f5Urj")
print(data)
# creating column list for insertion
cols = "`,`".join([str(i) for i in data.columns.tolist()])
print(cols)
# Insert DataFrame recrds one by one.
for i, row in data.iterrows():
    sql = "INSERT INTO `songs_list` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"
    cursor.execute(sql, tuple(row))
    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()
