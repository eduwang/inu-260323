import streamlit as st

st.set_page_config(page_title="자기소개", page_icon="👤", layout="centered")

# 헤더
st.title("👤 안녕하세요!")
st.subheader("저는 왕효원입니다.")
st.divider()

# 기본 정보
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/150", caption="프로필 사진", width=150)

with col2:
    st.markdown("### 기본 정보")
    st.markdown("""
- 🎓 **학교**: 인천대
- 📚 **전공**: 수학교육
- 📅 **학번**: 2026
- 📍 **위치**: 인천
    """)

st.divider()

# 자기소개
st.markdown("### 🙋 자기소개")
st.write("""
안녕하세요! 저는 [이름]입니다.
[간단한 자기소개 내용을 여기에 작성하세요.]
""")

st.divider()

# 관심사 / 기술
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 💡 관심 분야")
    st.markdown("""
- 관심 분야 1
- 관심 분야 2
- 관심 분야 3
    """)

with col4:
    st.markdown("### 🛠️ 보유 기술")
    st.markdown("""
- 기술 1
- 기술 2
- 기술 3
    """)

st.divider()

# 연락처
st.markdown("### 📬 연락처")
st.markdown("""
- 📧 이메일: [이메일 주소]
- 🐙 GitHub: [GitHub 링크]
""")

