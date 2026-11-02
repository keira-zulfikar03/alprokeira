def make_album(artist, title, songs=None):
    """Return a dictionary describing an album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


print(make_album('queen', 'a night at the opera'))
print(make_album('adele', '21'))
print(make_album('coldplay', 'parachutes', songs=10))