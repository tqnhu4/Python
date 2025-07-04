import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the application
st.title('Hello Streamlit! 👋')

# Display a simple text message
st.text('This is a basic Streamlit application to get familiar with its components.')
st.text('Below you will see a randomly generated line chart.')

# Generate some sample data for the line chart
# We'll create a DataFrame with some random numbers
chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 20 rows, 3 columns of random numbers
    columns=['a', 'b', 'c'] # Column names
)

# Display the line chart using the generated data
st.line_chart(chart_data)

# Use st.write() to display various types of content
st.write('---') # A horizontal rule for separation
st.write('You can also use `st.write()` to display text, DataFrames, and more.')
st.write('Here is the raw data used for the chart:')
st.write(chart_data) # Display the DataFrame itself

st.write('---')
st.write('Explore the data and the chart! ✨')