#coding: utf-8

from vagalume import lyrics
import dbus

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")
spotify_properties = dbus.Interface(spotify_bus,
                                    "org.freedesktop.DBus.Properties")
metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

# To just print the title
song_name = metadata['xesam:title']       # recovering song name
artist_name = metadata['xesam:artist'][0]   # recovering artist name

result = lyrics.find(artist_name, song_name)

if result.is_not_found():
    print 'Song not sound'
else:
    print 'Song title:', result.song.name
    print 'Song artist:', result.artist.name
    print
    print result.song.lyric
    print