# **Forecasting-Stock-Market-Index**



## Motivation and Purpose of the project

As we know Stock Market prices are highly unpredictable and volatile. This means that there are no consistent patterns in the data that allow one to model stock prices over time near-perfectly. So, as a stock buyer, you can reasonably decide when to buy stocks and when to sell them to make a profit. Instead of considering it a stochatic or random process and that there is no hope for machine learning. We are trying to model the data, so that the predictions one makes correlate with the actual behavior of the data. This is where time-series modeling comes in. You need good machine learning models that can look at the history of a sequence of data and correctly predict what the future elements of the sequence are going to be.

## What does the project use?
We are working with Time Series Model, which analyzes a sequence of data points collected over a time interval. In time series analysis, analysts record data points at consistent intervals over a set period of time rather than just recording the data points intermittently or randomly. Time series data can be used for forecasting - predicting future data based on historical data.

## We are using 3 major open-source frameworks and tools in our project.

# Streamlit: The fastest way to build and share data apps


Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science. It is the fastest way to build and share data apps. We can develop and deploy our web app using Streamlit very easily. In just a few minutes you can build and deploy powerful data apps. 



# Prophet: Automatic Forecasting Procedure

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well. It works best with time series that have strong seasonal effects

# Yahoo Finance: To get free stock quotes 
Yahoo! Finance is a media property that is part of the Yahoo! network. It provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content. It also offers some online tools for personal finance management.

## Python Installation and proceedings

**1.** Make sure you have python installed in your system already. If not, you can install it using in following command your terminal for installation
```
sudo apt install python3.8
```
 check version using,
 ```
 python3 --version
 ```
**2.** Now, for installing and managing the software packages, we'll first install pip using 
```
sudo apt install python3-pip 
```
and can check version by
```
pip3 --version
```
**3.** Next thing to do is create a virtual environment to separate your site packages used in this project from your rest of the projects, therefore to install use,
```
pip install virtualenv
```
create virtual environment using,
```
virtualenv <your_env_name>
```
and activate using,
```
source <your_env_name>/bin/activate
```
**4.** Further install all necessary modules using 
```
pip install streamlit fbprophet yfinance ploty
```
This will install all the required packages for the project such as, *numpy, pandas, matplotlib, etc.*

**Note** - Make sure you install one of the major dependency of Prophet `pystan` explicitly. You can refer [doc](https://facebook.github.io/prophet/docs/installation.html) for the same and if you encounter an import error with prophet then degrade `holidays` version to `0.9.12` and clone the [repository](https://github.com/facebook/prophet).

**5.** It's time to write some code. Refer the file attached in the repository for the same and understand the working of each line through the comments.

**6.** After writing the code, let's run it using the following command through the terminal
```
streamlit run home/username/Documents/<project_name.py>
```
The Streamlit app will now be visible in your browser at `localhost:8501` .

**7.** Lastly you can deactivate the virtual environment by giving command `deactivate` to your terminal.

# Glimpse of the Web App

## Let's see which source code line is responsible for which part of the output in our web app.

### Note : View in Dark Dimmed mode for better experience.


**Input:**

![image](https://user-images.githubusercontent.com/74777863/143777636-b76e96ac-f975-46f2-9cf7-a0471533342f.png)

**Output:**

![image](https://user-images.githubusercontent.com/74777863/143777908-4d926f70-08a3-4d60-bfd9-409f4e7cedcf.png)

**Input:**

![image](https://user-images.githubusercontent.com/74777863/143776780-2dc64e0c-4b86-4eda-a4c9-49962e5df06d.png)
![image](https://user-images.githubusercontent.com/74777863/143777215-e1090e7a-1521-4cd5-9def-06772f50e6c2.png)
![image](https://user-images.githubusercontent.com/74777863/143777251-119823d2-de15-4a33-8791-3327d1b0f5ff.png)

**Output:**

![image](https://user-images.githubusercontent.com/74777863/143777918-b6bde3c6-1bcb-428c-8fb0-f238c0e9a38e.png)

**Input:**

![image](https://user-images.githubusercontent.com/74777863/143777278-cb67c3a7-ec0b-4ef6-9e5f-05039ffc04ac.png)

**Output:**

![image](https://user-images.githubusercontent.com/74777863/143777934-73fb10ae-47f7-48e3-b536-89e0326402ae.png)

**Input:** 

![image](https://user-images.githubusercontent.com/74777863/143777299-4b4fde20-561a-4432-94e0-0580c6e3d8ed.png)

**Output:**

![image](https://user-images.githubusercontent.com/74777863/143778039-99097379-6e1c-43ad-9cd2-e2be5f078e24.png)


**Input:**

![image](https://user-images.githubusercontent.com/74777863/143778143-81f8f361-ca70-4927-b398-9c299e1e861e.png)

![image](https://user-images.githubusercontent.com/74777863/143777377-ddbcd52c-7766-46c8-8b85-730742454733.png)

**Output:** 

![image](https://user-images.githubusercontent.com/74777863/143778154-2ad1f3c3-6f20-48b7-8313-cdcc1ae9a4be.png)



**Input:** 

![image](https://user-images.githubusercontent.com/74777863/143777431-d4f780e3-42d1-4ce0-b535-42f1e6e0fe9f.png)

**Output:**

![image](https://user-images.githubusercontent.com/74777863/143778165-6574aacc-0b9f-4bdc-8e36-86beb77bc5a9.png)



**Input:**

![image](https://user-images.githubusercontent.com/74777863/143777440-c59cf21e-ff2f-4409-a140-b1c90ba81bc0.png)

**Output:**

![image](https://user-images.githubusercontent.com/74777863/143778180-8eeeb94a-edf1-4ed4-981c-03f3dd7bf4ab.png)



Thankyou!

