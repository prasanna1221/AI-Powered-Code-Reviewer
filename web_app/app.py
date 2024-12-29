import streamlit as st
import subprocess
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from intelligent_suggestions.code_refactor import refactor_code

from intelligent_suggestions.bug_detection import detect_bugs

st.title("AI-Powered Code Reviewer")

uploaded_file = st.file_uploader("Upload your Python code file", type="py")
if uploaded_file:
    code = uploaded_file.read().decode("utf-8")
    st.text_area("Uploaded Code", code, height=200)

    if st.button("Run Static Analysis"):
        flake8_report = subprocess.run(['flake8', '--stdin-display-name', uploaded_file.name], input=code, text=True, capture_output=True)
        st.text("Flake8 Report:")
        st.text(flake8_report.stdout)

    if st.button("Detect Bugs"):
        result = detect_bugs(code)
        st.text(result)

    if st.button("Refactor Code"):
        refactored = refactor_code(code)
        st.text_area("Refactored Code", refactored, height=200)
