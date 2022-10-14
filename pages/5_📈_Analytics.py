import streamlit as st 
import requests 
import json  


key = "4d61f4c5-3032-4d63-bce5-c8bcfef4ba50" 
url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" 

headers = {
    "accept":"application/json", 
    "X-CMC_PRO_API_KEY":key
}

st.sidebar.write("Select Category: ") 
category = st.sidebar.selectbox('',["Maps","Trending Gainers&Losers", "Listings Latest"])  


def format_map(row):
    res = st.markdown(f"""
        <div class = 'box' style = "display:flex; justify-content:space-around; align-items:center; margin:50px; border:2px solid white; border-radius:20px; padding:20px;">  
            <span>{row['id']}</span><span>{row["name"]}</span><span>{row['sign']}</span><span>{row['symbol']}</span> 
        </div> 
    """,unsafe_allow_html=True) 
    return res

if category == "Maps": 
    url = "https://pro-api.coinmarketcap.com/v1/fiat/map" 
    r = requests.get(url,headers = headers) 
    response = r.json() 
    data = response['data']

    st.markdown(f"""
        <div class = 'box' style = "display:flex; justify-content:space-around; align-items:center; margin:50px; border-bottom:2px solid white; border-radius:0px; padding:20px;">  
            <span style = "font-weight:1000; font-size:30px;">ID</span><span style = "font-weight:1000; font-size:30px;">Name</span><span style = "font-weight:1000; font-size:30px;">SIGN</span><span style = "font-weight:1000; font-size:30px;">SYMBOL</span> 
        </div> 
    """,unsafe_allow_html=True) 

    for row in data:
        res = format_map(row)
        try:  
            st.write(res)
        except:
            pass   

if category == "Trending Gainers&Losers":
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers" 

if category == "Listings Latest":
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"  
    r =  requests.get(url,headers = headers) 
    st.write(r.json()) 

#currency = st.sidebar.selectbox("Conversion Currency: ", ['USD','INR']) 

# if currency == "USD":
#     url+="?convert=USD" 

# if currency == "INR":
#     url+="?convert=INR" 

  


# endpoint = st.sidebar.selectbox("Type FIlter:",['Floor Price']) 

# if(endpoint == 'Floor Price'):
#     URL = "https://api.howrare.is/v0.1/floor" 
#     headers = {
#         'accept':'application/json'
#     } 

#     response = requests.get(URL,headers = headers).json()
#     st.write(response) 