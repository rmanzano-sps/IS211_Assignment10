DROP DATABASE IF EXISTS music;

create database if not exists music;

use music;

CREATE TABLE IF NOT EXISTS artist (
  artist_id INTEGER PRIMARY KEY,
  artist_name TEXT
);

CREATE TABLE IF NOT EXISTS album (
  album_id integer PRIMARY KEY,
  album_title text,
  artist_id integer,
  FOREIGN KEY (artist_id) REFERENCES artist (artist_id)
);

CREATE TABLE IF NOT EXISTS song (
  track_id integer PRIMARY KEY,
  song_name text,
  song_length text,
  album_id integer,
  FOREIGN KEY (album_id) REFERENCES album (album_id)
);
