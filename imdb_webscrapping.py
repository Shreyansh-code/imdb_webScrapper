#!/usr/bin/env python
# coding: utf-8

# In[36]:


from bs4 import BeautifulSoup
import requests
import csv


# In[2]:


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


# In[3]:


page = requests.get(url)


# In[7]:


soup = BeautifulSoup(page.text, "html.parser")


# In[14]:


raw_html = soup.find("tbody", {"class": "lister-list"}).findAll("tr")


# In[ ]:


def main_function():
    movie_list = []
    for html in raw_html:
        title = html.find("td", {"class": "titleColumn"}).find("a").get_text()

        rating = html.find("td", {"class": "ratingColumn imdbRating"}).find("strong").get_text()
        rating = float(rating)
        raw_list = [title, rating]
        movie_list.append(raw_list)

    recommendation(movie_list)
    create_csv(movie_list)


# In[ ]:


def recommendation(m_list):
    user = float(input("Rating:"))
    print("Movie above rating", user)
    for x in range(len(m_list)):
        if m_list[x][1]>user:
            print(m_list[x][0])


# In[ ]:


def create_csv(movie):
    with open('movie.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        row = ['Name', 'Rating']
        writer.writerow(row)
        for x in range(len(movie)):
            row = movie[x]
            writer.writerow(row)
    csvfile.close()        


# In[ ]:


main_function()


# In[ ]:




