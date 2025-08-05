# streamlit, matplotlib, numpy 라이브러리를 가져옵니다.
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# --- 한글 폰트 설정 (필수) ---
try:
    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
    plt.rc('font', family='NanumGothic')
    plt.rcParams['axes.unicode_minus'] = False
except FileNotFoundError:
    st.warning("나눔고딕 폰트를 찾을 수 없습니다. 차트의 한글이 깨질 수 있습니다.")

# --- Streamlit 앱 제목 설정 ---
st.title('🎨 Matplotlib으로 음식 선호도 차트 그리기')
st.write("랜덤으로 생성된 음식 선호도 데이터를 Matplotlib 차트로 그려보는 실습입니다.")
st.write("---")


# --- 랜덤 데이터 생성 ---
# 시각화할 데이터를 간단하게 생성합니다.
foods = ['떡볶이', '치킨', '피자', '라면', '초밥', '햄버거']
# 각 음식에 대한 랜덤 투표 수(10표 ~ 50표)를 생성합니다.
votes = np.random.randint(10, 51, size=len(foods))


# --- Matplotlib 차트 생성 ---
st.header("음식 선호도 조사 결과")

# 1. 차트를 그릴 도화지(figure)와 좌표평면(axes) 준비
fig, ax = plt.subplots(figsize=(10, 6))

# 2. 막대그래프(bar chart) 그리기
ax.bar(foods, votes, color='lightcoral')

# 3. 차트 꾸미기
ax.set_title('전체 학생 대상 음식 선호도', fontsize=16)
ax.set_xlabel('음식 종류')
ax.set_ylabel('득표 수')
ax.tick_params(axis='x', rotation=45) # x축 라벨이 겹치지 않도록 45도 회전

# 4. Streamlit에 차트 표시
st.write("`st.pyplot(fig)`을 사용하여 Matplotlib 차트를 화면에 표시합니다.")
# plt.show() 대신 st.pyplot(fig)를 사용합니다.
st.pyplot(fig)