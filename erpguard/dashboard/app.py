import streamlit as st

from erpguard.compliance_summary import generate_summary


st.title("ERPGuard Dashboard")
summary = generate_summary()

for rule, data in summary.items():
    passes = data.get("PASS", 0)
    fails = data.get("FAIL", 0)
    st.write(f"**{rule}**: {passes} pass, {fails} fail")
