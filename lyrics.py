#coding: utf-8

from vagalume import lyrics
import dbus

def spotify_info():
    try:
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                        "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

        return metadata
    except:
        print 'Spotify is not open right now, try opening it!'
        exit()

def recover_data(metadata):
    try:
        song_name = metadata['xesam:title']       # recovering song name
        artist_name = metadata['xesam:artist'][0]   # recovering artist name

        return artist_name, song_name
    except:
        print 'There is no song playing right now'
        exit()

def recover():
    artist, song = recover_data(spotify_info())
    result = lyrics.find(artist, song)
    
    if result.is_not_found():
        print 'Song not found'
    else:
        print 'Song title:', result.song.name
        print 'Song artist:', result.artist.name
        print
        print result.song.lyric
        print

def thread_input():
    thread.start_new_thread(thread_recover())

if __name__ == "__main__":
    while True:
        print 'type \'r\' to reload the lyric of the current playing song'
        print 'CTRL+C or type \'e\' to exit'
        entry = raw_input()

        if entry == 'r':
            recover()
        elif entry == 'e':
            exit()