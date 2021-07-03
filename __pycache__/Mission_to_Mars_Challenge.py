#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[17]:


#html = browser.html
#img_soup = soup(html, 'html.parser')
#img_soup


# In[18]:


# 2. Create a list to hold the images and titles.
#hemisphere_image_urls = []
#Find the HTML tag that holds all the links to the full-resolution images, or find a common CSS element for the full-resolution image.
#Using a for loop, iterate through the tags or CSS element.
#Create an empty dictionary, hemispheres = {}, inside the for loop.
#Use the for loop to complete the following actions: a) click on each hemisphere link, b) navigate to the full-resolution image page, c) retrieve the full-resolution image URL string and title for the hemisphere image, and d) use browser.back() to navigate back to the beginning to get the next hemisphere image.
#Save the hemisphere image title as the value for the title key that will be stored in the dictionary you created from the Hint.
#Before getting the next image URL and title, add the dictionary with the image URL string and the hemisphere image title to the list you created in Step 2.
# 3. Write code to retrieve the image urls and titles for each hemisphere.
#def hemisphere(browser):
url = 'https://marshemispheres.com/'
browser.visit(url)
    
    #find_by_tag('button')[1]
    #itemLink product-item
    #<img class="thumb" src="images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png">
    
    #img_url_name = browser.find_by_tag('itemLink product-item')
    #brower.find_image
img_url_name = browser.find_by_css('a.product-item img') #.get('src')
title = browser.find_by_tag('h3').text
    #title = img_soup.find('img', class_='fancybox-image').get('src')
    
hemisphere_image_urls = []
    
for i in range(len(img_url_name)):
    hemispheres = {}
    browser.find_by_css('a.product-item img')[i].click()
    title_code = browser.links.find_by_text('Sample').first
    hemispheres['image_url'] = title_code['href']
    hemispheres['title'] = browser.find_by_css('h2.title').text

    hemisphere_image_urls.append(hemispheres)

    browser.back()

#return hemisphere_image_urls


# In[19]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[20]:


# 5. Quit the browser
browser.quit()


# In[ ]:




