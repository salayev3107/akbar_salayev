# sendmessage
# import requests
# token = '////'
# method = 'sendMessage'
# response = requests.post(
#     url = f'https://api.telegram.org/bot{token}/{method}',
#     data = {'chat_id':640872833,'text':'Hello Akbar'}
#   ).json()
# print(response)


# 1 sendVoice
# ovozli xabar yuboradigan method

import requests
token = '***'
method = 'sendVoice'
file_path = r'C:\Users\user\Downloads\win.mp3.mp3'

with open(file_path, 'rb') as audio_file:
  response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833},
    files = {'voice': audio_file}
   ).json()
print(response)

# 2 sendPhoto
# rasm yuboradigan method

import requests
token = '***'
method = 'sendPhoto'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833,'photo':'AgACAgIAAxkBAAEdCDpp2kddovRe3aintzv-95ESio4EuwACHBRrG_zr0UreZQen2BT7HQEAAwIAA3MAAzsE'},
       ).json()
print(response)


# 3 sendVideo
# video yuboradigan method

import requests
token = '***'
method = 'sendVideo'
video_path = r'C:\Users\user\Downloads\Telegram Desktop\video.mp4'
with open(video_path, 'rb') as video_path1:
 response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833},
    files = {'video': video_path1}
       ).json()
 print(response)

# 4 sendLocation
# lokatsiya yuboradigan method

import requests
token = '***'
method = 'sendLocation'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833,'latitude':41.223874,'longitude':69.170030}
  ).json()
print(response)

# 5 sendContact
# contact yuboradigan method

import requests
token = '***'
method = 'sendContact'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833,
            'first_name':'Akbar',
            'phone_number':+998997553107}
  ).json()
print(response)

# 6 sendPoll
# opros qiladigan method

import requests
token = '***'
method = 'sendPoll'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    json = {'chat_id':640872833,
            'question':'what is the capital of UZB?',
            'options':["moscow", "Tashkent", "rome", "paris"]}
  ).json()
print(response)

# 7 getUserProfilePhotos
# profile photo oladigan method

import requests
token = '***'
method = 'getUserProfilePhotos'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'user_id':640872833
            }
  ).json()
print(response)

# 8 sendVenue
# locationni boshqachasi tadbir otkaziladgan joy

import requests
token = '***'
method = 'sendVenue'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833,'latitude':41.536468411698806,'longitude':60.65131095499097,
            'title':'Dunyo Toyxonasi',
            'address':'Ургенч, ул. Ханкинская, д. 62а, Urgench, Узбекистан'}
  ).json()
print(response)

# 9 sendMessageDraft
# yozyatrganda qisman yazyatrgaliqini bildiradi(chernovik).

import requests
token = '***'
method = 'sendMessageDraft'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833,
            'draft_id':123,
            'text':'Hello how are you? '}
  ).json()
print(response)


#10 sendDocument
# document yuboradigan method

import requests
token = '***'
method = 'sendDocument'
response = requests.post(
    url = f'https://api.telegram.org/bot{token}/{method}',
    data = {'chat_id':640872833,
            'document':'BQACAgIAAxkBAAEdCTRp2mzeebSPlSKxj-KEujtrIFb1hQACoZgAAvzr0UqMOx-lTDeELjsE'}
  ).json()
print(response)

