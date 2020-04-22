import requests

from bs4 import BeautifulSoup


class Bitcoin:
    BITOK_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BD%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&rlz=1C1VLSB_enRU725RU772&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BD%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&aqs=chrome..69i57j35i39j0l6.8181j1j7&sourceid=chrome&ie=UTF-8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
       self.norm_bit = 6000

    def get_currency_price(self):
        full_page = requests.get(self.BITOK_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Цена Биткоина в рублях: {}".format(convert[0].text.replace(',', '.'))

    def check_currency(self):
        pass


