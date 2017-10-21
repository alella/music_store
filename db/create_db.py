"""
This script reads data from metadata.json and dumps it into sql database

NOTE:Create a database called musicstore before running this script
----
"""

import MySQLdb
import json
from pprint import pprint
import hashlib

db = MySQLdb.connect(host="localhost",  
                     user="root",  
                     passwd="",
                     db="musicstore")
cur = db.cursor()

# Drop tables
cur.execute("drop table if exists genre")
cur.execute("drop table if exists mood")
cur.execute("drop table if exists track")
cur.execute("drop table if exists album")

# Create tables
cur.execute("create table album(album_id char(32), album_name char(50), artist char(30), year int, art char(80), primary key (album_id))")
cur.execute("create table track(track_id char(32), album_id char(32),track_name char(20), track_no int(3), length char(5), price char(5), primary key (track_id), foreign key (album_id) references album(album_id))")
cur.execute("create table mood(track_id char(32), mood char(50), foreign key (track_id) references track(track_id))")
cur.execute("create table genre(track_id char(32), genre char(50), foreign key (track_id) references track(track_id))")


def mood_insert(track_id, moods):
    mood_fmt = "insert into mood (track_id, mood) values ('{0}','{1}');"
    for mood in moods:
        mood=mood.lower().replace("'",'')
        insert_str = mood_fmt.format(track_id, mood)
        print insert_str
        cur.execute(insert_str)
    
def genre_insert(track_id, genres):
    genre_fmt = "insert into genre (track_id, genre) values ('{0}','{1}');"
    for genre in genres:
        genre=genre.lower().replace("'",'')
        insert_str = genre_fmt.format(track_id, genre)
        print insert_str
        cur.execute(insert_str)
    
def album_insert(**kwargs):
    exists = cur.execute("select * from album where album_id='{0}'".format(kwargs['album_id']))
    if exists:
        return
    album_fmt = "insert into album (album_id, album_name, artist, year, art) values ('{album_id}','{album_name}','{artist}','{year}','{art}');"
    kwargs['album_name']=kwargs['album_name'].replace("'",'')
    insert_str = album_fmt.format(**kwargs)
    print insert_str
    cur.execute(insert_str)
    
def track_insert(**kwargs):
    track_fmt = "insert into track (track_id, album_id, track_name, track_no, length, price) values('{track_id}', '{album_id}', '{track_name}', '{track_no}', '{length}', '{price}');"
    kwargs['track_name']=kwargs['track_name'].replace("'",'')
    insert_str = track_fmt.format(**kwargs)
    print insert_str
    cur.execute(insert_str)
    

with open('metadata.json') as r:
    meta = json.load(r)
    for el in meta:
        print ""
        pprint(el)
        track_id = hashlib.md5(el['track']+el['artist']).hexdigest()
        album_id = hashlib.md5(el['album']+el['artist']).hexdigest()
        print "track_id=", track_id
        print "album_id=", album_id
        album_insert(album_id=album_id,
                     album_name=el['album'],
                     artist=el['artist'],
                     year=el['year'],
                     art=el['art'])
        track_insert(track_id=track_id,
                     album_id=album_id,
                     track_name=el['track'],
                     track_no=el['track_no'],
                     length=el['length'],
                     price=el['price'])
        mood_insert(track_id, el['mood'])
        genre_insert(track_id, el['genre'])
        
        db.commit()
        
print "done!"

