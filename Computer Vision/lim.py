import requests
import json

response = requests.post(
    'https://api-service.vanceai.com/web_api/v1/upload',
    files={'file': open(r"C:\Users\aayus\Desktop\scrap\scrap_63ac2a0badb8b84ef73a9622_old.webp", 'rb')},
    data={'api_token': '1cf01f5867d8d96c6b9ead239c782a6a'},
)
r = response.json()

json_path = "enlarge.json"
jparam={}

with open(json_path, 'rb') as f:
    jparam = json.load(f)

data={
    'api_token': '1cf01f5867d8d96c6b9ead239c782a6a',
    'uid': r['data']['uid'],
    'jconfig': json.dumps(jparam),
    'webhook': 'https://your-domain/path/to/webhook'
    }
response = requests.post(
    'https://api-service.vanceai.com/web_api/v1/transform',data)
r = response.json()
# print(r)

remoteFileUrl = 'https://api-service.vanceai.com/web_api/v1/progress?trans_id={}&api_token=1cf01f5867d8d96c6b9ead239c782a6a'.format(r["data"]["trans_id"])
response = requests.get(remoteFileUrl)
r = response.json()
if r['code'] == 200:
    print('status:', r['data']['status'])

# remoteFileUrl = 'https://api-service.vanceai.com/web_api/v1/download?trans_id={}&api_token=1cf01f5867d8d96c6b9ead239c782a6a'.format(r["data"]["trans_id"])
# dst_path = 'demo.jpg'

# response = requests.get(remoteFileUrl, stream=True)
# print(response)

# f = open(dst_path, "wb")
# for chunk in response.iter_content(chunk_size=2048):
#     if chunk:
#         f.write(chunk)
# f.close()

