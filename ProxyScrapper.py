from six.moves import urllib
import urllib2, sys
from bs4 import BeautifulSoup
import validators

filepath = "export_data,csv"

#Open File 
f = open(filepath, "w")

parsedcount = 0 #Succesfully parsed




        
#Constructed link
url ='https://hidemyna.me/en/proxy-list/'

hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(url,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

#Check valid url to avoid unwanted exit
if validators.url(link):
    
    #Requesting url
    source = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(source,'lxml')#Passing  source html to soup

    #Central table has 1 attr , border = 1
    table = soup.find('table', {"class" : "proxy__t"})

    #If there are data to be exported
    if table:
            #Passing rows to csv
        for row in table.findAll("tr"):
            cells = row.findAll("td")

            #Building row for csv
            proxy_ip = cells[0].find(text=True)
            port  = cells[1].find(text=True)
            country = cells[2].find(text=True)
            
            #Line to be written onto csv file 
            line = (str(proxy_ip) + ',' + str(port) + ',' + str(perc) +  "\n")

            f.write(line)   # Write to csv

        # Output : Verified Date / Coins
    else:
        print ("ERROR:No table exists on :" + "Parsed ") 

        

# Output : Succesfully extracted url count
print("Succesfully Extracted : " + str(parsedcount) + "/" + str(URLCOUNT) + "Urls")

f.close()
