import streamlit as st
import base64
from typing import List


def get_base64_from_png(png_path: str) -> str:
    with open(png_path, "rb") as image_file:
        return base64.b64encode(image_file.read())

def image_link(link: str, png_path: str) -> str:
    image_base64 = get_base64_from_png(png_path)
    html = f"<a href={link}><img src='data:image/png;base64,{image_base64.decode()}'></a>"
    return html


def sidebar(pages: List[str]) -> st.radio:
    st.sidebar.image("img/me_min.png", use_column_width=True)
    st.sidebar.subheader('Luc Vedrenne')
    left_column, mid_column, right_column = st.sidebar.beta_columns([4,1,1])
    left_column.text(
        "deep learning student    \n"
        "looking for a PhD.")
    html = image_link('https://github.com/the-dharma-bum', "./img/github_min.png")
    mid_column.markdown(html, unsafe_allow_html=True)
    html = image_link('https://linkedin.com/in/luc-vedrenne-499326155', "./img/linkedin_min.png")
    right_column.markdown(html, unsafe_allow_html=True)
    selection = st.sidebar.radio("Go to", pages)
    return selection