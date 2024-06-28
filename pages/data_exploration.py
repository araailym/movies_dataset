import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import random



st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """Here you can see the dataframe. """
)


@st.cache_data
def load_data():
    df = pd.read_csv('movie_dataset.csv')
    return df

df = load_data()


st.dataframe(
    df,
    column_config={
        "Movie_Title": "Movie Title",
        "Main_Actor": "Main Actor",
        "Production_Company": "Production Company",
        "Release_Year": "Release Year",
        "Movie_Category": "Movie Category",
        "Num_Screens": "Number of Screenings",
        "Marketing_Spend": "Marketing Expenses",
        "Social_Media_Buzz": "Social Media Buzz",
        "Box_Office_Success": "Box Office Success",
    },
    hide_index=True,
)

