import requests

def client_credentials(path_to_credentials): 
    """
    Returns the access token for the Spotify API.
    """
    # Open the file and read the credentials
    with open(path_to_credentials, 'r') as file:
        CLIENT_ID = file.readline().strip()  # Read the first line and remove any trailing newline
        CLIENT_SECRET = file.readline().strip()  # Read the second line and remove any trailing newline

    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=data, headers=headers)

    #Save the acces token
    access_token = response.json().get('access_token')

    return access_token

def followers(artist_id, access_token):
    """
    Returns the total number of followers for a given artist.
    """

    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    followers = response.json().get('followers').get('total')
    artist_name = response.json().get('name')

    print(f"{artist_name} has {followers} followers.")

def top_items(access_token, type="tracks", time_range="short_term", limit=10):
    """
    Returns the top items of yourself.
    For type, you can choose between 'tracks' and 'artists'.
    For time_range, you can choose between 'short_term', 'medium_term', and 'long_term'.
    Limit is the number of items you want to retrieve.
    """
    
    url = f"https://api.spotify.com/v1/me/top/{type}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    print(response.json())

    
