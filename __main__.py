import requests
from utils import client_credentials, followers, top_items

my_credentials_path = "credentials.txt"

access_token = client_credentials(path_to_credentials=my_credentials_path)

headers = {
    "Authorization": f"Bearer {access_token}"
}
# The artist you want to query
id = "2sSGPbdZJkaSE2AbcGOACx?si=ALRGQwNaRciaTTYF_mob9w" #The Marias


followers(artist_id=id, access_token=access_token)

# top_items(access_token=access_token)