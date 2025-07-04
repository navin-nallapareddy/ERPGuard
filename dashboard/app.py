import streamlit as st
import pandas as pd
from database.connection import get_connection

conn = get_connection()
cur = conn.cursor()
st.title("ERPGuard Compliance Dashboard")
table = st.selectbox("Select table to view rule results:", ["items_master", "boms", "suppliers", "equipment"])
cur.execute("SELECT * FROM rule_results WHERE table_name = %s", (table,))
data = cur.fetchall()
df = pd.DataFrame(data, columns=['id', 'table_name', 'record_key', 'rule_name', 'status', 'message', 'checked_at'])
st.write(df)