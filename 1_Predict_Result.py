import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "..", "student_model.pkl")
model = pickle.load(open(model_path, "rb"))

# Dark Gradient Background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

div.stButton > button {
    background-color: #00c6ff;
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 10px 24px;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #0072ff;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Predict Student Result")

# Sliders inside columns
col1, col2, col3 = st.columns(3)

with col1:
    attendance = st.slider("Attendance (%)", 0, 100)

with col2:
    study_hours = st.slider("Study Hours per Day", 0, 10)

with col3:
    internal_marks = st.slider("Internal Marks", 0, 100)

if st.button("🚀 Predict Now"):

    input_data = pd.DataFrame(
        [[attendance, study_hours, internal_marks]],
        columns=["attendance", "study_hours", "internal_marks"]
    )

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("🎉 Student is likely to PASS")
        result_color = "#00ff88"
    else:
        st.error("❌ Student is likely to FAIL")
        result_color = "#ff4b4b"

    # Graph Section
    fig, ax = plt.subplots()

    values = [attendance, study_hours, internal_marks]
    labels = ["Attendance", "Study Hours", "Internal Marks"]

    bars = ax.bar(labels, values)

    # Styling Graph
    ax.set_facecolor("#1e1e1e")
    fig.patch.set_facecolor("#1e1e1e")

    ax.set_title("Student Performance Overview", color="white", fontsize=16)
    ax.set_ylabel("Values", color="white")
    ax.tick_params(colors='white')

    # Color bars dynamically
    for bar in bars:
        bar.set_color(result_color)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2,
                height + 1,
                f'{height}',
                ha='center',
                color='white')

    st.pyplot(fig)