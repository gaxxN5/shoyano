#!/usr/bin/env -S python -m streamlit run

import streamlit as st

with st.echo(code_location='below'):
    st.title(':red[風船アニメーション]')
    st.balloons()
