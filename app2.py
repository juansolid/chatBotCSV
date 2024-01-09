import streamlit as st
#from pandasai.llm.openai import OpenAI
from pandasai.llm import GooglePalm
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import SmartDataframe
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

load_dotenv()
# AIzaSyD8QoXRAcQ76OQyAL97QD5O20nU1bptm4s
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "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"

def chat_with_csv(df,prompt):
    llm = GooglePalm(api_key="AIzaSyD8QoXRAcQ76OQyAL97QD5O20nU1bptm4s")
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    return result

st.set_page_config(layout='wide')
st.title("Chatbot IA generativa")
st.markdown('<style>h1{color: BLUE; text-align: center;}</style>', unsafe_allow_html=True)
st.subheader('Analisis archivo CSV')
st.markdown('<style>h3{color: red;  text-align: center;}</style>', unsafe_allow_html=True)

# Upload multiple CSV files
input_csvs = st.sidebar.file_uploader("Carga de archivo  CSV ", type=['csv'], accept_multiple_files=True)

if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    #load and display the selected csv file 
    st.info("CSV uploaded successfully")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data,use_container_width=True)

    #Enter the query for analysis
    st.info("Chat Below")
    input_text = st.text_area("Enter the query")

    #Perform analysis
    if input_text:
        if st.button("Chat with csv"):
            st.info("Your Query: "+ input_text)
            result = chat_with_csv(data,input_text)
            fig_number = plt.get_fignums()
            if fig_number:
                st.pyplot(plt.gcf())
            else:
                st.success(result)