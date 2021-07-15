import spotipy
import spotipy.util as util

src = ''
dst = ''

username = ''
client_id = ''
client_secret = ''
redirect_uri = 'http://localhost:8000/'

removeFromDst = True;

def auth():
    scope = 'playlist-modify-private playlist-read-private'

    token = util.prompt_for_user_token(
                            username,
                            scope,
                            client_id = client_id,
                            client_secret= client_secret,
                            redirect_uri = redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        print('Authenticated')
        return sp
    else:
        print("Failed to get token")

sp = auth()


def getTracksForPlst(uri):
    playlist = sp.playlist_tracks(uri)
    allTracks = playlist['items']
    while playlist['next']:
        playlist = sp.next(playlist)
        allTracks.extend(playlist['items'])
    tracks = []
    for t in allTracks:
        tracks.append(t['track']['uri'])
    
    return tracks


srcTracks = getTracksForPlst(src)

dstTracks = getTracksForPlst(dst)

diffSrcDst = list(set(srcTracks) - set(dstTracks))
diffDstSrc = list(set(dstTracks) - set(srcTracks))

if diffSrcDst:
    sp.playlist_add_items(dst, diffSrcDst)

if diffDstSrc and removeFromDst:
    sp.playlist_remove_all_occurrences_of_items(dst, diffDstSrc)

print(f"Added {len(diffSrcDst)}, removed {len(diffDstSrc)}")