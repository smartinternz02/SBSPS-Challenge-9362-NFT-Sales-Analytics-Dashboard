from email.headerregistry import UniqueSingleAddressHeader
import streamlit as st 

st.set_page_config(page_title="About-CryptoKnights",layout = "wide")  

st.markdown("""
   <style>
      .content ul li{
         font-size:20px; 
      }

      .team span{
         font-size:20px;  
      }

      .team{
         display:flex; 
         align-items:center; 
         justify-content:center; 
         gap:50px;   
      }

      .team_header{
         font-size:10px;

      }

      .team{
         width:80%;
         padding:30px;  
      }

      .fac{
         display:flex; 
         align-items:center; 
         justify-content:flex-end;  
         width:90%; 
         letter-spacing:1px; 
      }
   </style>
   <div class = "container" style = "display:flex; align-items:center; justify-content:center; flex-direction:column">   
      <div class = "content" style = "display:flex; flex-direction:column; align-items:center; justify-content:center"> 
      <h2 style = "text-align:center">About us</h2>
      <h5 style = "text-align:center;line-height:40px; letter-spacing:1px">We are the Students from <br> Dr.MGR Educational and research Institute<br><span>Maduravoyal , Chennai - India</span></h5> 
   </div>
   <div class = 'content' style = "display:flex; align-items:center; justify-content:space-between; width:80%" > 
      <ul style = "display:block; padding:20px; width:50%">  
         <li>NFTs have recently received enormous attention from both cryptocurrency investors and the media</li>
         <li>This is a Web-based Data Analytics app to solve conflicts and confusions about NFTs</li>
         <li>Due to sudden raise in NFT trends in the market and people being inaware and unguided of where to invest in, our Analytics app provides a clear idea of NFT trends</li>
      </ul>
      <span style = "display:block; text-align:center;padding:20px; margin:50px; font-size:30px; width:50%">   
         And MoreOver , <b>ITS FOSS!!</b> 
         As we built this without any <i>paid</i> or <i>subscription</i> based services , It's possible to make it open-Source for people to explore and better understand the new World !!   
      </span>  
   </div>
   <div class = 'team'> 
         <h3 class='team_header'>Team Members : </h3>  
         <span>Harishwar</span>
         <span>Gurubaravikkram</span>
         <span>Harichselvam</span>
         <span>Hariharan</span> 
   </div>  
   <div class = 'fac'> 
      <p>-- Under the guidance of : Ms.Aiswarya Vijayan (IBM Faculty)</p> 
   <div>
""", unsafe_allow_html=True) 