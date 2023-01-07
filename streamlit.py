import streamlit as st
import pandas as pd

st.title('VMI Dashbaord')

option = st.selectbox(
    'Week',
    ['22'+str(i) for i in range(0,20)])



st.write('My first Streamlit app')
df = (pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
st.table(df)


st.write('You selected:', option)