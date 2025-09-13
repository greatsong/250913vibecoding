import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("MBTI 유형별 Top 10 국가 시각화")

# 기본 파일 경로
default_file = "countriesMBTI_16types.csv"
df = None

# 1) 기본 파일이 있으면 그걸 사용
if os.path.exists(default_file):
    df = pd.read_csv(default_file)
    st.success(f"기본 데이터 파일을 불러왔습니다: {default_file}")

# 2) 없으면 업로드 요청
else:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("업로드한 파일을 불러왔습니다.")

# 데이터가 준비된 경우에만 실행
if df is not None:
    mbti_types = df.columns[1:]  # 첫 번째는 Country
    
    # MBTI 유형 선택
    selected_mbti = st.selectbox("분석할 MBTI 유형을 선택하세요:", mbti_types)
    
    # 선택한 MBTI 기준으로 정렬 후 상위 10개 추출
    top10 = df[["Country", selected_mbti]].sort_values(by=selected_mbti, ascending=False).head(10)
    
    # Altair 그래프
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_mbti, title=f"{selected_mbti} 비율"),
            y=alt.Y("Country", sort="-x", title="국가"),
            tooltip=["Country", selected_mbti]
        )
        .interactive()
    )
    
    st.altair_chart(chart, use_container_width=True)
