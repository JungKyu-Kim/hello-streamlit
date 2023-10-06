import streamlit as st
from streamlit.hello.utils import show_code

st.sidebar.header("Simple Demo")
a = st.sidebar.radio('Select one:', [1, 2])

st.markdown("# Simple Demo")
st.write(
    """테스트 입니다."""
)
