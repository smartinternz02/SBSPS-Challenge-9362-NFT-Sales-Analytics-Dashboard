import streamlit as st
import base64


st.set_page_config(page_title = "NFT - Home Page", layout="wide") 

def get_base64(img_path): 
    with open(img_path,'rb') as f: 
        data = f.read()
    return base64.b64encode(data).decode() 

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#set_background('./bg.jpg')  


st.markdown(f"""
    
    <header style = "padding:none; margin:none; box-sizing:border-box"> 
        <div class = 'logo' style = "display:flex; flex-direction:column;align-items:flex-start;justify-content:center; padding:none;margin:none; padding:none; height:max-content">      
            <h1 style = "position:relative; ">CryptoKnights</h1> 
            <h6 style = "position:relative; bottom:0px; left:0%; transform:translateX(50%)">Your NFT Mentor</h6> 
        </div> 
    </header>

    <div class = 'container' style = "width:100%; display:flex; flex-direction:column;text-align:center; align-items:center; justify-content:space-around; margin:50px">    
          <h2 style = "margin-bottom:50px">The Ultimate Analytics Tool to analyize your data</h2>
          <div class = 'box' style = "display:flex; flex-direction:row; align-items:center; justify-content:space-around; width:100%">   
            <div class = 'right' style = "width:40%; padding:30px"> 
                <h2>What is NFT ANalytics Dashboard?</h2><br>
                <h4 style = "word-wrap:break-word"> NFT data analytics dashboard provides a rundown of the NFT collections and the fluctuations in their floor price. This allows investors to track trends within the NFT sphere and gauge the general sentiment.</h4>
            </div> 
            <div class = "left" style = "width:60%; display:flex; align-items:center; justify-content:center; flex-direction:column; margin-top:50px">   
                <h3 style = "word-wrap:break-word; width:60%">Get Live news Updates while you look our <i>analytics</i></h3>   
                <a href = './News' target = "_self"><button type = 'button' style = "padding:10px 20px; font-size:20px; font-weight:700; border-radius:30px; ">Crypto News</button></a> 
                <br> <br>
                <h3 style = "word-wrap:break-word; width:60%">No Idea where to start with ? View out mathematically chosen <i>Top Trending NFTs</i></h3>  
                <a href = './Top_NFTs' target = "_self"><button type = 'button' style = "padding:10px 20px; font-size:20px; font-weight:700; border-radius:30px; ">Top NFTs</button></a> 
            </div> 
    </div>
""",unsafe_allow_html = True) 