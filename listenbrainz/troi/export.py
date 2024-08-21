import spotipy
import requests
from troi.patches.playlist_from_listenbrainz import TransferPlaylistPatch

SOUNDCLOUD_URL='https://api.soundcloud.com'

def export_to_spotify(lb_token, spotify_token, is_public, playlist_mbid=None, jspf=None):
    sp = spotipy.Spotify(auth=spotify_token)
    # TODO: store spotify user ids in external_service_oauth table
    spotify_user_id = sp.current_user()["id"]
    lb_token="68fd28b9-37c2-41e1-97b2-31eda342c8c2"
    playlist_mbid="1247e52e-7831-44fd-83f6-d99fa5b450b9"
    args = {
        "mbid": playlist_mbid,
        "jspf": jspf,
        "read_only_token": lb_token,
        "spotify": {
            "user_id": spotify_user_id,
            "token": spotify_token,
            "is_public": is_public,
            "is_collaborative": False
        },
        "upload": True,
        "echo": False,
        "min_recordings": 1
    }
    patch = TransferPlaylistPatch(args)
    playlist = patch.generate_playlist()
    metadata = playlist.playlists[0].additional_metadata
    return metadata["external_urls"]["spotify"]

def export_to_soundcloud(lb_token, soundcloud_token, is_public, playlist_mbid=None, jspf=None):
    print("export_to_soundcloud")
    soundcloud_user_id = get_current_soundcloud_user(soundcloud_token)["id"]
    print(soundcloud_user_id)
    playlist_mbid="1247e52e-7831-44fd-83f6-d99fa5b450b9"
    args = {
        "mbid": playlist_mbid,
        "jspf": jspf,
        "read_only_token": lb_token,
        "soundcloud": {
            "user_id": soundcloud_user_id,
            "token": soundcloud_token,
            "is_public": is_public,
        },
        "upload": True,
        "echo": False,
        "min_recordings": 1
    }
    patch = TransferPlaylistPatch(args)
    playlist = patch.generate_playlist()

    metadata = playlist.playlists[0].additional_metadata
    return metadata["external_urls"]["soundcloud"]

def get_current_soundcloud_user(access_token):
    url = f"{SOUNDCLOUD_URL}/me"
    headers = {
        'Authorization': f'OAuth {access_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    response = response.json()
    return response