import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")   # 👉 PANTALLA COMPLETA REAL

# Leer archivo HTML
with open("OPERMERAS.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Contenedor full screen con CSS
full_html = f"""
    <style>
        .container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 95vw;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
            z-index: 1;
        }}
        iframe {{
            width: 100%;
            height: 70%;
            border: none;
        }}
    </style>
    <div class="container">
        {html_content}
    </div>
"""

components.html(full_html, height=3800, scrolling=False)


