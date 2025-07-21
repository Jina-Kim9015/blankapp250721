import streamlit as st

import streamlit as st
import pandas as pd
import time

st.title("🎈 My new app")  # 기존 타이틀 유지

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header("1. 텍스트 요소")  # 헤더
st.subheader("서브헤더 예시")  # 서브헤더
st.text("일반 텍스트입니다.")  # 일반 텍스트
st.header("2. 데이터 표시")  # 데이터 표시 섹션
st.write("DataFrame 예시:")
df = pd.DataFrame({
    '이름': ['홍길동', '김철수'],
    '나이': [28, 34]
})
st.dataframe(df)  # 데이터프레임 표시
st.table(df)  # 정적 테이블 표시
st.json({'key': 'value', 'list': [1, 2, 3]})  # JSON 표시

st.header("3. 미디어 요소")  # 미디어 요소
st.image("https://static.streamlit.io/examples/cat.jpg", caption="고양이 사진")  # 이미지
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오
st.video("https://www.youtube.com/watch?v=5qap5aO4i9A")  # 비디오

st.header("4. 입력 위젯")  # 입력 위젯
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
option = st.radio("성별을 선택하세요", ('남성', '여성'))  # 라디오 버튼
selected = st.selectbox("좋아하는 과일을 선택하세요", ['사과', '바나나', '오렌지'])  # 셀렉트박스
multi = st.multiselect("좋아하는 색상을 모두 선택하세요", ['빨강', '파랑', '초록'])  # 멀티셀렉트
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time_input = st.time_input("시간을 선택하세요")  # 시간 입력
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로더
st.slider("점수를 선택하세요", 0, 100, 50)  # 슬라이더

st.header("5. 버튼 및 상호작용")  # 버튼
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")  # 버튼 클릭 시 메시지

st.header("6. 진행 표시 및 상태")  # 진행 표시
with st.spinner("잠시만 기다려주세요..."):  # 스피너
    time.sleep(1)
st.success("완료!")  # 성공 메시지
st.info("정보 메시지입니다.")  # 정보 메시지
st.warning("경고 메시지입니다.")  # 경고 메시지
st.error("에러 메시지입니다.")  # 에러 메시지

st.header("7. 사이드바")  # 사이드바
st.sidebar.title("사이드바 제목")
st.sidebar.write("여기는 사이드바입니다.")

st.header("8. 레이아웃")  # 레이아웃
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

with st.expander("더보기"):
    st.write("이곳에 추가 정보를 넣을 수 있습니다.")

# 각 요소마다 주석(각주)을 달아 어떤 기능인지