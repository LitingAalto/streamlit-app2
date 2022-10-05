import streamlit as st
import numpy as np
import datetime
import pandas as pd                        
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import time
import math
import xlsxwriter
from datetime import date
from io import BytesIO
warnings.filterwarnings("ignore") 
from pytrends.request import TrendReq
pytrend = TrendReq()
<<<<<<< HEAD
=======
# from pytrends.request import TrendReq as UTrendReq
# GET_METHOD='get'
>>>>>>> 91994c4b8dd873fcbb05614201d7a7299f905086

# import requests

# headers = {
#     'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#     'Referer': 'https://trends.google.com/',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
# }


class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)
    
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Google Trends</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: darkgrey;'>Automates search and save the needed keywords for modelling</h2>", unsafe_allow_html=True)
keyw = pd.read_excel('keywordlist.xlsx').drop('Unnamed: 0',1)

start = st.date_input(
"start date of comparison",
datetime.date(2020, 10, 1))
end = st.date_input(
    "end date of comparison",
    date.today())
duration = str(start)+' '+str(end)



st.markdown("<h5 style='text-align: left; color: black;'>\nInput here keywords and their afflixes for Google trends comparison</h1>", unsafe_allow_html=True)

category = st.text_input('Category name for the keywords set for search', value = 'Mobiililaajakaistaliittymät')
st.text(" ")

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
kw_dict = {}
with col1:
    word = st.text_input('Key Word1', value = "Elisa mobiililaajakaista")
    afflix = st.text_input('Afflix1', value = "Elisa")
    kw_dict[word]=afflix
with col2:
    word = st.text_input('Key Word2', value = "Saunalahti mobiililaajakaista")
    afflix = st.text_input('Afflix2', value = "Elisa")
    kw_dict[word]=afflix
with col3:
    word = st.text_input('Key Word3', value = "DNA mobiililaajakaista")
    afflix = st.text_input('Afflix3', value = "DNA")
    kw_dict[word]=afflix
with col4:
    word = st.text_input('Key Word4', value = "Telia mobiililaajakaista")
    afflix = st.text_input('Afflix4', value = "Telia")
    kw_dict[word]=afflix
with col5:
    word = st.text_input('Key Word5', value = "Sonera mobiililaajakaista")
    afflix = st.text_input('Afflix5', value = "Telia")
    kw_dict[word]=afflix
with col6:
    word = st.text_input('Key Word6', value = "Moi mobiililaajakaista")
    afflix = st.text_input('Afflix6', value = "Moi")
    kw_dict[word]=afflix
with col7:
    word = st.text_input('Key Word7')
    afflix = st.text_input('Afflix7')
    kw_dict[word]=afflix
with col8:
    word = st.text_input('Key Word8')
    afflix = st.text_input('Afflix8')
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

<<<<<<< HEAD
def merge2df(df1, df2):
    df=df1.merge(df2, on='date')
    df['trans']=df[df.filter(regex='_x').columns].values/df[df.filter(regex='_y').columns].values
    df['trans']=df['trans'].fillna(df['trans'].mean())
    for col in df.columns[-(df2.shape[1]-1):-1]:
        if col != 'trans':
            df[col] = df['trans']*df[col]
            df[col] = df[col].fillna(0).apply(lambda x: int(round(x,0)))
    df.drop(df.filter(regex='_y').columns,1, inplace=True)
    df.columns = [ x.split('_x')[0] for x in df.columns]
    return df.drop('trans',1)

def keywords_list(kw_dict, duration = duration):
=======
@st.cache
def keywords_list(search):
>>>>>>> 91994c4b8dd873fcbb05614201d7a7299f905086
    df=pd.DataFrame()
    search1 = search = list(kw_dict.keys())
    while len(search)>1:
        time.sleep(3)
        pytrend.build_payload(search[:5], cat=0, timeframe=duration, geo='FI', gprop='')
        df1 = pytrend.interest_over_time().reset_index().drop('isPartial',1)
        df = pd.concat([df1.drop('date',1), df] ,1)      
        search = list(set(search)-set(search[:5]))
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


<<<<<<< HEAD
def sos_calculator(kw_dict, duration=duration, category = category):
    df=pd.DataFrame()
    for keywords in keywords_list(kw_dict, duration = duration):
