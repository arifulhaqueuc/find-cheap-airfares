import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from bs4 import BeautifulSoup

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


## step 1: get the data and instantiate the brower object
url = "https://www.google.com/flights/explore/#explore;f=IAD,DCA,BWI;t=r-Europe-0x46ed8886cfadda85%253A0x72ef99e6b3fcf079;li=3;lx=5;d=2018-01-15"
driver = webdriver.PhantomJS()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
  
  )
driver = webdriver.PhantomJS(
  desired_capabilities=dcap, service_args=[
    '--ignore-ssl-errors=true'
    ]
  )
  
driver.implicity_wait(20)
driver.get(url)



## Step 2: Retrieve fare Data using web scraping
s = BeautifulSoup(driver.page_source, "lxml")
## List of all best prices
best_price_tags = s.findAll('div', 'LH3SCIC-w-e')
best_prices = []
for tag in best_price_tags:
    best_prices.append(int(tag.text.replace('$','').replace(',','')))
print(best_price_tags)
best_prices = best_prices[0]
print(best_prices)

## Get the list of bar height for each
best_height_tags = s.findAll('div', 'LH3SCIC-w-f')
best_heights = []
for t in best_height_tags:
    best_heights.append(float(t.attrs['style']\
          .split('height:')[1].replace('px;','')))
best_height = best_heights[0]
print(best_height)

## Calculate price per pixel
pph = np.array(best_price)/np.array(best_height)
print(pph)
cities = s.findAll('div', 'LH3SCIC-w-o')
print(cities)


hlist=[]
for bar in cities[0].findAll('div', 'LH3SCIC-w-x'):
        hlist.append(float(bar['style'].split('height: ')[1].replace('px;',''))*pph)

fares = pd.DataFrame(hlist, columns=['price'])
print(fares)

## calculate the minimum fare
minimum_fare = fares.min()
print(minimum_fare)


fig, ax = plt.subplots(figsize=(10,6))
plt.scatter(np.arange(len(fares['price'])), fares['price'])


px = [x for x in fares['price']]
ff = pd.DataFrame(px, columns=['fare']).reset_index()

X = StandardScaler().fit_transform(ff)
db = DBSCAN(eps=.5, min_samples=1).fit(X)



labels = db.labels_
clusters = len(set(labels))
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

plt.subplots(figsize=(12,8))
for k, c in zip(unique_labels, colors):
    class_member_mask = (labels == k)
    xy = X[class_member_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=c,
        markeredgecolor='k', markersize=14)
plt.title("Total Clusters: {}".format(clusters), fontsize=14,
    y=1.01)


    