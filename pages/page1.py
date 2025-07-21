import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 폰트 매니저 임포트
import os

st.title("matplotlib 시각화 예시")  # 페이지 타이틀

# NanumGothic 폰트 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)

# matplotlib 기본 폰트 설정
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 예시 데이터프레임 생성
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [28, 34, 22]
})

st.write("데이터프레임 예시:")
st.dataframe(df)  # 데이터프레임 표시

# matplotlib을 활용한 막대그래프 시각화
fig, ax = plt.subplots()
ax.bar(df['이름'], df['나이'], color=['skyblue', 'orange', 'green'])
ax.set_xlabel('이름', fontproperties=fontprop)
ax.set_ylabel('나이', fontproperties=fontprop)
ax.set_title('이름별 나이 막대그래프', fontproperties=fontprop)
ax.tick_params(axis='x', labelsize=10)
for label in ax.get_xticklabels():
    label.set_fontproperties(fontprop)
for label in ax.get_yticklabels():
    label.set_fontproperties(fontprop)

st.pyplot(fig)  # Streamlit에 matplotlib 그래프 출력

# 각 요소마다 주석(각주)을 달아 어떤 기능인지 설명했습니다.