=======
@st.cache
def sos_calculator(search,duration,group, smoothing):
    df=pd.DataFrame()
    ll = keywords_list(search)
    for keywords in ll:
>>>>>>> 91994c4b8dd873fcbb05614201d7a7299f905086
        pytrend.build_payload(keywords, cat=0, timeframe=duration, geo='FI', gprop='')
        df1 = pytrend.interest_over_time().reset_index().drop('isPartial',1)
        if df.shape[0]>0:
            df = merge2df(df, df1)
        else:
            df = df1.copy()
    
    df=df.set_index('date')
    df0 = df.copy()
    df2 = df0.reset_index()
    df2['date']=df2['date'].dt.to_period('M').astype('str')
    dfm = df2.groupby('date').mean().dropna()
    
    df.columns=df.columns.map(kw_dict)
    df = df.groupby(lambda x:x, axis=1).sum()
    df2 = df.reset_index()
    df2['date']=df2['date'].dt.to_period('M').astype('str')
    df2 = df2.groupby('date').mean().dropna() # monthly agg
    return df0.reset_index(), dfm.reset_index(), df2.reset_index()

if st.button('Calculate Google trends'):
    df_weekly, df_monthly, df = sos_calculator(kw_dict,duration, category = category )
    col1, col2 = st.columns(2)
    with col1:
        fig = px.line(df, x="date", y=list(kw_dict.values()), title='Share of Search Over Time (Monthly aggregated)')
        
        st.plotly_chart(fig, use_container_width=True)
        ax = sns.lineplot(data=df.set_index('date'))
        plt.xticks(rotation=90)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True)
        plt.savefig("python.png")
        
#         if st.button('Save keywords for reporting and modeling'):
#         with open('report.txt','a') as f:
#             f.write(str(kw_dict)+'\n')
    with col2:
        df1=pd.DataFrame()
        df1['share']=(df.mean()/(df.mean().sum())).values
        df1['names']=(df.mean()/(df.mean().sum())).index
        fig1 = px.pie(df1, values='share', names='names', title='Share of Search in %',hole=.65)
        #fig1.show()  
        st.plotly_chart(fig1, use_container_width=True)
        

<<<<<<< HEAD
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_weekly.to_excel(writer, index=False, sheet_name='weekly_orign')
        df_monthly.to_excel(writer, index=False, sheet_name='monthly_orign')
        workbook = writer.book
        worksheet = workbook.add_worksheet("Plot(Monthly aggregated)")
        worksheet.insert_image('B2', 'python.png', {'x_offset': 15, 'y_offset': 1})
        writer.save()
        processed_data = output.getvalue()
        return processed_data
    df_xlsx = to_excel(df)
    file = st.text_input('Name your file', value='5G google trends')
    st.download_button(label='📥 Download trends data from the selected keywords',
                                    data=df_xlsx ,
                                    file_name= f'{file}.xlsx')
if st.button('♞ Add current keywords to BI reports! Be sure you add the right one, once it is added, it will be in reporting'):
    def keyword_excel(kw_dict, cat):
        df = pd.DataFrame(kw_dict.items(), columns=['keywords','afflix'])
        df['category'] = cat
        df['flag'] = 0
        return df
    if category not in keyw.category.unique():
        keyw = keyw.append(keyword_excel(kw_dict, category))
        keyw.to_excel('keywordlist.xlsx')
    else:
        st.markdown("<h5 style='text-align: left; color: black;'>\nCategory already exists, input a new one and add again!</h5>", unsafe_allow_html=True)
def to_excel2(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    keyw.to_excel(writer, index=False, sheet_name='keywords')
    writer.save()
    processed_data = output.getvalue()
    return processed_data
df_xlsx = to_excel2(keyw)
st.download_button(label='Download keywords lists for BI report',
                                data=df_xlsx ,
                                file_name= 'keywordlist.xlsx')
=======
    with col2:
        fig3 = px.line(dfn, x="date", y=list(kw_dict.values()), title='Share of Search Over Time')
        df1=pd.DataFrame()
        df1['share']=(dfn.mean()/(dfn.mean().sum())).values
        df1['names']=(dfn.mean()/(dfn.mean().sum())).index
        fig4 = px.pie(df1, values='share', names='names', title='Share of Search in %',hole=.65)
        st.plotly_chart(fig3, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)
>>>>>>> 91994c4b8dd873fcbb05614201d7a7299f905086
