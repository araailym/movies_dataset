


import streamlit as st
import pandas as pd
import altair as alt
import time



st.set_page_config(page_title=" Demo", page_icon="")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """Here are some plots. """
)


@st.cache_data
def load_data():
    df = pd.read_csv('movie_dataset.csv')
    return df


df = load_data()



df['Release_Year'] = df['Release_Year'].astype(str)
df['Box_Office_Success'] = df['Box_Office_Success'].astype(str)
_="""movie_counts = df.groupby('Release_Year').size().reset_index(name='count')

# Calculate the rolling mean
movie_counts['rolling_mean'] = movie_counts['count'].rolling(window=10, min_periods=1).mean()

bar = alt.Chart(movie_counts).mark_bar().encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('count:Q', title='Number of Movies')
)

# Create the line chart
line = alt.Chart(movie_counts).mark_line(color='red').encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('rolling_mean:Q', title='Rolling Mean of Movies')
)


chart=(bar + line).properties(width=600)


st.altair_chart(chart)


budget_sums = df.groupby('Release_Year')['Budget'].sum().reset_index(name='sum_budget')
budget_sums['bos_percent']=df.groupby('Release_Year')['Box_Office_Success'].size()
budget_sums['rolling_mean'] = budget_sums['sum_budget'].rolling(window=10, min_periods=1).mean()

bar = alt.Chart(budget_sums).mark_bar().encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('sum_budget:Q', title='Total Budget')
)

# Create the line chart
line = alt.Chart(budget_sums).mark_line(color='red').encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('rolling_mean:Q', title='Rolling Mean of Total Budget')
)

# Combine the charts
chart = (bar + line).properties(width=600)

# Display the chart using Streamlit
st.altair_chart(chart)



"""


budget_sums = df.groupby('Release_Year')['Budget'].sum().reset_index(name='sum_budget')
budget_sums['bos_percent']=df.groupby('Release_Year')['Box_Office_Success'].size()
budget_sums['rolling_mean'] = budget_sums['sum_budget'].rolling(window=10, min_periods=1).mean()

chart=st.empty()
for i in budget_sums.index:
    year_to_be_added = budget_sums.iloc[0: i+1, :]

    bar = alt.Chart(year_to_be_added).mark_bar().encode(
        x=alt.X('Release_Year:O', title='Release Year'),
        y=alt.Y('sum_budget:Q', title='Total Budget'),
    ).interactive()

    # Create the line chart
    line = alt.Chart(year_to_be_added).mark_line(color='red').encode(
        x=alt.X('Release_Year:O', title='Release Year'),
        y=alt.Y('rolling_mean:Q', title='Rolling Mean of Total Budget')
    ).interactive()

    time.sleep(0.05)

    chart.altair_chart(bar+line)

df = load_data()

df['Release_Year'] = df['Release_Year'].astype(str)
df['Box_Office_Success'] = pd.Categorical(df['Box_Office_Success'], categories=['Low', 'Medium', 'High'],ordered=True)


grouped_data = df.groupby(['Release_Year', 'Box_Office_Success'])['Budget'].sum().reset_index()
chart = alt.Chart(grouped_data).mark_bar().encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('sum(Budget):Q', title='Total Budget'),
    color=alt.Color('Box_Office_Success', title='Box Office Success', sort=['High', 'Medium', 'Low'])
).properties(
    width=600,
    title='Total Budget and Box Office Success by Release Year'
)


st.altair_chart(chart)

budget_sums = df.groupby('Release_Year')['Marketing_Spend'].sum().reset_index(name='sum')
budget_sums['bos_percent']=df.groupby('Release_Year')['Box_Office_Success'].size()
budget_sums['rolling_mean'] = budget_sums['sum'].rolling(window=10, min_periods=1).mean()

bar = alt.Chart(budget_sums).mark_bar().encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('sum:Q', title='Marketing Spend')
)

# Create the line chart
line = alt.Chart(budget_sums).mark_line(color='red').encode(
    x=alt.X('Release_Year:O', title='Release Year'),
    y=alt.Y('rolling_mean:Q', title='Rolling Mean of Marketing Spend')

)

# Combine the charts
chart = (bar + line).properties(width=600,
    title='Marketing Spend and Box Office Success by Release Year')

# Display the chart using Streamlit
st.altair_chart(chart)
