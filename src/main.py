from authorize import user_token as token
from get import get_recently_played
import pandas as pd
from dotenv import load_dotenv
import format
import os

load_dotenv()

file_location = os.getenv('FILE_LOCATION')

def extract_artists_name(lst:list[dict])->str:
    names:list = []
    for i in lst:
        names.append(i["name"])
    names_one_line = format.concat(names)
    return names_one_line

history_playlist = get_recently_played(token,50)
df = pd.DataFrame(
    {
    "song_name": pd.Series([data["track"]["name"] for data in history_playlist]),
    "album_type": pd.Series([data["track"]["album"]["album_type"] for data in history_playlist]),
    "artist":pd.Series([extract_artists_name(data["track"]["artists"]) for data in history_playlist]),
    "release_date": pd.Series([data["track"]["album"]["release_date"] for data in history_playlist]),
    "duration_minute": pd.Series([format.to_minute(data["track"]["duration_ms"]) for data in history_playlist]),
    "played_at": pd.Series([data["played_at"] for data in history_playlist])
    }
)
df.to_csv(file_location+"history.csv")
print(df)

# for data in history_playlist:
#     for i  in 