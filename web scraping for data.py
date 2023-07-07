#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import csv


def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response , 'lxml')
    tag = soup.find('td' , {"id":"mp-right"})
    h=soup.find_all("h2")
    content = [span.text for span in h]
    
    with open("wiki.csv" , "w") as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(content)


Extract (url = "https://en.wikipedia.org/wiki/Lucknow")

