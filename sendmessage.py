import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '9422195873',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())