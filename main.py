import streamlit as st
import os
import json
import pandas as pd
import requests


string_data = False
API_ENDPOINT2= "https://ynu1ow7ibh.execute-api.eu-central-1.amazonaws.com/vectordb"

st.markdown("<h1 style='text-align: center; color:  #d68910;'>Vector Database </h1>", unsafe_allow_html=True)
question_area = st.text_input("Project ID")
#temp = st.slider("Temeperature", 0, 10, 1)
country = st.selectbox("Country", ["None", "United States", "China", "Japan", "Germany", "United Kingdom"])
inds = st.selectbox("Industry", ["None","Consumer Goods & Services", "Energy & Utilities", \
                          "Financials & Real Estate", "Health Care", \
                            "Industrial & Transportation", \
                                "Materials & Natural Resources", "Public Policy", "Technology & Telecommunication", "Other"])
office = st.selectbox("Atheneum_office", ["None", "China", "London", "Berlin", \
                                        "Munich", "Shanghai", "Lahore", \
                                        "New York", "San Francisco", "Santiago", "Tokyo"])
proj = st.selectbox("Project_type", ["None","Expert Backed Research", "Expert Sessions", "Expert Placement", "Expert Survey Research"])
top_number = st.slider("Top_k", 1, 10, 1)

if string_data:
    question_area=string_data
   
try:
    if st.button('Send') and question_area is not "":
        res = requests.post(API_ENDPOINT2, json={"project_id": question_area, "country" : country , 
                                                 "industry" : inds, "project_type" : proj, "top_number" : top_number, "office": office})
        df=pd.DataFrame(res.json()["Results"])
        df["projectid"] = df["projectid"].astype(str).str.replace(".0000", "").astype(float)
        df["projectid"] = df["projectid"].astype('int64')
        df["Text"] = res.json()["Text"].values()
        st.dataframe(df, width=800)
except Exception as e:
    st.text_area("Error", height=200, value ="No results, please try a different combination of filters or project id.\n Thank You!!!", disabled=True)
