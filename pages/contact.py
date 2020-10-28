import streamlit as st
import base64

def content():
    st.title('Contact me')
    left_column, right_column = st.beta_columns(2)
    left_column.write('Phone: +33 7 50 92 55 97')
    left_column.write('Email: vedrenneluc@gmail.com')
    right_column.write('[LinkedIn](https://linkedin.com/in/luc-vedrenne-499326155)')
    right_column.write('[Github](https://github.com/the-dharma-bum)')