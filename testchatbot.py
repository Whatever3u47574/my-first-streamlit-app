import streamlit as st

st.title("🤖 기분에 따라 답해주는 챗봇")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 오늘 기분은 어떠신가요?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("메시지를 입력하세요."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if "행복" in prompt or "기뻐" in prompt or "좋아" in prompt:
        response = "정말 좋은 날이네요! 오늘 하루도 행복한 일만 가득하시길 바라요. ✨"
    elif "슬퍼" in prompt or "우울" in prompt or "힘들" in prompt:
        response = "그런 날도 있죠. 따뜻한 차 한 잔 마시면서 잠시 쉬어가는 건 어떨까요? 제가 옆에 있어 드릴게요. ☕"
    elif "배고파" in prompt or "음식" in prompt or "뭐 먹지" in prompt:
        response = "맛있는 음식을 먹으면 기분이 좋아지죠! 오늘은 따끈한 국물이 있는 음식을 추천해요! 🍜"
    else:
        response = "그렇군요. 더 듣고 싶어요. 어떤 이야기를 해주시겠어요?"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

        