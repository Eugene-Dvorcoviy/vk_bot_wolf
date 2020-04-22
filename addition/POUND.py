import requests

from bs4 import BeautifulSoup


class Pound:
    POUND_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk01umtxI7WfZCuQPQyMdy_8fjDelYA%3A1586890140719&ei=nAWWXvyyK8SRrgSisLugBA&q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjIHCAAQFBCHAjICCAAyBwgAEBQQhwIyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6CQgAEAoQRhCCAjoECAAQCkoUCBcSEDYtMTc1ZzE4NWcxNjdnNjBKDQgYEgk2LTFnMmcxZzNQ-hxYhCpgqCxoAXACeACAAc0BiAHIBpIBBTAuNC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwj88Im5yujoAhXEiIsKHSLYDkQQ4dUDCAw&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        '''self.current_euro = float(self.get_currency_price())'''

    def get_currency_price(self):
        full_page = requests.get(self.POUND_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Курс Рубля к Пунду Стерлингов: {}".format(convert[0].text.replace(',', '.'))

    def check_currency(self):
        pass


