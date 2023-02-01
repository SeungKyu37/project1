# 홈

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.title('내방 어디?')

from search import run_search
from predict import run_predict
from suggestions import run_suggestions

selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색",  "📊전세 시세 예측", '💬건의사항'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)

# 홈 탭
if selected3 == "🏠Home":
    st.subheader('홈페이지')
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    st.write(data.head())

# 전월세 검색 탭
elif selected3 == "🔎전월세 검색":
    run_search()

# 전세 시세 예측 탭 
elif selected3 == "📊전세 시세 예측":
    run_predict()

# 건의사항 탭
elif selected3 == "💬건의사항":
    run_suggestions()
else:
    selected3 == "🏠Home"
