def make_album(artist, title, songs=None):
    """Return a dictionary describing an album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


while True:
    print("\nEnter an album's details (enter 'q' at any time to quit).")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)