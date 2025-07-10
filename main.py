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
        "reason": "고요한 분위기와 깊은 역사에서 사색과 분석적 사고를 즐길 수 있어요."
    },
    "INTP": {
        "places": ["케임브리지 🇬🇧", "레고랜드 빌룬 🇩🇰", "헬싱키 🇫🇮"],
        "highlight": "케임브리지 대학교 도서관 📚",
        "reason": "지적 자극을 주는 공간에서 아이디어와 탐구를 마음껏 펼칠 수 있어요."
    },
    "ENTJ": {
        "places": ["뉴욕 🇺🇸", "두바이 🇦🇪", "싱가포르 🇸🇬"],
        "highlight": "마리나베이 샌즈 🏙️",
        "reason": "글로벌 비즈니스와 리더십 감각을 자극하는 도시의 상징이기 때문이에요."
    },
    "ENTP": {
        "places": ["베를린 🇩🇪", "도쿄 🇯🇵", "샌프란시스코 🇺🇸"],
        "highlight": "베를린 예술 거리 🎨",
        "reason": "창의성과 혁신이 넘치는 분위기에서 에너지와 아이디어를 얻을 수 있어요."
    },
    "INFJ": {
        "places": ["아말피 해안 🇮🇹", "브뤼헤 🇧🇪", "우유니 소금사막 🇧🇴"],
        "highlight": "우유니 소금사막 🌌",
        "reason": "신비롭고 내면적인 감성에 깊은 영감을 주는 장소예요."
    },
    "INFP": {
        "places": ["프라하 🇨🇿", "호이안 🇻🇳", "코펜하겐 🇩🇰"],
        "highlight": "프라하 구시가지 🕯️",
        "reason": "동화 같은 분위기에서 감성적인 상상을 펼치기 좋아요."
    },
    "ENFJ": {
        "places": ["로마 🇮🇹", "바르셀로나 🇪🇸", "케이프타운 🇿🇦"],
        "highlight": "바티칸 시국 ⛪",
        "reason": "사람들과의 연결, 역사 속 영성에 깊은 울림을 받을 수 있어요."
    },
    "ENFP": {
        "places": ["리우데자네이루 🇧🇷", "시드니 🇦🇺", "방콕 🇹🇭"],
        "highlight": "시드니 오페라하우스 🎭",
        "reason": "열정적인 분위기에서 다양한 문화를 만끽하며 자유로움을 느낄 수 있어요."
    },
    "ISTJ": {
        "places": ["빈 🇦🇹", "서울 🇰🇷", "브뤼셀 🇧🇪"],
        "highlight": "빈 슈테판 대성당 ⛪",
        "reason": "질서정연하고 전통을 느낄 수 있는 곳에서 편안함을 느껴요."
    },
    "ISFJ": {
        "places": ["부다페스트 🇭🇺", "루체른 🇨🇭", "교토 🇯🇵"],
        "highlight": "루체른 호수 ⛵",
        "reason": "평화롭고 조용한 분위기에서 마음의 안정을 찾을 수 있어요."
    },
    "ESTJ": {
        "places": ["베이징 🇨🇳", "프랑크푸르트 🇩🇪", "워싱턴 D.C. 🇺🇸"],
        "highlight": "워싱턴 국회의사당 🏛️",
        "reason": "사회와 조직의 구조를 느끼며 실용적인 통찰을 얻을 수 있어요."
    },
    "ESFJ": {
        "places": ["파리 🇫🇷", "피렌체 🇮🇹", "밴쿠버 🇨🇦"],
        "highlight": "파리 에펠탑 🗼",
        "reason": "로맨틱하고 정서적인 교감을 나눌 수 있는 분위기가 어울려요."
    },
    "ISTP": {
        "places": ["캐나다 로키산맥 🇨🇦", "아이슬란드 🇮🇸", "호주 태즈메이니아 🇦🇺"],
        "highlight": "아이슬란드 블루라군 ♨️",
        "reason": "자연과 탐험을 즐기면서 고요한 자유를 만끽할 수 있어요."
    },
    "ISFP": {
        "places": ["산토리니 🇬🇷", "보라카이 🇵🇭", "코타키나발루 🇲🇾"],
        "highlight": "산토리니 일몰 🌅",
        "reason": "감각적인 아름다움과 조용한 낭만을 즐기기에 완벽한 장소예요."
    },
    "ESTP": {
        "places": ["라스베이거스 🇺🇸", "홍콩 🇭🇰", "리우데자네이루 🇧🇷"],
        "highlight": "라스베이거스 스트립 🎰",
        "reason": "즉흥적이고 활기찬 에너지로 모험심을 자극해요!"
    },
    "ESFP": {
        "places": ["하와이 🇺🇸", "두브로브니크 🇭🇷", "마요르카 🇪🇸"],
        "highlight": "하와이 와이키키 해변 🌴",
        "reason": "자유롭고 흥겨운 분위기 속에서 즐거움을 가득 누릴 수 있어요."
    }
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
