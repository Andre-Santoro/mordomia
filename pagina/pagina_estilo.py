import streamlit as st

def estilo_pagina():
    return st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom, #1f005c, #5b0060, #870160, #ac255e, #ca485c, #e16b5c, #f39060, #ffb56b);
            color: white;
        }

        /* Estilo do input de mensagem */
        input[type="text"] {
            border-radius: 4px !important;
            border: 1px solid #ccc !important;
            box-shadow: none !important;
            outline: none !important;
        }

        input[type="text"]:focus {
            border: 1px solid #ccc !important;
            box-shadow: none !important;
            outline: none !important;
        }

        /* Rodapé fixo na parte inferior da janela */
        .rodape-container {
            width: 100%;
            position: fixed;
            bottom: 0;
            left: 0;
            background-color: rgba(0, 0, 0, 0.2);
            text-align: center;
            padding: 10px 0;
            font-size: 12px;
            color: white;
            opacity: 0.7;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)
