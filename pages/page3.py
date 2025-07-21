import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

st.title("성적 데이터 시각화")  # 페이지 타이틀

# NanumGothic-Bold 폰트 경로 지정
font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Bold.ttf')
fontprop = fm.FontProperties(fname=font_path)

# matplotlib 기본 폰트 설정
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 예시 데이터 생성
data = {
    '이름': ['홍길동', '김영희', '이철수', '박민수', '최지은'],
    '수학': [85, 90, 70, 95, 60],
    '영어': [78, 88, 65, 92, 72],
    '과학': [92, 84, 75, 89, 68]
}
df = pd.DataFrame(data)

# 인덱스를 1부터 시작하도록 설정
df.index = df.index + 1

st.write("성적 데이터:")
st.dataframe(df)

# 학생별 평균 점수 계산
df['평균'] = df[['수학', '영어', '과학']].mean(axis=1)
st.subheader("학생별 평균 점수")
st.dataframe(df[['이름', '평균']])

# 학생별 평균 점수 시각화
st.subheader("학생별 평균 점수 그래프")
fig, ax = plt.subplots()
ax.bar(df['이름'], df['평균'], color='skyblue')
ax.set_xlabel('이름', fontproperties=fontprop)
ax.set_ylabel('평균 점수', fontproperties=fontprop)
ax.set_title('학생별 평균 점수', fontproperties=fontprop)
for label in ax.get_xticklabels():
    label.set_fontproperties(fontprop)
for label in ax.get_yticklabels():
    label.set_fontproperties(fontprop)
st.pyplot(fig)

# 과목별 점수 분포 시각화
st.subheader("과목별 점수 분포")
fig2, ax2 = plt.subplots()
for col in ['수학', '영어', '과학']:
    ax2.plot(df['이름'], df[col], marker='o', label=col)
ax2.set_xlabel('이름', fontproperties=fontprop)
ax2.set_ylabel('점수', fontproperties=fontprop)
ax2.set_title('과목별 점수 분포', fontproperties=fontprop)
for label in ax2.get_xticklabels():
    label.set_fontproperties(fontprop)
for label in ax2.get_yticklabels():
    label.set_fontproperties(fontprop)
ax2.legend(prop=fontprop)
st.pyplot(fig2)

# 각 주요 부분에