from authorize import user_token
from get import get_recently_played
import pandas as pd
from dotenv import load_dotenv
import format
import os
from datetime import datetime,timedelta

load_dotenv()
file_location = os.getenv('FILE_LOCATION')
previous_date = datetime.today() - timedelta(days=1)
millisec_timestamp = int(previous_date.timestamp() *1000)
history_playlist = get_recently_played(user_token,after=millisec_timestamp,limit=50)
df = pd.DataFrame(
    {
    "song_name": pd.Series([data["track"]["name"] for data in history_playlist]),
    "album_type": pd.Series([data["track"]["album"]["album_type"] for data in history_playlist]),
    "artist":pd.Series([format.extract_artists_name(data["track"]["artists"]) for data in history_playlist]),
    "release_date": pd.Series([data["track"]["album"]["release_date"] for data in history_playlist]),
    "duration_minute": pd.Series([format.to_duration_minute(data["track"]["duration_ms"]) for data in history_playlist]),
    "played_at": pd.to_datetime(pd.Series([format.to_th_time(data["played_at"]) for data in history_playlist])),
    }
)
df.to_csv(file_location+"history.csv")
print(df)
