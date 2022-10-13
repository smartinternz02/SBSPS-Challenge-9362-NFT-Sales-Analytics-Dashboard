import streamlit as st 
import requests 
import json 

API = "pub_11616c40ecb72c98f6bf758c161ce92999576" 
URL = f"https://newsdata.io/api/1/news?apikey={API}" #&language=en&country=in"   

params = {
    'language':'en',
    'country':'in', 
    'q':None , 
    'qInTitle':None  
}

st.markdown("""
    <header style = "text-align:center; letter-spacing:2px"> 
        <h2>Get Instant NFT NEWS</h2> 
        <h4>Right in your FEED !! </h4> 
    </header>
""",unsafe_allow_html=True)  

st.write("---") 
st.sidebar.write("---") 
block = st.sidebar.selectbox("Select Crypto",['Bitcoin',"Ethereum","DogeCoin"])  
st.sidebar.write("---") 
query_title = st.sidebar.text_input("Search Query Title: ")  


if(block): 
    params['q'] = block 
    params['qInTitle'] = None 


if(query_title and not query_title.isspace()): 
    params['qInTitle'] = query_title
    params['q'] = None 
 

response = requests.get(URL,params = params).json()
#st.write(response)

def format_news(result): 
    st = f"""
        <div class = 'container' style = "display:flex; flex-direction:column; align-items:center; text-align:center; gap:50px">    
            <header>
                <h1>{result['title']}</h1> 
            </header>
            <div class = 'content'>
                <p>{result['content'][:700] if result['content'] !=None else None}....</p>      
                ....Read More <a href = "{result['link']}" >{result['link']}</a>
            </div>  
            <footer style = "display:flex; flex-direction:row; justify-content:space-between; align-items:center; width:70%">  
                <span><b><i>{result['pubDate']}</i></b></span> 
                <span style = "font-size:25px; font-weight:1000">--{' '.join(i+' , ' for i in result['creator']) if result['creator']!= None else " "}</span>   
            </footer>
        </div>
    """ 

    return st 

for i in range(len(response['results'])):
    st.markdown(f"""
        {format_news(response['results'][i])}
        ---  
    """,unsafe_allow_html=True)  

