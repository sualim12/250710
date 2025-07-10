import streamlit as st

st.set_page_config(page_title="MBTI 여행지 추천", page_icon="✈️")

st.title("✈️ MBTI별 추천 여행지")
st.write("당신의 MBTI 유형을 선택하면, 어울리는 여행지 3곳과 꼭 가야 할 명소를 추천해드릴게요! 🎒")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("MBTI 유형을 선택하세요 👇", mbti_list)

recommendations = {
    "INTJ": {
        "places": ["교토 🇯🇵", "하이델베르크 🇩🇪", "바르셀로나 🇪🇸"],
        "highlight": "하이델베르크 성 🏰",
        "reason": "조용하고 역사 깊은 도시 속에서 사색할 수 있는 장소이기 때문이에요."
    },
    "INFP": {
        "places": ["프라하 🇨🇿", "호이안 🇻🇳", "코펜하겐 🇩🇰"],
        "highlight": "프라하 구시가지 🕯️",
        "reason": "동화 같은 분위기에서 감성적인 상상을 펼치기 좋아요."
    },
    "ENTP": {
        "places": ["뉴욕 🇺🇸", "베를린 🇩🇪", "도쿄 🇯🇵"],
        "highlight": "뉴욕 브루클린 거리 🌆",
        "reason": "창의적인 자극을 받을 수 있는 다양성과 개성이 넘치는 곳이기 때문이에요."
    },
    "ISFJ": {
        "places": ["부다페스트 🇭🇺", "스위스 루체른 🇨🇭", "교토 🇯🇵"],
        "highlight": "루체른 호수 ⛵",
        "reason": "평화롭고 조용한 분위기에서 마음의 안정을 찾을 수 있어요."
    },
    # 필요시 아래에 나머지 MBTI 유형도 추가 가능
}

if mbti in recommendations:
    st.subheader(f"💡 {mbti} 유형에게 어울리는 여행지")
    for place in recommendations[mbti]["places"]:
        st.markdown(f"- {place}")

    st.markdown(" ")
    st.subheader(f"🌟 꼭 가보면 좋을 장소: **{recommendations[mbti]['highlight']}**")
    st.write(f"이유: {recommendations[mbti]['reason']}")

    st.balloons()
else:
    st.info("아직 이 MBTI에 대한 추천 정보가 준비 중이에요. 곧 업데이트할게요! 🔧")
