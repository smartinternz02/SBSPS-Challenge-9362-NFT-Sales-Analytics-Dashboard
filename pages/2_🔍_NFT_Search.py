import streamlit as st
import pandas as pd
import requests 
import json 

st.set_page_config(layout = "wide") 

# st.markdown("""
#     <style>
#         .e1tzin5v0{ 
#             width:70%;  
#             display:grid;  
#             grid-template-columns: 1fr 1fr;   
#         } 
#     </style> 
# """,unsafe_allow_html=True) 

#<==============================>     VENLY POSTMAN AUTHENTICATIOn    <=======================================>   


# client_id =  "Testaccount-capsule"
# secret_id =  "82c19251-1753-44f5-ae76-93438d3628de"                              # VENLY API And KEY 
# application_id =  "3b613051-4e10-479d-a75a-ee355541e5a0"


# url = f"https://login-staging.arkane.network/auth/realms/Arkane/protocol/openid-connect/token"

# payload= f'grant_type=client_credentials&client_id={client_id}&client_secret={secret_id}' 
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded'
# }

# response = requests.request("POST", url, headers=headers, data=payload).json()

# st.write(response)  


#<==============================================================================================================================>



#URL = 'https://api.blockspan.com/v1/nfts' #"https://api.opensea.io/api/v1/assets"      #blockspan  # "S2HC5tAf5ZXyJUS6RAQhzguHVCFkTm09"

# MORALIS - 5EvfeDpypIin2PATbpk3HA76XMZsIBRaIgtw0PPujj6KdkkyngnuFlGuzhnoJG0P



#API = "5EvfeDpypIin2PATbpk3HA76XMZsIBRaIgtw0PPujj6KdkkyngnuFlGuzhnoJG0P"  ## Moralis  
## API = "S2HC5tAf5ZXyJUS6RAQhzguHVCFkTm09"  ## Blockspan


#<==================> HEADER FILES FOR MORALIS API <=========================>

moralis_headers = {
    'accept':'application/json' ,
    'X-API-KEY' : "5EvfeDpypIin2PATbpk3HA76XMZsIBRaIgtw0PPujj6KdkkyngnuFlGuzhnoJG0P"
}


#<===============================>  HEADER FILES FOR VENLY API  <============================> 

venly_headers = {
    'accept':'application/json' , 
    'X-API-KEY' : "82c19251-1753-44f5-ae76-93438d3628de"
}




# <=====> NFT METADATA RETRIVAL <===>  

URL = None 

def NFT_Metadata(address,token_id):   
    #  URL = f"https://api-business.venly.io/api/apps/{application_id}/contracts/{contract_id}/token-types/{token_type_id}/metadata"  ## Venly 
    URL = f"https://deep-index.moralis.io/api/v2/nft/{address}/{token_id}" 
    response = requests.get(URL,headers = moralis_headers).json()
    return response  

#  <==========> Retrive NFT based on wallet Address   <========================> 

    
#<=====================================================> GET NFT BY OWNERS  <==========================> 

def NFT_Owners(wallet_address): 
    URL = f"https://deep-index.moralis.io/api/v2/{wallet_address}/nft?chain=eth&format=decimal" 
    response = requests.get(URL,headers = moralis_headers).json()
    return response 



endpoint = st.sidebar.selectbox("Search by", ['-','Query Search','Block','NFT Metadata'])     

if endpoint == '-':
    st.markdown("""
        <header style = "display:flex; align-items:center; justify-content:center; flex-direction:column; gap:20px">  
            <h1>NFT Search Tool </h1> 
            <h3>Retrive MetaData with Known Data 📇</h3>
            <h4 style = "text-align:center">We Provide you the Ultimate Search Filters Right out of the box <br><span style = "color:rgba(255,255,255,0.5)">( literally ! , It's in the sidebar! )</span></h4> 
            <br>
            <marquee behavious = "scroll" width = "100%" scrollamount="30" direction = "left" style = "padding:20px; border:2px solid rgba(255,255,255,0.4); border-radius:50px; font-size:30px; letter-spacing:5px">
                All You need is a Right Piece of Art!! 
            </marquee>
        </header> 

    """,unsafe_allow_html=True)



