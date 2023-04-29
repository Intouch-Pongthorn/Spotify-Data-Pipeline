from requests import get
import json
import pprint
from datetime import datetime,timedelta

def get_auth_header(token):
    return {"Authorization": "Bearer "+token}

def get_artist_info(token,artist_name,limit=1):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query_str = f"?q={artist_name}&type=artist&limit={limit}"
    query_url = url+query_str
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    return json_result

def get_playlist_info(token,playlist_name,limit=5):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query_str = f"?q={playlist_name}&type=playist&limit={limit}"
    query_url = url+query_str
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_top_tracks(token,artist_id,country='TH'):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country={country}"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_recently_played(token,after,limit=50):
    url = "https://api.spotify.com/v1/me/player/recently-played"
    headers = get_auth_header(token)
    query_str = f"?after={after}&limit={limit}"
    query_url = url+query_str
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result


if __name__ == '__main__':
    #import user_token if directly run this file
    from authorize import user_token as token
    previous_date = datetime.today() - timedelta(days=1)
    millisec_timestamp = int(previous_date.timestamp() *1000)
    
    history_list = get_recently_played(token,after=millisec_timestamp,limit=50)
    for history in history_list:
        pprint.pprint(history_list)
    print(token)
