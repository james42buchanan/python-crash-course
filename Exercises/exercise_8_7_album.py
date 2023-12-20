def make_album(artist_name, album_name):
    '''Returns dictionary containing artist name and album name.
    '''
    
    album = {
        'artist_name': artist_name.title(),
        'album_name': album_name.title()
    }

    return album


# print(make_album('hovvdy', 'true love', 10))
# print(make_album('jeff buckley', 'grace'))
# print(make_album('aphex twin', 'selected ambient works 85-92'))


while True:
    print('\nEnter "quit" to exit the program.')
    print('Please enter the name of an artist and the name of one of their albums: \n')
    albums = dict()


    artist_name = input('Please enter the name of an artist: ')
    if artist_name.lower() == 'quit':
        break

    album_name = input('Please enter the name of an album: ')
    if album_name.lower() == 'quit':
        break

    albums.update(make_album(artist_name, album_name))
    print(albums)

