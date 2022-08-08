import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title='AWS Comprehend Medical', layout='wide', page_icon='💉')
st.header('AWS Comprehend Medical')

inp = st.text_area('Enter the diagnosis', height=150)
opt = st.radio('Select the option', ("Detect Entities", "RXNorm", "ICD-10-CM", "SNOMED CT", "Detect PHI"))
url = 'https://f6rlxo1pde.execute-api.us-east-1.amazonaws.com/cmaws' # OR YOUR OWN API URL

def insights(opt, inp):
    r = requests.post(url, json={'body': inp, 'choice': opt})
    return r.json()

if btn := st.button('Go!') and inp != '':
    r = insights(opt, inp)
    if r != []:
        df = pd.DataFrame(r)
        df = df[['Text', 'Category', 'Type', 'Score']]
        st.write(df)
    else:
        st.write('No results found')