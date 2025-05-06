import streamlit as st
import deepl_utils

st.title("Text Translator with DeepL")


# Language options
langs = {
    "English": "EN-US",
    "Czech": "CZ",
    "French": "FR",
    "German": "DE",
    "Spanish": "ES",
    "Italian": "IT",
    "Portuguese": "PT",
    "Dutch": "NL"
}

styles = {
    "general writing": "",
    "professionality": "",
    "friendliness": ""
}

st.subheader("TRANSLATION")
text_to_translate = st.text_area("Enter text to translate:", key='input')
target_lang = st.selectbox("Translate to:", list(langs.keys()))
target_lang = langs[target_lang]

# Translate button
if st.button("Translate"):
    if not text_to_translate: 
        st.write("Please enter text!")
    else:
        response = deepl_utils.translate(text_to_translate, target_lang)
        st.success("Translation successful:")
        st.write(response.text)


st.subheader("WRITING STYLE")
text_to_improve = st.text_area("Enter text to improve style:", key="style")
style = st.selectbox("Improve:", list(styles.keys()))
if st.button("Rewrite") and text_to_improve:
    #response = deepl_utils.translate(text_to_translate, target_lang)
    st.success("Feature will be available soon :)")