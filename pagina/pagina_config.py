import streamlit as st

def configuração_pagina():
    return st.set_page_config(
    page_title="MordomIA",
    page_icon="🤵",
    layout="centered",
    initial_sidebar_state="collapsed"
)