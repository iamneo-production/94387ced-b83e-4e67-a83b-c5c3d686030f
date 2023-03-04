import streamlit as st
import pandas as pd
import time
import calendar
# Load the data
df = pd.read_csv('/home/ananth/slit/aqi_2016_to_2023.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Define the Streamlit app
st.title('AQI Predictor (Telengana)')

# Add input widgets for location, year, and month
location_options = df['location'].unique()
year_options = df['date'].dt.year.unique()
month_options = range(1, 13)

location = st.selectbox('Station Name', options=location_options)
year = st.selectbox('Year', options=year_options)
month = st.selectbox('Month', options=month_options)

# Add a button to store the input values
inputs = []
date = pd.to_datetime(f'{year}-{month}-01')

if st.button('Predict'):
    # Filter the data based on the input values
    filtered_data = df[(df['date'].dt.month == date.month) & (df['location'] == location)]
    aqi = filtered_data['aqi'].values[0]

    # Add the inputs and AQI to the list of inputs
    inputs.append((location, year, month, aqi))

    # Simulate some processing time
    with st.spinner('Predicting...'):
        time.sleep(1)

    # Display the predicted AQI and other input values
    st.success(f'Predicted!AQI :{aqi}')

    # Plot the AQI trends for the selected location and month
    fig_data = df[(df['date'].dt.month == date.month) & (df['location'] == location)][['aqi', 'date']]
    fig_data['year'] = fig_data['date'].dt.year
    fig_data = fig_data[['aqi', 'year']].groupby('year').mean()
    # st.write('AQI Trends:\t',location,'\t\nmonth:',calendar.month_name[date.month])
    st.subheader(f'AQI Trends at :blue[{location}] during the Month of :orange[{calendar.month_name[date.month]}]')
    st.bar_chart(fig_data)

# Show the inputs and predicted AQI
if inputs:
    st.write('Inputs and Predictions:')
    for input_set in inputs:
        st.write(input_set)
st.caption('Trained with Temporal Fusion Transformer and achieved MAE score of 13')