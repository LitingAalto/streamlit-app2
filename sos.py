import streamlit as st
import numpy as np
import datetime
import pandas as pd                        
import plotly.express as px
import matplotlib.pyplot as plt
import warnings
import time
import math
warnings.filterwarnings("ignore") 
from pytrends.request import TrendReq
pytrend = TrendReq()
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Share Of Search</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: darkgrey;'>Automates search and save the needed keywords for modelling</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    start = st.date_input(
    "start date of comparison",
    datetime.date(2020, 7, 6))
    end = st.date_input(
        "end date of comparison",
        datetime.date(2022, 7, 6))
    duration = str(start)+' '+str(end)
with col2:
    group = st.selectbox(
    'How would you like The data to be aggregated?',
    ('Monthly', 'Weekly'))
with col3:
    if group =='Monthly':
        sm = st.selectbox(
        'How would you like to smooth data?',
        ('No', 'Yes, moving average 12m'))
    else:
        sm = st.selectbox(
        'How would you like to smooth data?',
        ('No', 'Yes, moving average 1m'))
    smoothing = False
    if sm != 'No':
        smoothing = True


st.markdown("<h5 style='text-align: left; color: black;'>\nInput here keywords and their afflixes for SoS comparison</h1>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
kw_dict = {}
with col1:
    word = st.text_input('Key Word1', value = "Elisa Samsung Galaxy")
    afflix = st.text_input('Afflix1', value = "Elisa Phone")
    kw_dict[word]=afflix
with col2:
    word = st.text_input('Key Word2', value = "Telia Samsung Galaxy")
    afflix = st.text_input('Afflix2', value = "Telia Phone")
    kw_dict[word]=afflix
with col3:
    word = st.text_input('Key Word3', value = "Elisa 5G liittymä")
    afflix = st.text_input('Afflix3', value = "Elisa")
    kw_dict[word]=afflix
with col4:
    word = st.text_input('Key Word4', value = "Saunalahti 5G liittymä")
    afflix = st.text_input('Afflix4', value = "Elisa")
    kw_dict[word]=afflix
with col5:
    word = st.text_input('Key Word5', value = "Elisa 5G")
    afflix = st.text_input('Afflix5', value = "Elisa")
    kw_dict[word]=afflix
with col6:
    word = st.text_input('Key Word6', value = "DNA 5G liittymä")
    afflix = st.text_input('Afflix6', value = "DNA")
    kw_dict[word]=afflix
with col7:
    word = st.text_input('Key Word7', value = "DNA 5G")
    afflix = st.text_input('Afflix7', value = "DNA")
    kw_dict[word]=afflix
with col8:
    word = st.text_input('Key Word8', value = "")
    afflix = st.text_input('Afflix8', value = "")
    kw_dict[word]=afflix

with st.expander("Input more Keywords"):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        word = st.text_input('Key Word9')
        afflix = st.text_input('Afflix9')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word16')
        afflix = st.text_input('Afflix16')
        kw_dict[word]=afflix
    with col2:
        word = st.text_input('Key Word10')
        afflix = st.text_input('Afflix10')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word17')
        afflix = st.text_input('Afflix17')
        kw_dict[word]=afflix
    with col3:
        word = st.text_input('Key Word11')
        afflix = st.text_input('Afflix11')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word18')
        afflix = st.text_input('Afflix18')
        kw_dict[word]=afflix
    with col4:
        word = st.text_input('Key Word12')
        afflix = st.text_input('Afflix12')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word19')
        afflix = st.text_input('Afflix19')
        kw_dict[word]=afflix
    with col5:
        word = st.text_input('Key Word13')
        afflix = st.text_input('Afflix13')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word20')
        afflix = st.text_input('Afflix20')
        kw_dict[word]=afflix
    with col6:
        word = st.text_input('Key Word14')
        afflix = st.text_input('Afflix14')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word21')
        afflix = st.text_input('Afflix21')
        kw_dict[word]=afflix
    with col7:
        word = st.text_input('Key Word15')
        afflix = st.text_input('Afflix15')
        kw_dict[word]=afflix
        st.text(" ")
        word = st.text_input('Key Word22')
        afflix = st.text_input('Afflix22')
        kw_dict[word]=afflix
        

kw_dict = {k: v for k, v in kw_dict.items() if v!=''}
search = list(kw_dict.keys())

@st.cache
def keywords_list(search):
    df=pd.DataFrame()
    search1 = search.copy()
    while len(search)>1:
        time.sleep(5)
        pytrend.build_payload(search[:5], cat=0, timeframe=duration, geo='FI', gprop='')
        df1 = pytrend.interest_over_time().reset_index().drop('isPartial',1)
        df = pd.concat([df1.drop('date',1), df] ,1)  
        search = list(set(search)-set(search[:5]))
        time.sleep(5)
    s = (df == 0).astype(int).sum(axis=0).sort_values(ascending=True).index[:math.ceil((len(search1)-1)/4)-1]
    search1 = list(set(search1)-set(s))
    if len(s) == 0:
        return [search1]
    elif len(s) == 1:
        return [search1[:4]+[s[0]],[s[0]]+search1[4:]]
    elif len(s) == 2:
        return [search1[:4]+[s[0]],[s[0]]+search1[4:7]+[s[1]],[s[1]]+search1[7:]]
    elif len(s) == 3:
        return [search1[:4]+[s[0]],[s[0]]+search1[4:7]+[s[1]],[s[1]]+search1[7:10]+[s[2]],[s[2]]+search1[10:]]
    elif len(s) == 4:
        return [search1[:4]+[s[0]],[s[0]]+search1[4:7]+[s[1]],[s[1]]+search1[7:10]+[s[2]],[s[2]]+search1[10:13]+[s[3]],[s[3]]+search1[13:]]

def merge2df(df1, df2):
    df=df1.merge(df2, on='date')
    df['trans']=df[df.filter(regex='_x').columns].values/df[df.filter(regex='_y').columns].values
    df['trans']=df['trans'].fillna(df['trans'].mean())
    for col in df.columns[df2.shape[1]-1:]:
        if col != 'trans':
            df[col] = df['trans']*df[col]
            df[col] = df[col].fillna(0).apply(lambda x: int(round(x,0)))
    df.drop(df.filter(regex='_y').columns,1, inplace=True)
    df.columns = [ x.split('_x')[0] for x in df.columns]
    return df.drop('trans',1)

@st.cache
def sos_calculator(search,duration,group, smoothing):
    df=pd.DataFrame()
    ll = keywords_list(search)
    for keywords in ll:
        pytrend.build_payload(keywords, cat=0, timeframe=duration, geo='FI', gprop='')
        df1 = pytrend.interest_over_time().reset_index().drop('isPartial',1)
        if df.shape[0]>0:
            df = merge2df(df, df1)
        else:
            df = df1.copy()
  
    if group == 'Weekly':
        if smoothing:
            df1 = df.rolling(4).mean()
            df1['date']=df['date']
            df=df1.dropna()
    else:
        df['date']=df['date'].dt.to_period('M').astype('str')
        df = df.groupby('date')[search].mean().reset_index().dropna()
        if smoothing:
            df1 = df.rolling(12).mean().dropna()
            df1['date']=df['date']
            df=df1.dropna()
    df=df.set_index('date')
    df.columns=df.columns.map(kw_dict)
    df = df.groupby(lambda x:x, axis=1).sum().reset_index()
    return df
if st.button('Calculate SoS'):
    
    df = sos_calculator(search,duration,group, smoothing)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.line(df, x="date", y=list(kw_dict.values()), title='Share of Search Over Time')
        #fig.show()
        st.plotly_chart(fig, use_container_width=True)
#         if st.button('Save keywords for reporting and modeling'):
        with open('report.txt','a') as f:
            f.write(str(kw_dict)+'\n')
    with col2:
        df1=pd.DataFrame()
        df1['share']=(df.mean()/(df.mean().sum())).values
        df1['names']=(df.mean()/(df.mean().sum())).index
        fig1 = px.pie(df1, values='share', names='names', title='Share of Search in %',hole=.65)
        #fig1.show()  
        st.plotly_chart(fig1, use_container_width=True)
    
with st.expander('Add Dates to compare change of SoS'):
    start1 = st.date_input(
    "start date of the added comparison",
    datetime.date(2020, 7, 6))
    end1 = st.date_input(
        "end date of the added comparison",
        datetime.date(2022, 7, 6))
    duration1 = str(start1)+' '+str(end1)
    df = sos_calculator(search,duration,group, smoothing)
    dfn = sos_calculator(search,duration1,group, smoothing)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.line(df, x="date", y=list(kw_dict.values()), title='Share of Search Over Time')
        
        df1=pd.DataFrame()
        df1['share']=(df.mean()/(df.mean().sum())).values
        df1['names']=(df.mean()/(df.mean().sum())).index
        fig1 = px.pie(df1, values='share', names='names', title='Share of Search in %',hole=.65)
        st.plotly_chart(fig, use_container_width=True) 
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig3 = px.line(dfn, x="date", y=list(kw_dict.values()), title='Share of Search Over Time')
        df1=pd.DataFrame()
        df1['share']=(dfn.mean()/(dfn.mean().sum())).values
        df1['names']=(dfn.mean()/(dfn.mean().sum())).index
        fig4 = px.pie(df1, values='share', names='names', title='Share of Search in %',hole=.65)
        st.plotly_chart(fig3, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)
