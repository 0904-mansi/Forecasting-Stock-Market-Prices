# importing libraries and site packages
import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# Defining a start date so that we can get a range of data from that date till today
START = "2011-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Providing a title to the project
st.title('Predict over data')

# yfinance has its abbreviations defined for the stocks, we are here picking few and using them
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
# creating a select box using streamlit feature
selected_stock = st.selectbox('Select dataset for prediction', stocks)

# Setting a slider for the years of prediction and getting the details of prices of stock of each day
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

# Definig a function to fetch the stock quotes
@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Loading data from yfinance for selected stocks using load_data()
# Caching it so that if I chose AAPL first and get stock prices and then get the same for GOOG, and again switches to AAPL then data will not be fetched again rather will be saved due to earlier access	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')


st.subheader('Raw data')
st.write(data.tail())

# Plotting the raw data
def plot_raw_data():
	fig = go.Figure()
# Open is the first price that someone has paid for for share of the particular stock.
# Close is the last price that someone has paid for a share of the particular stock.
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predicting forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Showing and plotting the forecast with the help of plotly
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

# Forecast components
st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)
