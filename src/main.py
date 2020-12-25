import requests

from twitch import twitch_header, client_id, client_secret

r = requests.get("https://id.twitch.tv/oauth2/validate", 
    headers = {"Authorization": f"OAuth {client_secret}"})

print(r)
print(r.json())



exit()

r = requests.get("https://api.twitch.tv/helix/search/channels?query=a_seagull", headers = twitch_header)
print(r)
print(r.json())