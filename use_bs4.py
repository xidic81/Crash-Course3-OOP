import requests
from bs4 import BeautifulSoup

url = 'http://detik.com/'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Hureee! Response = {response.status_code}')
        # print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'Oh nooo, salah requests {response.status_code}')
except Exception as e:
    print(f'Error Bang! {e}')
print('Program ended.')
