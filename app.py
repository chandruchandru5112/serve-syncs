"""Volunteer Opportunity Finder - Streamlit wrapper.

Embeds the single-page app (index.html, same folder) inside Streamlit.
Deploy on Streamlit Community Cloud with main file = app.py.

Data (opportunities, registrations, history, profile) is stored in each
visitor's browser localStorage, so it is private to that browser/device.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Volunteer Opportunity Finder",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default padding/chrome so the app fills the page
st.markdown(
    """
    <style>
      #MainMenu, footer, header[data-testid="stHeader"] {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1400, scrolling=True)
