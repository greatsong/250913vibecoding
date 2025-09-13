import streamlit as st
import random

st.set_page_config(page_title="MBTI 공부 추천 💡", page_icon="📚", layout="centered")

# 헤더
st.title("📚 MBTI 유형별 공부 방법 추천 ✨")
st.write("당신의 MBTI를 선택하면 🎯 딱 맞는 공부 비법을 알려드려요!")

# MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

choice = st.selectbox("👉 MBTI 유형을 골라주세요!", mbti_list)

# MBTI별 추천 공부 방법
study_tips = {
    "INTJ": "📖 혼자 깊게 탐구하며 📊 계획을 세워 체계적으로 공부하세요!",
    "INTP": "🧪 호기심을 따라 실험처럼 🔍 탐구하는 공부가 잘 맞아요!",
    "ENTJ": "⚡ 목표를 크게 잡고 💼 리더십 있게 스터디 그룹을 이끌어보세요!",
    "ENTP": "💡 토론과 💬 브레인스토밍으로 아이디어 폭발형 공부!",
    "INFJ": "🌱 의미와 가치를 찾으며 ✍️ 조용히 글로 정리하는 게 좋아요.",
    "INFP": "🎨 감성을 살려 ✨ 스스로와 연결된 공부 주제를 찾아보세요.",
    "ENFJ": "🤝 사람들과 함께 ❤️ 서로 가르쳐주는 방식으로 공부해보세요.",
    "ENFP": "🎉 자유롭게 🪄 창의적 프로젝트로 배우는 게 좋아요!",
    "ISTJ": "📑 꼼꼼히 ✏️ 규칙과 원칙을 지키며 반복 학습이 잘 맞아요.",
    "ISFJ": "🧸 안정된 환경에서 📒 차분히 복습하는 공부법이 좋아요.",
    "ESTJ": "📋 명확한 목표를 세우고 ✅ 실용적으로 문제를 해결해보세요.",
    "ESFJ": "👥 친구들과 함께 🎶 협동 학습으로 시너지를 내보세요.",
    "ISTP": "🔧 직접 해보는 🛠️ 실습 중심 공부법이 잘 맞아요.",
    "ISFP": "🌸 편안한 분위기에서 🎨 감각을 살린 공부가 좋아요.",
    "ESTP": "🔥 도전적인 문제를 🏃 빠르게 해결하며 배우는 게 좋아요.",
    "ESFP": "🎶 재미있고 🎭 활동적인 학습 환경에서 공부가 잘 돼요!"
}

# 결과 출력
if choice:
    st.subheader(f"✨ {choice} 유형의 추천 공부 방법은...")
    st.success(study_tips[choice])

    # 재미있는 효과 랜덤 적용
    effect = random.choice(["balloons", "snow", "celebration"])
    if effect == "balloons":
        st.balloons()
    elif effect == "snow":
        st.snow()
    else:
        st.toast("공부 파이팅! 🚀✨", icon="🔥")
