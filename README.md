Last Major Update: June 4' 2018 



About the Project
===
This is a Python/Machine Learning application. This application helps us find cheap airfares between an origin and one/several destination places using Python Machine learning techniques.

This is a backend application. No frontend is attached to the application yet. 

This repository helps us understand analysing Data retrieved from online source by using Machine Learning algorithm based on given requirements. By practicing such application, developers should have a basic level of understanding on how to structure a real life machine learning application. 

This project targets the beginners of Machine Learning who have basic knowledge on Machine Learning algorithms, and would like to see how to implement such algorithm in real life example. 




Table of Contents
===
 - Primary Technologies/concepts used
 - Knowledge-base
 - Know before you go
 - Technical Description
 - How to run the application



Primary Technologies/Concepts Used
=========
  - PhantomJS
  - Beautiful Soup
  - Sellenium
  - Pandas
  - Numpy
  - Matplotlib
  - What is User Agent
  - What is DOM
  

Know before you Go
======
 - Structure of a general machine learning application


Technical Description
===
There are four/five steps in this process:
<br />
**Step 1:**
<br>Sourcing airfare pricing data

To get the primary data, we will use Google's Flight Tracker which is called Google Flight Explorer. Once we set an origin and destination, it gives us a series of pricing data within a given time frame which ultimately helps us understand the changes in airfares over a period of time. For example, the following link will give you the airfare prices from Washington DC to the major cities within US for a 3-5 days trip. 
<!--
https://www.google.com/flights/explore/#explore;f=IAD,DCA,BWI;t=r-United+States-0x54eab584e432360b%253A0x1c3bb99243deb742;li=3;lx=5;d=2018-04-30
-->
This is our primary source of data for this project.


**Step 2:**
<br>Retrieving the fare data with web scraping technique

Python has a number of web scraping libraries such as beautifulsoup, requests, scrap. For this process, we need a browser to retrieve the data. 

**Step 3:** 
<br>Parsing the DOM to extract pricing data


**Step 4:**
<br>Sending real-time alerts using IFTTT



How to Run
===
Please follow the following steps to run the application on your local machine
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
[TBD]
