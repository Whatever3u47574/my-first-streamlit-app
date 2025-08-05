import streamlit as st

# openai 라이브러리 임포트 (app.py 상단에서 import 필요)
from openai import OpenAI

st.title("🧑‍🎓 학생 심리상담 챗봇 (Upstage Solar Pro2)")

# OpenAI 클라이언트 생성 (Upstage Solar Pro2)
client = OpenAI(
    api_key=st.secrets["UPSTAGE_API_KEY"],
    base_url="https://api.upstage.ai/v1"
)

# 세션 상태에 메시지 저장
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 저는 여러분의 심리상담을 도와주는 챗봇입니다. 무엇이든 편하게 이야기해 주세요."}
    ]

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
if prompt := st.chat_input("상담 내용을 입력해 주세요."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Upstage Solar Pro2로 답변 생성 (streaming)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # OpenAI 메시지 포맷에 맞게 변환
        messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]

        stream = client.chat.completions.create(
            model="solar-pro2",
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


