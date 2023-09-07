import re
import urllib.request

sites = ['https://www.google.com/', 'https://www.youtube.com/']
for site in sites:
    print('Searching the site ', site)
    site_url = urllib.request.urlopen(site)
    content = site_url.read()
    title = re.findall("<title>.*</title>", str(content), re.IGNORECASE)
    print(title[0])

site = urllib.request.urlopen("https://www.redbus.in/info/contactus")
text = site.read()
zipcodes = re.findall('[- ][0-9]{6}', str(text))
for zipcode in zipcodes:
    print(zipcode)

data = input('Enter mail id\n')
match = re.fullmatch('\\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]+', data)
if match is not None:
    print("Valid mail id")
else:
    print("Invalid mail id")


data = input('Enter car number\n')
match = re.fullmatch('TN[0-3][0-9][A-Z]{2}\\d{4}', data)
if match is not None:
    print("Valid number")
else:
    print("Invalid number")
