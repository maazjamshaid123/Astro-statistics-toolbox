import streamlit as st
import pandas as pd
import openai

def show_gpt():
    key = st.sidebar.text_input("ENTER API KEY")
    openai.api_key = key

    st.title("_AstroGPT_ 🧠")
    st.markdown('---')

    name = st.text_input("Name")
    date = st.date_input("Date", value=None)
    topic = st.text_input("Topic")

    st.markdown("---")

    uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
    
        # Display the DataFrame
        st.dataframe(df)

        # Convert DataFrame to a string representation
        text = df.to_string(index=False)

        st.write(f"Token: {len(text)}")

        if st.button('ANALYZE'):
            messages = [{"role": "system", "content": f" In the start of report mention: \nName: {name}\nDate: {date}\nTopic: {topic}. Your name is ASTROGPT. Produce a comprehensive analysis report by thoroughly examining the contents of the provided CSV file. Explore the data trends, patterns, and insights that emerge from the dataset, find mean, median and other possible calculations for each columns to highlight key findings. The report should delve into the relationships between variables, identify any outliers or anomalies, and present a well-structured interpretation of the information. Produce results under the following headings: Introduction, Data Source and Description, Statistical Calculations (do calculations), Data Preprocessing Needed, Data Trends and Patterns, Advanced Analysis Techniques (if applicable), Discussion, Conclusion, Limitations."}]

            def CustomChatGPT(user_input):
                messages.append({"role": "user", "content": user_input})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                ChatGPT_reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": ChatGPT_reply})
                return ChatGPT_reply

            response = CustomChatGPT(text)
            st.text_area('AstroGPT:', value=response, height=300, max_chars=None, key=None) 