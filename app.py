import streamlit as st
import pandas as pd
import plotly.express as px
from skimage import io 

st.set_page_config(page_title = 'ODYSSEY', layout="wide")

# col1, col2, col3 = st.columns(3)
# with col2:
st.image('odyssey.png')

# col1, col2, col3 = st.columns(3)
# with col2:
st.title('$ODYSSEY$ by AstroAlgo')
st.subheader('Empowering Your Journey through Cosmic Data')
st.write('Provide feedback at: https://forms.gle/5hKrGPJGqs2aeHUC8')

st.markdown('----')

def plot_data(data, plot_type, x_col, y_col=None, z_col=None):
    if plot_type == 'Scatter':
        fig = px.scatter(data, x=x_col, y=y_col, width=1000, height=700)
    elif plot_type == 'Color-Color':
        fig = px.scatter(data, x=x_col, y=y_col, color=z_col, width=1000, height=700)
    elif plot_type == 'Line':
        fig = px.line(data, x=x_col, y=y_col, width=1000, height=700)
    elif plot_type == 'Light Curve':
        fig = px.line(data, x=x_col, y=y_col, color=z_col, width=1000, height=700)
    elif plot_type == 'Bar':
        fig = px.bar(data, x=x_col, y=y_col, width=1000, height=700)
    elif plot_type == 'Horizontal Bar':
        fig = px.bar(data, x=x_col, y=y_col, color=z_col, orientation='h', width=1000, height=700)
    elif plot_type == 'Histogram':
        fig = px.histogram(data, x=x_col, width=1000, height=700)
    elif plot_type == 'Density Heatmap':
        fig = px.density_heatmap(data, x=x_col, y=y_col, width=1000, height=700,color_continuous_scale="Viridis")
    elif plot_type == '3D Scatter':
        fig = px.scatter_3d(data, x=x_col, y=y_col, z=z_col, color=z_col, width=1000, height=700)
    elif plot_type == 'Analyze Image':
        fig = px.imshow(data, width=1000, height=700)
    st.plotly_chart(fig)


def main():
    file = st.file_uploader("Upload a file to get started", type=["csv", "xlsx", "jpg", "jpeg", "png"])
    if file is not None:
        if file.name.endswith('.csv'):
            data = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            data = pd.read_excel(file, engine='openpyxl')
        elif file.name.endswith('.jpg') or file.name.endswith('.jpeg') or file.name.endswith('.png'):
            data = io.imread(file)
            data = px.imshow(data, width=1000, height=700)
        st.subheader("Data:")
        st.write(data)

        if file.name.endswith('.csv') or file.name.endswith('.xlsx'):
            plot_type = st.selectbox("Select Plot Type", ["Scatter", "Color-Color", "Line", "Light Curve", "Bar", "Horizontal Bar", "Histogram", "Density Heatmap", "3D Scatter"])
            if plot_type == '3D Scatter':
                x_col = st.selectbox("Select X-axis Feature", data.columns)
                y_col = st.selectbox("Select Y-axis Feature", data.columns)
                z_col = st.selectbox("Select Z-axis Feature", data.columns)
            elif plot_type == 'Color-Color':
                x_col = st.selectbox("Select X-axis Feature", data.columns)
                y_col = st.selectbox("Select Y-axis Feature", data.columns)
                z_col = st.selectbox("Select Color Feature", data.columns)
            elif plot_type == 'Light Curve':
                x_col = st.selectbox("Select X-axis Feature", data.columns)
                y_col = st.selectbox("Select Y-axis Feature", data.columns)
                z_col = st.selectbox("Select Color Feature", data.columns)
            elif plot_type == 'Horizontal Bar':
                x_col = st.selectbox("Select X-axis Feature", data.columns)
                y_col = st.selectbox("Select Y-axis Feature", data.columns)
                z_col = st.selectbox("Select Color Feature", data.columns)
            elif plot_type == 'Histogram':
                x_col = st.selectbox("Select X-axis Feature", data.columns)
                y_col = None
                z_col = None
            else:
                x_col = st.selectbox("Select X-axis Feature", data.columns)
                y_col = st.selectbox("Select Y-axis Feature", data.columns)
                z_col = None
            plot_data(data, plot_type, x_col, y_col, z_col)

if __name__ == '__main__':
    main()