import streamlit as st

def show_intro():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('odyssey_logo.png')

    # st.title("$WHAT$ $IS$ $ODYSSEY?$")
    st.subheader('From Data To Discovery: Revolutionize Your Understanding Of The Cosmos')

    st.markdown('----')

    st.write('Provide feedback at: https://forms.gle/5hKrGPJGqs2aeHUC8')
    st.write('Linkedin: [AstroAlgo](https://www.linkedin.com/company/astroalgo)')

    st.markdown('----')
