def song_decoder(song):
    song = song.split("WUB")
    return " ".join(i for i in song if i!="")
