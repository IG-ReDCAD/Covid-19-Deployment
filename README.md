# Covid-19 News
Sentiment Analysis of the Covid-19 News.
![alt text](https://github.com/IG-ReDCAD/Covid-19-Deployment/blob/master/searchNews/static/news/img/img2.jpg "Web App Design")

#### Main Page
This is how the web app is displayed when user navigates to this website. The app is powered by Django and Elasticsearch. News articles related to Covid-19 are fetched from the News API by making requests to the endpoint every 3 minutes. The articles so retrieved are seeded into the Elasticsearch database. These articles are then used to run the machine learning model and perform sentiment analysis. The model is designed to calculate the sentiment every time the database is seeded with new articles in order to ensure that the users are provided with the latest information. These sentiment calculations are then rendered on the UI using charts.


#### Charts
The charts are powered using the Charts.js JavaScript library. The metrics in the charts are populated with the sentiment analysis performed on the backend. The doughnut displays the overall statistics of the sentiments of all the news in the database. The line chart displays the daily statistics of the sentiment of news articles seeded into the database each day.


#### Latest News Articles
The user can also review Covid-19 related news, and navigate to any news article by clicking on them. In order to ensure that the API rate limit is not exceeded, the algorithm is designed to render the latest news from data that is cached in the database.

## Deployment (TBD)
Deploy Elasticsearch on AWS EC2 server.
Deploy the Django app on Huroku.


## Table of contents
* [Tech Stack](#tech-stack)
* [Third Party APIs](#api)
* [Installation](#installation)

## <a name="tech-stack"></a>Tech Stack
* Bootstrap
* CSS
* Django
* Elasticsearch
* HTML
* JavaScript (jQuery, Charts.js)
* Python

* ML libraries
  - Imblearn
  - Pandas
  - Numpy
  - Sklearn

## <a name="api"></a>Third Party APIs
* Diffbot Article API
* News API



## <a name="installation"></a>Installation
To run the web app on your own machine:
Go to: 
```
https://github.com/shimoleejhaveri/Covid19-News-Project.git
```

