# streamlit, pandas, numpy 라이브러리를 가져옵니다.
import streamlit as st
import pandas as pd
import numpy as np

# --- Streamlit 앱 제목 설정 ---
st.title('🐼 Pandas로 음식 선호도 데이터 만들기')
st.write("학급별 음식 선호도 데이터를 랜덤으로 생성하고, Streamlit 표로 확인하는 실습입니다.")
st.write("---")

# --- 데이터 준비 ---
# 설문 대상 음식과 학급 리스트를 정의합니다.
foods = ['김치', '햄버거', '피쉬&칩', '스시', '마라탕']
classes = ['대한민국', '미국', '프랑스', '일본', '쭝국']

# --- 랜덤 데이터 생성 및 DataFrame 만들기 ---
# 각 음식에 대해 학급별로 랜덤한 투표 수(5표~20표)를 생성하여 딕셔너리에 저장합니다.
survey_data = {
    food: np.random.randint(0, 23456, size=len(classes)) for food in foods
}

# 생성된 딕셔너리 데이터와 학급 이름을 인덱스로 사용하여 DataFrame을 만듭니다.
df = pd.DataFrame(survey_data, index=classes)


# --- Streamlit으로 결과 출력 ---

st.header("학급별 음식 선호도 투표 결과 (랜덤)")
# 생성된 데이터프레임을 Streamlit 화면에 표로 표시합니다.
st.dataframe(df)

st.header("음식별 총 득표수")
st.write("각 음식의 총 득표수를 계산한 결과입니다.")
# 각 열(음식)의 합계를 계산하여 새로운 데이터프레임으로 보여줍니다.
total_votes = df.sum().sort_values(ascending=False)
st.dataframe(total_votes)