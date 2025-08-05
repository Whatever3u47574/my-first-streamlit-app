import streamlit as st

st.title("📝 미니 설문조사")

with st.form('미니 설문조사'):
    st.write("아래 설문에 답변해주세요.")

    name = st.text_input("이름을 입력하세요.")
    food = st.text_input("가장 좋아하는 음식은 무엇인가요?")
    opinion = st.text_area("하고 싶은 말을 자유롭게 적어주세요.")

    submit = st.form_submit_button('제출하기')

if submit:
    st.write('---')
    st.success("설문조사에 참여헤주셔서 감사합니다.")

    st.write(f'이름: {name}')
    st.write(f'좋아하는 음식{food}')
    st.write(f'남겨주신 의견: {opinion}')