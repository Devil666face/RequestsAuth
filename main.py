import requests
import re

session = requests.Session()
response = session.post('https://netstalkers.com/api/auth/jwt/create/', {
     'password': 'Artem1337k.',
     'username': 'devil666face',
})
cookies = session.cookies

video_dict = dict()

def get_title(name):
    title = re.sub("[^А-Яа-яA-Za-z0-9\s]", "", name)
    print(f'{title}')
    return title

for i in range (1,100):
    try:
        url = f'https://netstalkers.com/api/patrons/?page={i}'
        page_json = session.get(url).json()
        result = page_json.get('results')
        for item in result:
            video_dict[item.get('id')] = get_title(item.get('title','video'))
    except Exception as ex:
        break


for video_id in video_dict:
    url = f'https://netstalkers.com/api/stream/{video_id}/'
    print(f'Скачиваю {url}')
    
    video_response = session.get(url)
    print(video_response)
    with open(f'{video_dict.get(video_id)}.mp4','wb') as video:
        video.write(video_response.content)
