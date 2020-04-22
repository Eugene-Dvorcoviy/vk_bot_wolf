import requests

from bs4 import BeautifulSoup


class Yuan:
    YUAN_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk01y9cS4_mNRB9rrJta9s12O16G6Xw%3A1586890147742&ei=owWWXvTkLIKvrgTw4qzwCA&q=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjIHCAAQFBCHAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgcIIxDqAhAnOgQIIxAnOgUIABCDAToECAAQQzoHCAAQgwEQQzoJCCMQJxBGEIICOgQIABAKSikIFxIlMGcxNjJnMTU1ZzE2N2cxNjdnMTUzZzE3MGcxOTBnMTM0ZzExNUoXCBgSEzBnMmcxZzFnMWcxZzJnMWcxZzNQpakPWMP-D2CdgRBoBHABeACAAbgBiAHRDpIBBDAuMTKYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwi0wra8yujoAhWCl4sKHXAxC44Q4dUDCAw&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        '''self.current_euro = float(self.get_currency_price())'''

    def get_currency_price(self):
        full_page = requests.get(self.YUAN_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Курс Рубля к Юаню: {}".format(convert[0].text.replace(',', '.'))



