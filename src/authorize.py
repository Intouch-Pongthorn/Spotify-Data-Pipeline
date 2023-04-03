from dotenv import load_dotenv
import spotipy.util as util
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
username = os.getenv("USERNAME")
scope = "user-read-recently-played"

user_token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)

if __name__ == "__main__":
    print(user_token)

