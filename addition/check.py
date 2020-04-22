from DOLLAR import Dollar
from Hryvnia import Hryvnia
from EURO import Euro
from POUND import Pound
from YUAN import Yuan
from BITCOIN import Bitcoin

po = Pound()
dol = Dollar()
hr = Hryvnia()
euro = Euro()
yu = Yuan()
bitk = Bitcoin()
print(dol.get_currency_price())
print(hr.get_currency_price())
print(euro.get_currency_price())
print(po.get_currency_price())
print(yu.get_currency_price())
print(bitk.get_currency_price())