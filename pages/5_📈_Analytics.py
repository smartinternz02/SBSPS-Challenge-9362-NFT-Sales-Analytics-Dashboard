import streamlit as st 
import pandas as pd
import plotly_express as px  
import requests 
import json  

st.set_page_config(layout = 'wide') 


key = "4d61f4c5-3032-4d63-bce5-c8bcfef4ba50" 
url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" 

headers = {
    "accept":"application/json", 
    "X-CMC_PRO_API_KEY":key
}

st.sidebar.write("Select Category: ") 
category = st.sidebar.selectbox('Filter : ',["Analysis Graph","Maps"])  


if category == "Analysis Graph":
    dataset = st.sidebar.selectbox("Select Data : ", ["Top NFTs","History Sales"]) 

    if dataset == "Top NFTs":
        top_collection = pd.read_csv("./Dataset/NFT_Top_Collections.csv") 
        #st.write(top_collection)
        values = st.sidebar.multiselect("Name: ",options = top_collection['Name'].unique()) 

        if len(values) == 0:
            #floor_price = px.histogram(top_collection,x=top_collection['Name'],y=top_collection['Floor_Price']) 
            reference = st.sidebar.selectbox('Select Data Reference:',['Floor_Price','Average_Price','Volume','Sales','Owners'])  
            for i in range(0,600,100):
                 st.bar_chart(top_collection[i:i+100],x='Name',y=reference,use_container_width=True) 

            #st.plotly_chart(floor_price) 
            
        else:
            st.write("# :bar_chart: Analytics Dashboard")  
            for value in values:
                st.markdown("---") 
                collection_selection = top_collection.query(f'Name == @value')  
                st.markdown(f"## {value}")   
                st.write(collection_selection) 
                # avg_sales = px.bar(collection_selection,collection_selection['Market_Cap']) 
                # avg_sales.add_bar(collection_selection,)  
                # st.plotly_chart(avg_sales)  
                # st.write(collection_selection)
                #analysis = px.histogram(collection_selection,collection_selection['Volume'],collection_selection['Owners'])     
                st.bar_chart(collection_selection,x='Name',y=['Volume','Floor_Price','Sales'])             
                #st.plotly_chart(analysis)  


    if dataset == "History Sales":
        history_sales = pd.read_csv("./Dataset/NFT_Sales_History.csv") 
        #st.dataframe(history_sales)   
        st.markdown("# Historical Sales Analysis") 
        left_column,right_column = st.columns(2)  
        st.bar_chart(history_sales,x='Date',y=['AverageUSD_cum'])  
        st.bar_chart(history_sales,x = 'Date', y='Number_of_Sales')   
        st.area_chart(history_sales,x = 'Date',y = ['Primary_Sales_cumsum','Secondary_Sales_cumsum'])     
  



def format_map(row):
    res = st.markdown(f"""
        <div class = 'box' style = "display:flex; justify-content:space-around; align-items:center; margin:20px; border:2px solid white; border-radius:20px; padding:20px;">  
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
        <div class = 'box' style = "display:flex; justify-content:space-around; align-items:center;margin:20px; border-bottom:2px solid white; border-radius:0px; padding:20px;">  
            <span style = "font-weight:1000; font-size:30px;">ID</span><span style = "font-weight:1000; font-size:30px;">Name</span><span style = "font-weight:1000; font-size:30px;">SIGN</span><span style = "font-weight:1000; font-size:30px;">SYMBOL</span> 
        </div> 
    """,unsafe_allow_html=True) 

    for row in data:
        res = format_map(row)
        try:  
            st.write(res)
        except:
            pass   




# def format_latest(row):
#     res = st.markdown("""
#         <div class = 'container' style = "display:flex; ">
            
#         </div> 
#     """,unsafe_allow_html=True)

# if category == "Listings Latest":
#     url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"  
#     r =  requests.get(url,headers = headers) 
#     response = r.json()
#     st.write(r.json()) 
#     data = response['data'] 
#     for row in data:
#         res = format_latest(row)
#         st.write(res) 

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