import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("성적 분석 도구")  # 페이지 타이틀

# 파일 업로더 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(df)  # 데이터프레임 표시

    # 학생별 평균 점수 계산
    score_cols = ['수학', '영어', '과학']
    if all(col in df.columns for col in score_cols):
        df['평균'] = df[score_cols].mean(axis=1)
        st.subheader("학생별 평균 점수")
        st.dataframe(df[['이름', '평균']])

        # 과목별 석차 계산
        st.subheader("과목별 석차")
        rank_df = df[['이름']].copy()
        for col in score_cols:
            rank_df[col + ' 석차'] = df[col].rank(ascending=False, method='min').astype(int)
        st.dataframe(rank_df)

        # 학생별 평균 점수 시각화
        st.subheader("학생별 평균 점수 그래프")
        fig, ax = plt.subplots()
        ax.bar(df['이름'], df['평균'], color='skyblue')
        ax.set_xlabel('이름')
        ax.set_ylabel('평균 점수')
        ax.set_title('학생별 평균 점수')
        st.pyplot(fig)

        # 과목별 점수 분포 시각화
        st.subheader("과목별 점수 분포")
        fig2, ax2 = plt.subplots()
        for col in score_cols:
            ax2.plot(df['이름'], df[col], marker='o', label=col)
        ax2.set_xlabel('이름')
        ax2.set_ylabel('점수')
        ax2.set_title('과목별 점수 분포')
        ax2.legend()
        st.pyplot(fig2)
    else:
        st.error("CSV 파일에 '수학 성적', '영어 성적', '과학 성적' 컬럼이 모두 포함되어야 합니다.")
else:
    st.info("CSV 파일을 업로드하면 성적 분석 결과가 표시됩니다.")

# 각 주요 부분에