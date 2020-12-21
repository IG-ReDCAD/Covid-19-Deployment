# Covid-19 News
Sentiment Analysis of the Covid-19 News.

![alt text](https://github.com/IG-ReDCAD/Covid-19-Deployment/tree/master/searchNews/static/news/img/img1.png)

#### Main Page
In the following image, we display the UI of our app. The app is powered by Django and Elasticsearch. To get the charts, a huge work was done behind the scenes. We, first of all, collected the labeled data. Second, we preprocessed and prepared the collected data to create the model. Third, we built the Machine Learning (ML) model. Finally, we created our app.

First, we collected data using Diffbot API to train our ML model in order to use it for prediction. The diffbot API allows us to collect labeld news related to Covid-19. Unfortunately, the collected Data was imbalanced. 

Second, understanding, visualizing and cleaning the data was needed to run machine learning algorithms. To clean and visualize our data, we used pandas. Then, to preprocess our data and create the matrices, we used the sklearn objects; TfidfVectorizer to create a tf-idf matrix. Once the fit_transform method had been applied, each text was returned as a vector. In addition to solve the problem of the imbalanced data, we used Over-Sampling techniques to fix it using the imblearn.over_sampling library. 

Third, after partitioning the data into two sets: train and test, we used Logistic Regression as a supervised learning classification algorithm to assign sentiments and to generate our model. Then, we evaluated our ML model using a Cross-validation technique. This technique traines our ML model on subsets of the available input data and evaluates them on the complementary subset of the data. We found a 78% as an accuracy score and for each sentiment we found a good precision score. To create our model, we used scikit-learn library. 

Finally, we fetched new data: news articles related to Covid-19, from the News API by making requests to the endpoint every 3 minutes. These articles are seeded into the Elasticsearch database. Then, it is used to run our saved machine learning model. Our model enables us to predict the sentiments of the new fetched data, in order to display these predictions on the UI using charts.
![alt text](https://github.com/IG-ReDCAD/Covid-19-Deployment/tree/master/searchNews/static/news/img/img2.gif)


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

