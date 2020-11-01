from six.moves import urllib
import time
from bs4 import BeautifulSoup
import validators
import requests



States = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI',
 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT',
  'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD',
   'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']

Businesses = ['Electricians','Concrete','Plumber','Dinner']

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
filepath = 'bbb/unfiltered.csv'
f = open(filepath, "w+")
line = 'Name , Phone , Address , Locality , Url \n'
f.write(line)

for state in States:
  for business in Businesses:
    
    page = 1

    while True:
      print ('\n Searching ' + business + ' , page :' + str(page))
        
      link = ('https://www.yellowpages.com/search?search_terms=' + business + '&geo_location_terms=' + state + '&s=default&page=' + str(page))
      try:
        dreq = requests.get(link,headers=headers).text
        bs = BeautifulSoup(dreq,features="lxml")

        listings = bs.find_all('div', attrs={'class': 'result'})
      except:
        break

      if not listings:
        break

      for listing in listings:
    
        try:
          url   = listing.find("a", class_="business-name")['href']
        except:
          url = 'Undefined'
        try:
          name      = listing.find("a", class_="business-name").text
        except:
          name = 'Undefined'
        try:
          info      = listing.find("div", class_="categories").text
        except:
          info = 'Undefined'
        try:
          website   = listing.find('a', attrs={'class': 'track-visit-website'})['href']
        except:
          website = 'Undefined'
        try:
          phone     = listing.find("div", class_="phones phone primary").text
        except:
          phone = 'Undefined'
        try:
          address   = listing.find("div", class_="street-address").text
        except:
          address = 'Serving the ' + state + ' area.'
        try:
          locality  = listing.find_all("div", class_="locality")[0].text
        except:
          locality = 'Serving the ' + state + ' area.'
        try:
          #Line to be written onto csv file     
          line = ('"' + str(name).rstrip() + '"' + ',' + '"' + str(info).rstrip() + '"' + ',' + '"' + str(website).rstrip() + '"' + ','+ '"' + str(phone) + '"' + ',' + '"' + str(address).rstrip() + '"' + ',' + '"' + str(locality).rstrip() 
          + '"' + ',' + '"' + str(url).rstrip() + '"' + "\n")
          
          f.write(line)   # Write to csv
      
          print ('====================')
          print ('Name :' + name)
          print ('Phone :' + phone)
          print ('Location :' + locality)
        except:
          print 'Probably ascii problem '


      page +=1
      
  
f.close()
