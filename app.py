import streamlit as st
from intro import show_intro
from analysis import show_analysis
# from redshift import show_redshift
# from black_hole import show_black_hole

st.set_page_config(page_title = 'ODYSSEY | AstroAlgo',page_icon="page_icon.png", layout="wide", menu_items={
        'Get Help': 'https://www.linkedin.com/company/astroalgo',
        'Report a bug': "https://forms.gle/5hKrGPJGqs2aeHUC8",
        'About': '''$Odyssey$ by [AstroAlgo](https://www.linkedin.com/company/astroalgo): Data-Driven Insights Into The Cosmos'''
    })

st.sidebar.image("astroalgo.png", use_column_width=True)

st.sidebar.markdown("---")

PAGE_DICT = {
    "What is Odyssey?": show_intro,
    "Astronomical Analysis": show_analysis,
    # "Predict Galaxy Redshifts": show_redshift
}
page = st.sidebar.selectbox("Get Started", PAGE_DICT)

st.sidebar.markdown("---")


#***********************************************************************************************

if page == "What is Odyssey?": #FIRST PAGE
    show_intro()

#***********************************************************************************************
       
elif page == "Astronomical Analysis": #SECOND PAGE
    show_analysis()
    
#***********************************************************************************************

# elif page == "Predict Galaxy Redshifts": #THIRD PAGE
#     show_redshift()

#***********************************************************************************************

# elif page == "Black Holes in Globular Clusters": #FOURTH PAGE
#     show_black_hole()
