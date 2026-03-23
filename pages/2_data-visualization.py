import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# 한글 폰트 설정
font_path = Path(__file__).resolve().parents[1] / "fonts" / "NanumGothic-Bold.ttf"
font_manager.fontManager.addfont(str(font_path))
font_name = font_manager.FontProperties(fname=str(font_path)).get_name()

matplotlib.rcParams['font.family'] = font_name
matplotlib.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="데이터 시각화", page_icon="📊", layout="wide")
st.title("📊 데이터 시각화 예제")
st.divider()

# ── 1. 막대 그래프 (Plotly) ──────────────────────────────────────────
st.subheader("1. 월별 평균 기온 (막대 그래프)")

months = ["1월", "2월", "3월", "4월", "5월", "6월",
          "7월", "8월", "9월", "10월", "11월", "12월"]
temps = [-2.4, 0.4, 5.7, 12.5, 17.8, 22.2, 25.7, 26.4, 21.2, 14.5, 7.2, 0.8]

df_temp = pd.DataFrame({"월": months, "평균 기온 (°C)": temps})

fig1 = px.bar(
    df_temp, x="월", y="평균 기온 (°C)",
    title="인천 월별 평균 기온",
    color="평균 기온 (°C)",
    color_continuous_scale="RdYlBu_r",
    labels={"월": "월", "평균 기온 (°C)": "평균 기온 (°C)"},
)
fig1.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ── 2. 선 그래프 (Plotly) ────────────────────────────────────────────
st.subheader("2. 과목별 성적 추이 (선 그래프)")

weeks = [f"{i}주차" for i in range(1, 9)]
np.random.seed(42)
df_score = pd.DataFrame({
    "주차": weeks,
    "수학": np.clip(np.cumsum(np.random.randint(-5, 10, 8)) + 60, 0, 100),
    "영어": np.clip(np.cumsum(np.random.randint(-5, 10, 8)) + 65, 0, 100),
    "과학": np.clip(np.cumsum(np.random.randint(-5, 10, 8)) + 55, 0, 100),
})

fig2 = px.line(
    df_score.melt(id_vars="주차", var_name="과목", value_name="점수"),
    x="주차", y="점수", color="과목",
    title="주차별 과목 성적 추이",
    markers=True,
)
fig2.update_layout(yaxis_range=[0, 100])
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── 3. 파이 차트 (Plotly) ────────────────────────────────────────────
st.subheader("3. 전공별 학생 비율 (파이 차트)")

majors = ["수학교육", "영어교육", "체육교육", "미술교육", "음악교육"]
counts = [120, 95, 110, 80, 75]

fig3 = px.pie(
    values=counts, names=majors,
    title="전공별 학생 비율",
    hole=0.3,
)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ── 4. 히스토그램 (Matplotlib) ───────────────────────────────────────
st.subheader("4. 시험 점수 분포 (히스토그램)")

np.random.seed(7)
scores = np.random.normal(loc=72, scale=12, size=200).clip(0, 100)

fig4, ax = plt.subplots(figsize=(8, 4))
ax.hist(scores, bins=20, color="steelblue", edgecolor="white", alpha=0.85)
ax.set_title("시험 점수 분포", fontsize=14)
ax.set_xlabel("점수")
ax.set_ylabel("학생 수")
ax.axvline(scores.mean(), color="red", linestyle="--", label=f"평균: {scores.mean():.1f}점")
ax.legend()
st.pyplot(fig4)

st.divider()

# ── 5. 산점도 (Plotly) ───────────────────────────────────────────────
st.subheader("5. 공부 시간 vs 시험 점수 (산점도)")

np.random.seed(10)
study_hours = np.random.uniform(1, 10, 80)
exam_scores = (study_hours * 7 + np.random.normal(0, 8, 80)).clip(0, 100)

df_scatter = pd.DataFrame({"공부 시간 (시간)": study_hours, "시험 점수": exam_scores})

fig5 = px.scatter(
    df_scatter, x="공부 시간 (시간)", y="시험 점수",
    title="공부 시간과 시험 점수의 관계",
    trendline="ols",
    color_discrete_sequence=["darkorange"],
)
st.plotly_chart(fig5, use_container_width=True)
