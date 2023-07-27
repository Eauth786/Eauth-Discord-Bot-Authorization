import os
import requests
import json

BOT_TOKEN = '' # Your Discord bot token here
APP_KEY = '' # Your Eauth application key here
ACC_KEY = '' # Your Eauth account key here

def authority_check(user_id):
  # Send request
  response = requests.post('https://eauth.us.to/api/1.1/', headers={"User-Agent": "e_a_u_t_h"}, data = {'sort': 'authorize', 'platform': 'discord', 'userid': user_id, 'bottoken': BOT_TOKEN, 'appkey': APP_KEY, 'acckey': ACC_KEY})
  
  # Convert the JSON string to a Python dictionary
  data = json.loads(response.text)
  
  # Access the values in the dictionary
  if (data['message'] == 'access_granted'):
    # Remove the "message" key from the dictionary
    del data["message"]

    # Return user data
    return data
    
  else:
    return False
