import pandas as pd
import streamlit as st

from erpguard.compliance_summary import generate_summary
from erpguard.database.loader import load_dataframe
from erpguard.validation.rules_engine import run_rules

st.title("ERPGuard Dashboard")

st.sidebar.header("Upload CSV Data")
items_file = st.sidebar.file_uploader("Items master", type="csv")
suppliers_file = st.sidebar.file_uploader("Suppliers", type="csv")
equipment_file = st.sidebar.file_uploader("Equipment", type="csv")

if st.sidebar.button("Load and Run"):
    if items_file:
        items_df = pd.read_csv(items_file)
        load_dataframe(items_df, "items_master")
    if suppliers_file:
        suppliers_df = pd.read_csv(suppliers_file)
        load_dataframe(suppliers_df, "suppliers")
    if equipment_file:
        equipment_df = pd.read_csv(equipment_file)
        load_dataframe(equipment_df, "equipment")
    run_rules()
    st.sidebar.success("Data loaded and rules executed")

summary = generate_summary()
for rule, data in summary.items():
    passes = data.get("PASS", 0)
    fails = data.get("FAIL", 0)
    st.write(f"**{rule}**: {passes} pass, {fails} fail")
