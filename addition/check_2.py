from covid import Covid19
import COVID19Py

covid19 = COVID19Py.COVID19()
a = list()
c = 1
'''
for i in covid19.getLocations():
    if i["country_code"] not in a:
        print(str(c) + '.', i["country"], '--', '?' + i["country_code"])
        c += 1
        a.append(i["country_code"])'''

location = covid19.getLocationByCountryCode("US")
print(location)
print(location[0]["country"])



