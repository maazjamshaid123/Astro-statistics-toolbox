import streamlit as st
import time

def show_intro():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('odyssey.png')

    st.title("_ODYSSEY by  AstroAlgo_")
    st.subheader('From Data To Discovery: Revolutionize Your Understanding Of The Cosmos')

    st.markdown('----')

    st.write('Provide feedback [here](https://forms.gle/5hKrGPJGqs2aeHUC8)')
    st.write('[Linkedin](https://www.linkedin.com/company/astroalgo)')

    st.markdown('----')

    st.write('''
    $Odyssey$ is an innovative app developed by $AstroAlgo$ that is designed to help 
    space scientists in the fields of astronomy and astrophysics. With the help of data-driven 
    approaches such as data analysis, visualization, machine learning, and artificial 
    intelligence, Odyssey provides effective solutions for a wide range of problems faced by 
    space scientists.
    
    The app is designed to be user-friendly and accessible to scientists with varying 
    levels of expertise in data-driven approaches. With a wide range of tools and features, 
    Odyssey makes it easy for scientists to analyze large datasets, visualize complex data, 
    and develop effective solutions to a variety of problems.

    AstroAlgo is a Space Research company that is dedicated to advancing the field of space 
    sciences through innovative data-driven solutions. With a team of expert scientists and 
    engineers, AstroAlgo is committed to providing cutting-edge tools and technologies that 
    help scientists better understand the universe around us.
    
    If you're a space scientist looking for effective data-driven solutions to complex problems
    in astronomy and astrophysics, Odyssey is the web app for you. With its 
    user-friendly interface and advanced features, Odyssey can help you take your research to 
    the next level and unlock new insights into the mysteries of the cosmos.
    ''')

    st.markdown("---")

    st.error('Astronomical Analysis', icon = "🪐")
    # Define the list of items to display
    items = [
        'Scatter Plot',
        'Color-Color Plot',
        'Line Plot',
        'Plot For Light Curve',
        'Bar Plot',
        'Horizontal Bar Plot',
        'Histogram',
        'Density Heatmap',
        'PCA Analysis',
        'Contour Plot',
        'Distplot',
        'Residual',
        'Ordinary Least Square (OLS)',
        'Receiver Operating Characteristics (ROC)',
        'Enhanced Prediction Error Analysis',
        '3D Scatter'
    ]

    # Calculate the number of rows required to display all the items
    num_rows = len(items) // 3 + 1

    # Use a for loop to display each item in a separate column
    for i in range(num_rows):
        col1, col2, col3 = st.columns(3)
        if i*3 < len(items):
            col1.info(items[i*3])
        if i*3+1 < len(items):
            col2.info(items[i*3+1])
        if i*3+2 < len(items):
            col3.info(items[i*3+2])

    st.markdown("---")



