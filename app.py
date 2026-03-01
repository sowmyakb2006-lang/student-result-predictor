import streamlit as st

st.set_page_config(page_title="Student Result Predictor", layout="wide")

# Dark background + glass effect
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

.main-title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    margin-top: -20px;
}

.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    margin-top: 40px;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 Student Result Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Powered Performance Prediction System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>📌 About This Project</h3>
<p>This system predicts whether a student will PASS or FAIL based on:</p>
<ul>
<li>Attendance Percentage</li>
<li>Study Hours</li>
<li>Internal Marks</li>
</ul>
<p>👉 Use the sidebar to go to the Prediction Page.</p>
</div>
""", unsafe_allow_html=True)