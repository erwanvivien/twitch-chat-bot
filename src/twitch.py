from utils import get_content


# [:-1] trims last \n
client_id, client_secret = get_content("client_id")[:-1], get_content("client_secret")[:-1]

twitch_header = {"client-id": client_id, "Authorization": f"Bearer {client_secret}"}
