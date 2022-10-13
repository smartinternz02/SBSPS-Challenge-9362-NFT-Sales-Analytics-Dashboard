import streamlit as st 
import pandas as pd
import numpy as np
import json


# st.title("NFT Analysis and Visualization") 

st.set_page_config(page_title = "Top Charts")   

top_collection = pd.read_csv('Dataset/NFT_Top_Collections.csv') 

top_collection = pd.DataFrame(top_collection) 


st.markdown("""
    <h1 style ="width"100%; text-align:center; align-items:center; letter-spacing:20px">Top NFTs in current Trend</h1>   
""",unsafe_allow_html=True) 

# st.subheader("Raw NFT Data : ") 
# st.write(top_collection) 

# st.write(top_collection.describe()) 

#<=============================================>  CONTAINER APPEND IN JAVASCRIPT <============================>

st.markdown('''

<script type = 'text/javascript' defer>
function html_renderer(Index,Name,logo_url,volume,floor_price){ 

    st = `
    <div style = "border:2px solid white; padding:20px; margin:20px; background:#222;  border-radius:30px; display:flex; flex-direction:column; align-items:center; text-align:center;">      
        <div style = "display:flex; align-items:center; justify-content:space-around; width:100%"><h2>${Index+1} ) ${Name}</h2></div>
        <div style = "display:flex; align-items:center; justify-content:space-between; padding:10px width:100%">     
            <img src = ${logo_url} height = "200px" style = "border:2px solid white; border-radius:20px; margin:20px" /> 
            <div style = "display:flex; flex-direction:column; text-align:center; max-width:50% "><h3>Category:</h3><span style = "word-wrap:break-word; font-size:25px;">category</span></div>   
        </div> 
        <div style = "display:flex; flex-direction:row ; justify-content:center; align-items:space-around; width:100%">
            <h4>Volume : ${volume}</h4> 
            <h4>Floor Price :${floor_price}</h4> 
        </div>    
    </div> 
    `

    return st
    }
</script> ''' 
,unsafe_allow_html=True);  

st.markdown("""
    <div class = 'container' style = "display:flex; flex-direction:row; gap:50px; align-items:center; justify-content:center; width:100%; flex-wrap:wrap"> 
""",unsafe_allow_html = True)


def container_append(Index,Name,logo_url,volume,floor_price,Category):

    st.markdown(f"""
            <script type = "text/javascript" defer> 
                var container = document.querySelector('.container'); 
                ren = html_renderer({Index},{Name},{logo_url},{volume},{floor_price},{Category}); 
                container.appendChild(ren)  
            </script> 
        </div>  
    """,unsafe_allow_html=True)

#<===============================================================================================================================================================>


def html_renderer(Index,Name,logo_url,volume,floor_price,Category = None):
    if Category:  
        category =  json.dumps(Category).split(',') 
        category = category[:3]  
    st = f"""
    <div style = "border:2px solid white; padding:20px; margin:20px; background:#222;  border-radius:30px; display:flex; flex-direction:column; align-items:center; text-align:center;">      
        <div style = "display:flex; align-items:center; justify-content:space-around; width:100%"><h2 style = "text-transform:uppercase">{Index+1} ) {Name}</h2></div>
        <div id = 'imgbox{Index}' style = "display:flex; align-items:center; justify-content:space-between; padding:10px width:100%">     
            <img src = {logo_url} height = "200px" style = "border:2px solid white; border-radius:20px; margin:20px" /> 
            <div style = "display:flex; flex-direction:column; text-align:center; max-width:50% "><h3>Category:</h3><span style = "word-wrap:break-word; font-size:25px;">{' '.join(i+" , " for i in category) if category != None else None}</span></div>   
        </div> 
        <div style = "display:flex; flex-direction:row ; justify-content:center; align-items:space-around; width:100%">
            <h4>Volume : {volume}</h4> 
            <h4>Floor Price : {floor_price}</h4> 
        </div>    
    </div> 
    """

    return st 

display_size = 10
st.sidebar.write("---") 
display_size_input = st.sidebar.text_input("Enter Display Size : (LIMIT : 500)")   
st.sidebar.write("---") 
track = 0

display_size = int(display_size_input) if display_size_input else display_size 
pointer = 0 
while track < display_size and display_size < 500: 
    logo = top_collection['Logo'][pointer] 
    if(type(logo) == str and logo.endswith('jpg')):   
        #if(logo.endswith('png')):
        #    logo.replace('png','jpg')     
        track += 1 
        st.markdown(f"{html_renderer(int(top_collection['Index'][pointer]),top_collection['Name'][pointer],logo,top_collection['Volume'][pointer],top_collection['Floor_Price'][pointer],top_collection['Category'][pointer])}",unsafe_allow_html=True)
        #container_append(int(top_collection['Index'][pointer]),top_collection['Name'][pointer],logo,top_collection['Volume'][pointer],top_collection['Floor_Price'][pointer],top_collection['Category'][pointer])
    pointer += 1
