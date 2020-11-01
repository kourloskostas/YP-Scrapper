from six.moves import urllib
import time
from bs4 import BeautifulSoup
import requests
import threading
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}




def validate(file_in , file_out ,thread_id):

  with open(file_in) as csv_file , open(file_out , 'w+') as output:
      csv_reader = csv.reader(csv_file, delimiter=',')
      csv_writer = csv.writer(output, delimiter=',')

      line_count = 0
      for row in csv_reader:

        try:
          url = row[6]
          print(url)
          if(url != 'Undefined'):
            print("Url is " + url)
            line_count += 1

            link = ('https://www.yellowpages.com'+ url)
            dreq = requests.get(link,headers=headers).text
            bs = BeautifulSoup(dreq,features="lxml")

            emails = bs.find_all('a', attrs={'class': 'email-business'})
            if emails:
              emapp = ''
              for email in emails:
                emapp += email['href'][7:] + ' / '
                
              row.append(emapp)
              csv_writer.writerow(row)

              print ('Emails are ' + emapp)
        except:
          print ('Malakia egine')
          time.sleep(3)
          pass




        print(f'Processed {line_count} lines.')


threads = []
for num in range(1,4):
  finame = 'unfiltered_0' + str(num) + '.csv'
  foname = 'filtered_0' + str(num) + '.csv'
  th = threading.Thread(target=validate,args=(finame ,foname ,num))
  print ('Starting thread' + str(num))
  th.start()

