import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===== 标题 =====
st.title("🦵 膝关节运动分析（作业版）")

# ===== 生成数据 =====
np.random.seed(42)

t = np.arange(0, 10, 0.01)
phase = (t % 1) / 1

knee_angle = 5 + 15 * np.sin(np.pi * phase) + np.random.randn(len(t))

df = pd.DataFrame({
    "time": t,
    "knee_angle": knee_angle
})

# ===== 显示数据 =====
st.subheader("📊 数据预览")
st.dataframe(df.head(10))

# ===== 计算ROM =====
rom = df["knee_angle"].max() - df["knee_angle"].min()

st.subheader("📏 关节活动范围（ROM）")
st.write(f"ROM = {rom:.2f} 度")

# ===== 画图 =====
st.subheader("📈 膝关节角度变化")

fig, ax = plt.subplots()
ax.plot(df["time"], df["knee_angle"])
ax.set_xlabel("时间 (s)")
ax.set_ylabel("角度 (°)")
ax.set_title("Knee Angle")

st.pyplot(fig)