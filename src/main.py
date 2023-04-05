from authorize import user_token as token
from get import get_recently_played
import pandas as pd
from dotenv import load_dotenv
import format
import os

load_dotenv()

file_location = os.getenv('FILE_LOCATION')

history_playlist = get_recently_played(token,50)
df = pd.DataFrame(
    {
    "song_name": pd.Series([data["track"]["album"]["name"] for data in history_playlist]),
    "song_id": pd.Series([data["track"]["album"]["id"] for data in history_playlist]),
    "album_type": pd.Series([data["track"]["album"]["album_type"] for data in history_playlist]),
    "release_date": pd.Series([data["track"]["album"]["release_date"] for data in history_playlist]),
    "duration_ms": pd.Series([format.to_minute(data["track"]["duration_ms"]) for data in history_playlist]),
    "played_at": pd.Series([data["played_at"] for data in history_playlist])
    }
)
df.to_csv(file_location+"history.csv")
print(df)
