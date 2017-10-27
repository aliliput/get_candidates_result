
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import pandas as pd
import numpy as np
from pandas import Series

#元データを取得
def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    r = requests.get(url, headers=headers).content
    soup = BeautifulSoup(r, "lxml")
    return soup


# In[2]:


def get_status(soup):
    lists = soup.find_all("td", class_="status")
    listsStatus = []
    for i in lists:
        a = i.string
        if a == "前":
            b = "z"
        elif a == "元":
            b = "m"
        else:
            b = "n"
        listsStatus.append(b)
    return listsStatus

def get_results(soup):
    lists = soup.find_all("td", class_="rose")
    listsRose =[]
    for i in lists:
        if i.find("span", class_="shoto") != None:
            a = "s"
        elif i.find("span", class_="hito") != None:
            a = "h"
        else:
            a = "r"
        listsRose.append(a)
    return listsRose


# In[39]:


def get_party(soup):
    lists = soup.find_all("td", class_="party")
    listsParty = []
    b = ""
    for i in lists:
        a = i.string
        if a == "共産":
            b = "kyosan"
        elif a == "希望":
            b = "kibo"
        elif a == "自民":
            b = "jimin"
        elif a == "立憲":
            b = "rikken"
        else:
            b = "etc"
        listsParty.append(b)
    return listsParty


# In[4]:


def get_url():
    lists = []
    for i in range(1,48):
        n = str(i)
        if len(n) < 2:
            n = "0" + n
        a = "http://www.asahi.com/senkyo/senkyo2017/kaihyo/A" + n + ".html"
        lists.append(a)
    return lists


# In[40]:


def get_df():
    list_status = []
    list_party = []
    list_result =[]
    urls = get_url()
    for l in urls:
        soup = get_soup(l)
        list_s = get_status(soup)
        list_p = get_party(soup)
        list_r = get_results(soup)
        list_status.extend(list_s)
        list_party.extend(list_p)
        list_result.extend(list_r)
    resultsdf = pd.DataFrame([list_status, list_party, list_result], index=['Status','Party','Result'])
    return resultsdf.T


# In[41]:


resultsdf = get_df()


# In[42]:


jimin_r = resultsdf[resultsdf.Party == "jimin"]
len(jimin_r)


# In[43]:


len(jimin_r[jimin_r.Status == "z"])


# In[44]:


len(jimin_r[(jimin_r.Status == "z")&(jimin_r.Result == "s")])


# In[45]:


208/262*100


# In[46]:


rikken_r = resultsdf[resultsdf.Party == "rikken"]
len(rikken_r)


# In[47]:


len(rikken_r[rikken_r.Status == "z"])


# In[48]:


len(rikken_r[(rikken_r.Status == "z")&(rikken_r.Result == "s")])


# In[49]:


13/16*100


# In[50]:


kibo_r = resultsdf[resultsdf.Party == "kibo"]
len(kibo_r)


# In[51]:


len(kibo_r[kibo_r.Status == "z"])


# In[52]:


len(kibo_r[(kibo_r.Status == "z")&(kibo_r.Result == "s")])


# In[53]:


14/55*100


# In[122]:


289/len(resultsdf)*100


# In[124]:


prev = resultsdf[resultsdf.Status == "z"]
len(prev)


# In[127]:


len(prev[prev.Result=="s"])


# 269/398*100

# In[128]:


269/398*100


# In[129]:


len(resultsdf)

