import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': 'phone_number_receiver',
  'message': 'your text message',
  'key': 'textbelt',
})
print(resp.json())