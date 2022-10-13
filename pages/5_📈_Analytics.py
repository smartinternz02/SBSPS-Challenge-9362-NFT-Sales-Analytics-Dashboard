import streamlit as st 
import requests 

endpoint = st.sidebar.selectbox("Type FIlter:",['Floor Price']) 

if(endpoint == 'Floor Price'):
    URL = "https://api.howrare.is/v0.1/floor" 
    headers = {
        'accept':'application/json'
    } 

    response = requests.get(URL,headers = headers).json()
    st.write(response) 
