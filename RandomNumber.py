import requests
from bs4 import BeautifulSoup
while True:

    url = "https://www.calculator.net/random-number-generator.html?slower=1&supper=100&ctype=1&s=2254&submit1=Generate"
    r=requests.get(url)
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    result = soup.find('p', {'class': 'verybigtext'}).text.strip()
    print(result)