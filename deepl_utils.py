import deepl
import os
import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()

#API_KEY = os.getenv('DEEPL_API_KEY')
API_KEY = st.secrets["DEEPL_API_KEY"]
deepl_client = deepl.DeepLClient(API_KEY)


def translate(text, target_lang):
    # optional: tune level of formality 
    # optional: tune model response time (trade for quality)
    return deepl_client.translate_text(text, target_lang=target_lang)


def improve_style(text, tone='friendly'):
    return deepl_client.rephrase_text(text, tone=tone)
