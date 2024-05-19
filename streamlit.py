import streamlit as st

st.title('인공지능 시인')

title = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    st.write("시")
