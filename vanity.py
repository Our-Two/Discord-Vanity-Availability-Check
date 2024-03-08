import requests
import os
from dotenv import load_dotenv

load_dotenv()

def req(vanity, headers):
    url = f'https://discord.com/api/v9/invites/{vanity}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    vanity = input("Input Vanity: ")
    custom_headers = {'Authorization': os.getenv("AUTH")}
    response_data = req(vanity, custom_headers)
    if response_data is None:
        print(f'Discord.gg/{vanity} is Available!')
    else:
        if "message" in response_data and response_data["message"] == "Unknown Invite" and response_data["code"] == 10006:
            print(f'Discord.gg/{vanity} is Available!')
        elif "type" in response_data and response_data["type"] == 0:
            print(f'Discord.gg/{vanity} is Taken')
        else:
            print(f"Unknown response: {response_data}")

if __name__ == "__main__":
    main()
