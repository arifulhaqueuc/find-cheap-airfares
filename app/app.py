import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from bs4 import BeautifulSoup



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

driver.save_screenshot(r'flight_explorer.png')