if endpoint == 'Block':
    
    num = st.text_input("Enter BLock Number or Hash Number: ") 
    URL = f'https://deep-index.moralis.io/api/v2/block/{num}?chain=eth'  ## Moralis
    if num:
        response = requests.get(URL,headers = moralis_headers).json() 

        st.markdown(f"""
            <div class = 'container' style = "display:flex; flex-direction:column; align-items:center; justiify-content:space-between; padding:20px; border:2px solid white; border-radius:30px; gap:20px; margin:30px">    
                <h2><span>Block Number : </span><span>{response['number']}</span></h2> 
                <h3><span>Hash : </span><span>{response['hash']}</span></h2> 
                <h4><span>Sha3-Uncles : </span><span>{response['sha3_uncles']}</span></h4>
                <div style = "display:flex; align-items:center; justify-content:space-between"> 
                <h4><span>Nonce : </span><span>{response['nonce']}</span></h4>
                <h4><span>Difficulty : </span><span>{response['difficulty']}</span></h4>
                </div>
                <h4><span>Miner : </span><span>{response['miner']}</span></h4>
            </div> 
        """,unsafe_allow_html=True)
       # st.write(response) 
        # # if('message' not in response):
        # #     st.markdown(f"""
        # #         ### Hash : {response['hash']} 
        # #         ### Number : {response['number']} 
        # #         ### Nonce  : {response['nonce']} 
        # #         #### Uncle : {response['sha3_uncles']} 
        # #         ### miner : {response['miner']}
        # #     """, unsafe_allow_html=True)

        # else:
        #     st.header(response['message'])  

    else:
         st.markdown("""
            <div style = "display:flex; align-items:center;justify-content:space-between;flex-direction:column; padding:20px; margin-top:10% ; min-height:50%; gap:40px">    
                <h2 style = "align-text:center ; letter-spacing:3px; width:100%; font-weight:1000; line-height:60px">Retrive NFT Info Based on the mined Block Number OR solved Hash Number</h2> 
                <h3>On Entering the query NFT with respective BLOCK Number or HASH Number 
                <h5 style = "letter-spacing:2px"><i>Eg:<br><br> Hash : <u>0xd3.....57d9</u></i><br><br>OR<br><br>BLock : <i>65</i></h5></h3> 
            </div>
        """,unsafe_allow_html = True) 



if endpoint == "NFT Metadata":

    address = st.text_input("Enter NFT Address : ")
    token_id = st.text_input("Enter Token ID: ") 
    if token_id and address: 
        response = NFT_Metadata(address,token_id)
        #st.write(response)     # For Testing Purpose 
        try:
            img_url = json.loads(response['metadata'])['image']  
            st.markdown(f"""
                <div class = 'container' style = "display:flex; flex-direction:column; align-items:center; justiify-content:space-between; padding:20px; border:2px solid white; border-radius:30px; gap:20px; margin:30px">    
                    <h2><span style = "font-size:30px">Name : </span><span style = "font-weight:1000; letter-spacing:5px; margin:20px">{response['name']}</span></h2> 
                    <img src = "{img_url}" height = "200px" style = "border:2px solid white; border-radius:20px"> 
                    <h3><span>Token Address : </span><span><u><i>{response['token_address']}</i></u></span></h2> 
                    <h4><span>Token Hash : </span><span><u><i>{response['token_hash']}</i></u></span></h4>
                    <div style = "display:flex; align-items:center; justify-content:space-between"> 
                    <h4><span>Minted Block Number : </span><span>{response['block_number_minted']}</span></h4>
                    <h4><span>Block Number : </span><span>{response['block_number']}</span></h4>
                    </div>
                    <h4 style = "width:100%; padding:20px;"><span>NFT URL : </span><a href = "{response['token_uri']}" style = "word-wrap:break-word; font-size:20px">{response['token_uri']}</a></h4>
                </div> 
            """,unsafe_allow_html=True)
        except Exception as e:
            "---"
            st.markdown(f"# {response['message']}")  
        
    else:
        st.markdown("""
            <div style = "display:flex; align-items:center;justify-content:space-between;flex-direction:column; padding:20px; margin-top:10% ; min-height:50%; gap:40px">    
                <h2 style = "align-text:center ; letter-spacing:3px; width:100%; font-weight:1000; line-height:60px">Retrive NFT Info Based on Address <i>&</i> Token ID</h2> 
                <h3>On Entering required Query, NFTs with provided Address and Token ID will be Scraped and Displayed 
                <h5 style = "letter-spacing:2px"><i>Eg:<br><br> Address: <u>0xd3.....57d9</u></i><br><br>Token ID : <i>5678</i></h5></h3> 
            </div>
        """,unsafe_allow_html = True)

        


