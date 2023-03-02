import streamlit as st

from intro import show_intro
from analysis import show_analysis
from redshift import show_redshift

st.set_page_config(page_title = 'ODYSSEY | AstroAlgo',page_icon="page_icon.png", layout="wide", menu_items={
        'Get Help': 'https://www.linkedin.com/company/astroalgo',
        'Report a bug': "https://forms.gle/5hKrGPJGqs2aeHUC8",
        'About': '''$Odyssey$ by [AstroAlgo](https://www.linkedin.com/company/astroalgo): Data-Driven Insights Into The Cosmos'''
    })
logo = "1_bg.png"
st.sidebar.image(logo, use_column_width=True)
PAGE_DICT = {
    "What is Odyssey?": show_intro,
    "Astronomical Analysis": show_analysis,
    "Predict Galaxy Redshifts": show_redshift
}
page = st.sidebar.selectbox("Select a page", PAGE_DICT)

if page == "What is Odyssey?": #FIRST PAGE
    show_intro()

#***********************************************************************************************
       
elif page == "Astronomical Analysis": #SECOND PAGE
    show_analysis()
    
#***********************************************************************************************

elif page == "Predict Galaxy Redshifts": #THIRD PAGE
    st.title("Predict Galaxy Redshifts")
    # Add your redshift prediction content here


