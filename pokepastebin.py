
import requests
from requests import get
from sys import argv as cmd_line_param

def main():
    poke_name = cmd_line_param[1]
    dict = get_user_info(poke_name)
    if dict:
        user_strings = get_user_strings(dict)
        pastebin_url = post_to_pastebin(user_strings[0], user_strings[1])
        print(pastebin_url)

def get_user_info(poke_name):
    print("getting poke info- ", end='')
    poke_url = 'https://pokeapi.co/api/v2/pokemon/' 
    response = requests.get(poke_url + str(poke_name))
     

    if response.status_code == 200:
        print('success')
        return response.json()
    else:
        print('fail to get info',response.status_code)
        return None

def get_user_strings(user_dict):
    title = user_dict['name'] + " Pokemon abiltites"
    body_text = "Abilties:" + user_dict['abilities'][0]['ability']['name'] + "\n"
    body_text += "Abilties: " + user_dict['abilities'][1]['ability']['name']
    return (title, body_text)

def post_to_pastebin(title, body_text):
    print("Posting to PasteBin...", end='')

    params = {
       'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
       'api_option': 'paste',
       'api_paste_code': body_text,
       'api_paste_name': title
    }
    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, data=params)

    if response.status_code == 200:
        print('success')
        return response.text # Converts response body to a string
    else:
        print('failed. Response code:', response.status_code)
        return response.status_code
 
main()
    