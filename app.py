import streamlit as st
from intro import show_intro
from analysis import show_analysis
from astrogpt import show_gpt
from astrodata import show_caelus

st.set_page_config(page_title = 'ODYSSEY',page_icon="page_icon.png", layout="wide", menu_items={
        'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
        'Report a bug': "https://www.linkedin.com/in/maazjamshaid/",
        'About': '''$Odyssey$: Data-Driven Insights Into The Cosmos'''
    })

st.sidebar.image("5.png", use_column_width=True)
# st.sidebar.markdown("---")

PAGE_DICT = {
    "What is Odyssey? 🌌": show_intro,
    "Exploratory Data Analysis (EDA) 📊": show_analysis,
    "AstroGPT Insights 🧠": show_gpt,
    "Talk to Caelus 🤖": show_caelus
}
page = st.sidebar.selectbox("Get Started", PAGE_DICT)

st.sidebar.markdown("---")

st.write('©2022 AstroAlgo')

#***********************************************************************************************

if page == "What is Odyssey? 🌌": #FIRST PAGE
    show_intro()

#***********************************************************************************************
       
elif page == "Exploratory Data Analysis (EDA) 📊": #SECOND PAGE
    show_analysis()
    
#***********************************************************************************************

elif page == "AstroGPT Insights 🧠": #THIRD PAGE
    show_gpt()

#***********************************************************************************************

elif page == "Talk to Caelus 🤖": #FOURTH PAGE
    show_caelus()
