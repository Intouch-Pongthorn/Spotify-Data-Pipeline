from authorize import user_token as token
from get import get_recently_played
import pandas as pd

history_playlist = get_recently_played(token,1680536134)
print(history_playlist)
