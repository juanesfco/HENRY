import streamlit as st
import pandas as pd

df = pd.read_csv('data/df_homicides.csv')

if st.checkbox('show data'):
    st.dataframe(df)


