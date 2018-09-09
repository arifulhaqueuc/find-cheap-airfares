Last Major Update: June 4' 2018 
Next Major Update(estimated): Sept 2018


About the Project
===
About | Description
---- | ----
Overview | This is a Machine Learning application powered by Python. | The objective of this application is to help us find cheap airfares between an origin and one/several destination places using Python Machine learning techniques.
Application Nature | This is a backend application. No frontend is attached to the application yet. 
Objective | This repository helps us understand analysing Data retrieved from online source by using Machine Learning algorithm based on given requirements. By practicing such application, developers should have a basic level of understanding on how to structure a real life machine learning application. 
Target Audience | This project targets the beginners of Machine Learning who have basic knowledge on Machine Learning algorithms, and would like to see how to implement such algorithm in real life example. 



Primary Technologies/Concepts Used
=========
Topics | What is It | Links
----- | ---- | ----
PhantomJS | --- | ---
Beautiful Soup | --- | ---
Sellenium | Testing tool | ---
Pandas, Numpy | Python library for data science | ---
Matplotlib | Python package for data visualization | ---
DOM | Document Object Model | ---
  

Know before you Go
======
 - Structure of a general machine learning application
 - What is User Agent
 - Use of Sellenium 
 - Use of DOM

Technical Description
===
There are four/five steps in this process:
<br />

Step | Function | Description
--- | --- | ---
#1 | Sourcing airfare pricing data | To get the primary data, we will use Google's Flight Tracker which is called Google Flight Explorer. Once we set an origin and destination, it gives us a series of pricing data within a given time frame which ultimately helps us understand the changes in airfares over a period of time. For example, the following link will give you the airfare prices from Washington DC to the major cities within US for a 3-5 days trip. This is our primary source of data for this project.
#2 | Retrieving the fare data | Used web scraping technique to retrieve the data from the data source. Python has a number of web scraping libraries such as beautifulsoup, requests, scrap. For this process, we need a browser to retrieve the data. 
#3 | Parsing the DOM to extract pricing data | ---
#4 | Sending real-time alerts using IFTTT | ----



How to Run
===
Please follow the following steps to run the application on your local machine
  - setup a virtual environment in local machine ([https://github.com/arifulhaqueuc/python-project-startup-guide/blob/master/virtual_env.MD])
  - clone the repo
  - install the requirements from requirements.txt file
  - go to the app directory
  - run the app file

  

Support & Disclaimer
===
#### Support
Found a bug?? Here are the options
  - Please file an issue with detailed description.
  - If you know a possible solution, please create a new brnach, update the code and then submit pull request.
  - If you would  like to reach out to me directly with any question, email me at ariful.haque.uc@gmail.com

#### General Disclaimer
This is my personal project and not an official product of any company. If you would like to use this code, please keep it in your mind that, although I have tried to make it as error-free as possible, there's no warranty of a 100% bug free application. 




References
===
 - https://www.google.com/flights/explore/#explore;f=IAD,DCA,BWI;t=r-United+States-0x54eab584e432360b%253A0x1c3bb99243deb742;li=3;lx=5;d=2018-04-30


