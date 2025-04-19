#!/usr/bin/env -S python -m streamlit run

import streamlit as st

print('reloaded', flush=True)
st.title('title string `<h1>`')
st.header('大見出し `<h2>`')
st.subheader(
    body='中見出し `<h3>`',
    anchor='title',
    help='`<h3>`あるいは`###`に相当するStreamlitのコマンド',
    divider=True
)
