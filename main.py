from cgitb import text
import requests

session = requests.Session()
response = session.post('https://netstalkers.com/api/auth/jwt/create/', {
     'password': 'Artem1337k.',
     'username': 'devil666face',
})
cookies = session.cookies
# print(response.text)
# get_resp = session.get('https://netstalkers.com/api/patrons/post/29/')
# ans = get_resp.json()
# for i in range(10):
try:
    url = f'https://netstalkers.com/api/patrons/?page={1}'
    page_json = session.get(url).json()
    print(page_json)
except Exception as ex:
    print(ex)

# print(ans['video'])
# video_resp = session.get(ans['video'])
# print('save')
# with open("video.mp4", "wb") as code:
#     code.write(video_resp.content)