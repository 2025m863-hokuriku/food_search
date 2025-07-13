#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


combine_df = pd.read_csv("combine.csv")


# In[4]:


st.title("ラーメン屋・サーチ")

price_limit = st.slider("最低価格の上限", min_value=500, max_value=6000, step=200, value=999)
point_limit = st.slider("ポイントの下限", min_value=0.0, max_value=20.0, step=0.2, value=3.0)


# In[7]:


filtered_df = combine_df[
    (combine_df['price'] <= price_limit) & 
    (combine_df['point'] >= point_limit)
]


# In[12]:


fig = px.scatter(
    filtered_df,
    x='point',
    y='price',
    hover_data=['name_food', 'price', 'comment', 'collect', 'point'],
    title='ポイントと最低カット価格の散布図'
)

st.plotly_chart(fig)


# In[14]:


selected_food = st.selectbox('気になるラーメン店を選んで詳細を確認', filtered_df['name_food'])

if selected_food:
    url = filtered_df[filtered_df['name_food'] == selected_food]['link_food'].values[0]
    st.markdown(f"[{selected_food} のページへ移動]({url})", unsafe_allow_html=True)


# In[15]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("point","score_food","comment","price","collect")
)

ascending = True if sort_key == "point" else False


# In[17]:


st.subheader(f"{sort_key} )によるラーメン店ランキング（上位10件）")

ranking_df = filtered_df.sort_values(by=sort_key,ascending=ascending).head(10)

st.dataframe(ranking_df[["name_food","price","point","score_food","comment","collect","location","phone"]])


# In[ ]:




