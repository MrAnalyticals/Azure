**Connecting Rest API data to your Azure Databricks Notebook**

YouTube Video: https://youtu.be/0bn8BklUqMc

In this demo I show you how to connect REST API available data to your Azure Databricks notebook. 
In Microsoft's documentation page, entitled PySpark basics, 
[the url in this video's description,
https://learn.microsoft.com/en-us/azure/databricks/pyspark/basics]
there is information about creating a DataFrame from a JSON response returned by calling a REST API. It uses a Python requests package. You must import that package into your Databricks notebook to use it. 
The example provided, in that documentation page, uses data that does not have particular relevance to many residents in Europe or indeed, to many people outside the USA. So, let's use some data relevant to political science and in particular helpful to my task of understanding how and why political regimes come into being and take over a country. In my azure sql server database, as mentioned in my previous Databricks videos, I already have a table that lists many countries and their political regimes together with some relevant statistics. But with this demo let's delve a little deeper into what other information is available online and also relevant in assisting us with my aim. 

So, I found "Our World in Data" which offers a Chart Data API that allows you to access data in CSV and JSON formats. This API is designed to support automated workflows and custom applications which sounds perfect to me.
![image](https://github.com/user-attachments/assets/32e6cf14-8d53-43e1-ae92-ede0be50e869)

The url is available in this video's description. Let's connect to it and see what we have, shall we?
[https://ourworldindata.org/easier-to-reuse-our-data]
In the meantime let's have a look at an animated chart displayed on the "Our World in Data" site entitled Political Regime that displays the change in regime type across the planet, over time.

 
The Our World in data website describes its mission as follows:
Poverty, disease, hunger, climate change, war, existential risks, and inequality: The world faces many great and terrifying problems. It is these large problems that our work at Our World in Data focuses on. We want to improve the problem of data being inaccessible, to make research and data on the world's biggest challenges easier for everyone to understand and use, to make progress against those challenges." Sounds pretty perfect to me and a cause almost everyone should be working on, also. 

[For those wanting to make a donation to the Our World in Data mission use this link: https://ourworldindata.org/donate]

[The help page on using the REST API's available is here: https://docs.owid.io/projects/etl/api/#chart-data-api]

By searching their site for charts I found some REST APIs.
[Searching their data catalog at https://ourworldindata.org/data.]
Let’s review the code next.
The metadata urls provide information about the data set being queried.
Next I import the  headers then  I assign the REST API url to a variable. 
Next using the requests function I test the response is 200 and then proceed to write the response to the temp directory on the local file system of the driver node in the current Databricks cluster.
I then create a dataframe of the data using the spark read load functions and finally display it.
Interestingly the Life expectancy in Afghanistan, in 1950, was 27 years. Anyone in their 30’s was considered old. What other interesting facts are there in this data set? Let’s explore that in my next video, shall we? 


LinkedIn headline
•	Life expectancy in Afghanistan in 1950 was 27 years.
