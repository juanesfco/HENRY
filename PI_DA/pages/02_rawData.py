import streamlit as st
import pandas as pd

df = pd.read_excel('raw_data/homicidios.xlsx')

if st.checkbox('show data'):
    st.dataframe(df)