if endpoint == 'Wallet Address': 
    wallet_address = st.text_input("Enter Wallet Address: ") 
    if wallet_address:
        response = NFT_Owners(wallet_address)
        st.write(response)  
    else:
        st.markdown("""
            <div style = "display:flex; align-items:center;justify-content:space-between;flex-direction:column; padding:20px; margin-top:10% ; min-height:50%; gap:40px">    
                <h2 style = "align-text:center ; letter-spacing:3px; width:100%; font-weight:1000; line-height:60px">Retrive NFT Info Based on Owner's Wallet Address</h2> 
                <h3>On Entering required Query, NFTs present in the respective owner-wallet will be displayed
                <h5 style = "letter-spacing:2px"><i>Eg: <u>0xd3.....57d9</u></i></h5></h3> 
            </div>
        """,unsafe_allow_html = True)


#<============================> Query Search <=====================================>

def format_query(result):

    token_id = result['token_id'] 
    token_address = result['token_address'] 
    metadata = json.loads(result['metadata']) 
    description = metadata['description'][:500] if 'description' in metadata else None 
    name = metadata['name'] 
    image = metadata['image']  
    ref_url = metadata['external_url'] if 'external_url' in metadata else None
    block_number = result['block_number_minted'] 
    contract_type = result['contract_type'] 

    st = f"""
        <div class = 'container' style = "display:flex; flex-direction:column; justify-content:center; padding:20px; border:2px solid white; gap:30px; border-radius: 20px; width:50%; transform:translateX(25%); margin:50px">          
            <header style = "width:100%; display:flex; align-items:center; justify-content:center; ">
                <h2 style = "text-align:center; word-wrap:break-word">{name}</h2>   
            </header>
            <div class = 'disp' style = "display:flex; flex-direction:column; justify-content:space-around; align-items:center">    
                <img src="{image}" width="300px" style = "border:2px solid white; border-radius:20px; margin:30px ">       
                <span style="word-wrap:break-word; width:100%; text-align:center; font-size:20px">    
                    {description if description !=None else 'No Description, Just see the Image 😛'}.....  
                </span> 
            </div> 
            <div style = "display:flex; align-items:center; flex-direction:column; justify-content:space-around; width:100%">  
                <span style = "font-size:30px">Block Number : <i>{block_number}</i></span>  
                <span style = "font-style:30px">Contract Type : <b>{contract_type}</b></span> 
            </div> 
            <a href = "{ref_url if ref_url != None else '/NFT_View'}" style = "word-wrap:break-word; text-align:center; width:100%; font-size:20px; display:flex; justify-items:center">{str(ref_url) if ref_url != None else 'No Reference URL for this one'}</a>  
        </div>
    """ 

    return st 



if endpoint == 'Query Search':
    q = st.text_input('Enter Query Srting to search NFT') 
    if(q and not q.isspace()):
        q = q.replace(' ','%20') 
        URL = f'https://deep-index.moralis.io/api/v2/nft/search?chain=eth&format=decimal&q={q}&filter=name' 
        response = requests.get(URL,headers = moralis_headers).json() 
        #st.write(response['result'])  
        for result in response['result']:
            try:
                st.markdown(format_query(result),unsafe_allow_html=True) 
            except:
                pass 
    else:
        st.markdown("""
            <div style = "display:flex; align-items:center;justify-content:space-between;flex-direction:column; padding:20px; margin-top:10% ; min-height:50%; gap:40px">    
                <h2 style = "align-text:center ; letter-spacing:3px; width:100%; font-weight:1000; line-height:60px">Retrive NFT Info Based on Search Query stirng input</h2> 
                <h3>On Entering Search Query String into the above input field , NFTs related to the provided query will be displayed. 
                <h5 style = "letter-spacing:2px"><i>Query : <u>Bored Ape</u></i></h5></h3> 
            </div>
        """,unsafe_allow_html = True)


    
