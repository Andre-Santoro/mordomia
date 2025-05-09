import streamlit as st

def configuração_pagina():
    st.set_page_config(
        page_title="MordomIA",
        page_icon="🤵",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)