# import library
from bs4 import BeautifulSoup
import requests
import pandas as pd

data1 = []
for page in range(1, 2):
  if page ==1:
   url = "https://turnbackhoax.id/?s=aceh"
  else:
   url = "https://turnbackhoax.id/page/" + str(page) + "/?s=aceh"
  req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

column = soup.findAll("div", "mh-loop-content mh-clearfix")

for scraping in column:
  text = scraping.find("h3","entry-title mh-loop-title").text.strip().split("\n")
  link = scraping.find("a", {"rel":"bookmark"})["href"]
  print(text, link)

  data1.append([text, link])

df1 = pd.DataFrame(data1)
df1.head()

df1.rename(columns={0:"Berita",1:"URL"}, inplace = True)
df1.head()

df1.info()

data2 = []
for page in range(1, 2):
  if page ==1:
   url = "https://turnbackhoax.id/?s=tsunami"
  else:
   url = "https://turnbackhoax.id/page/" + str(page) + "/?s=tsunami"
   req = requests.get(url)
   soup = BeautifulSoup(req.text, "html.parser")

   column = soup.findAll("div", "mh-loop-content mh-clearfix")

   for scraping in column:
     text = scraping.find("h3","entry-title mh-loop-title").text.strip().split("\n")
     link = scraping.find("a", {"rel":"bookmark"})["href"]
     print(text, link)
 
     data1.append([text, link])

import pandas as pd

df2 = pd.DataFrame(data2)
df2.head()


df2.rename(columns={0:"Berita",1:"URL"}, inplace = True)
df2.head()

data_scrap = [df1, df2]

data_scraping = pd.concat(data_scrap)

data_scraping.head()

data_scraping.info()

data_scraping.tail()

data_scraping.to_csv("data scraping.csv", index=False)

hr = pd.read_csv("data scraping.csv")
hr.head()