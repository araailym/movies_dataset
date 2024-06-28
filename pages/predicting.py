
import streamlit as st
import pandas as pd
import altair as alt
import time
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title=" Demo", page_icon="")

st.markdown("# Predicting ")
st.sidebar.header("Predicting Demo")
st.write(

)

@st.cache_data
def load_data():
    df = pd.read_csv('movie_dataset.csv')
    return df

df = load_data()

df=pd.read_csv('movie_dataset.csv')


df.drop(["Movie_Title",'Director','Main_Actor','Production_Company'],axis=1,inplace=True)



year=st.slider("Release Year", 2005, 2024, 2016)
category = st.selectbox('Category', ['AAA','A','B','C'])
budget=st.slider("Budget", 1,200,1)
duration=st.slider("Duration", 1,300,1)
numscreen=st.slider("Number of Screenings", 1,200,1)
marketing=st.slider("Marketing Spend", 1,200,1)
buzz=st.slider("Social Media Buzz", 1,200,1)
genre=st.selectbox('Genre', df["Genre"].unique())

df = pd.get_dummies(df, columns = ['Genre'])


df.loc[df['Movie_Category'] == 'AAA', 'Movie_Category'] = 4
df.loc[df['Movie_Category'] == 'A', 'Movie_Category'] = 3
df.loc[df['Movie_Category'] == 'B', 'Movie_Category'] = 2
df.loc[df['Movie_Category'] == 'C', 'Movie_Category'] = 1

df.loc[df['Box_Office_Success'] == 'High', 'Box_Office_Success'] = 3
df.loc[df['Box_Office_Success'] == 'Medium', 'Box_Office_Success'] = 2
df.loc[df['Box_Office_Success'] == 'Low', 'Box_Office_Success'] = 1

X=df.drop(["Box_Office_Success",'Rating'],axis=1)
y=df['Box_Office_Success']

cat_features = [0,1,7,8,9,10,11]
#cb = CatBoostClassifier({'n_estimators': 150, 'max_depth': 3})
#cb.fit(X, y, cat_features=cat_features)

linreg=LinearRegression()
linreg.fit(X, y)



def to_cat_preds2(series: pd.Series):
    upper_bound= 1.303030
    lower_bound= 1.272727
    for idx, val in series.items():
        if val > upper_bound:
            series[idx] = 'High'
        elif val >= lower_bound and val <= upper_bound:
            series[idx] = 'Medium'
        elif val < lower_bound:
            series[idx] = 'Low'
    return series
data={
       "Release_Year":year,
    "Movie_Category":category,
    "Genre":genre,
    "Budget":budget,
    "Duration":duration,
    "Num_Screens":numscreen,
    "Marketing_Spend":marketing,
    "Social_Media_Buzz":buzz,

    }

    #st.write(data)
if st.button("Predict"):
    df2=pd.DataFrame(data, index=[0])
    df2=pd.get_dummies(df2,columns=["Genre"])


    df2.loc[df2['Movie_Category'] == 'AAA', 'Movie_Category'] = 4
    df2.loc[df2['Movie_Category'] == 'A', 'Movie_Category'] = 3
    df2.loc[df2['Movie_Category'] == 'B', 'Movie_Category'] = 2
    df2.loc[df2['Movie_Category'] == 'C', 'Movie_Category'] = 1
    for col in X.columns:
        if col not in df2.columns:
            df2[col]=0
    df2=df2[X.columns]
    #st.dataframe(df2)
    #pred = cb.predict(df2)

    preds = linreg.predict(df2)

    p2 = to_cat_preds2(pd.Series(preds))


    st.success(f"Predicted box office success : {p2[0]}")
