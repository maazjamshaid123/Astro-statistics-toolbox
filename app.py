import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm

st.set_page_config(page_title = 'ODYSSEY', layout="wide")

# col1, col2, col3 = st.columns(3)
# with col2:
st.image('odyssey.png')

# col1, col2, col3 = st.columns(3)
# with col2:
st.title('$ODYSSEY$ by AstroAlgo')
st.subheader('Odyssey by AstroAlgo: Empowering Your Journey through Cosmic Data')
st.markdown('----')

def plot_data(data, plot_type, x_col, y_col, z_col=None):
    if plot_type == 'Scatter':
        fig = px.scatter(data, x=x_col, y=y_col, color=z_col, width=1000, height=400)
    elif plot_type == 'Line':
        fig = px.line(data, x=x_col, y=y_col, color=z_col, width=1000, height=400)
    elif plot_type == 'Bar':
        fig = px.bar(data, x=x_col, y=y_col, color=z_col, width=1000, height=400)
    elif plot_type == 'Density Heatmap':
        fig = px.density_heatmap(data, x=x_col, y=y_col, width=1000, height=600,color_continuous_scale="Viridis")
    elif plot_type == 'Ordinary Least Square':
        fig = px.scatter(data, x=x_col, y=y_col, opacity=0.65,trendline='ols', trendline_color_override='red')
    elif plot_type == '3D Scatter':
        fig = px.scatter_3d(data, x=x_col, y=y_col, z=z_col, color=z_col, width=1000, height=600)
    st.plotly_chart(fig)



def main():

    st.write("Upload file to get started.")

    file = st.file_uploader("Upload a file", type=["csv", "xlsx"])
    if file is not None:
        if file.name.endswith('.csv'):
            data = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            data = pd.read_excel(file, engine='openpyxl')
        st.write("Data Frame:")
        st.write(data)

        plot_type = st.selectbox("Select Plot Type", ["Scatter", "Line", "Bar", "Density Heatmap","3D Scatter"])


        if plot_type == '3D Scatter':
            x_col = st.selectbox("Select X-axis Feature", data.columns)
            y_col = st.selectbox("Select Y-axis Feature", data.columns)
            z_col = st.selectbox("Select Z-axis Feature", data.columns)
        else:
            x_col = st.selectbox("Select X-axis Feature", data.columns)
            y_col = st.selectbox("Select Y-axis Feature", data.columns)
            z_col = None

        plot_data(data, plot_type, x_col, y_col, z_col)
        
if __name__ == '__main__':
    main()

        



    


