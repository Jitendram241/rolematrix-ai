
import streamlit as st
import pandas as pd

st.set_page_config(page_title="RoleMatrix.AI", layout="wide")

st.title("🔐 RoleMatrix.AI — SAP Role & SoD Intelligence")

st.sidebar.header("📁 Upload SAP Files")

agr_users_file = st.sidebar.file_uploader("Upload AGR_USERS.csv", type="csv")
agr_1251_file = st.sidebar.file_uploader("Upload AGR_1251.csv", type="csv")
sod_rules_file = st.sidebar.file_uploader("Upload SoD_RULES.csv", type="csv")

if agr_users_file and agr_1251_file:
    st.session_state["agr_users"] = pd.read_csv(agr_users_file)
    st.session_state["agr_1251"] = pd.read_csv(agr_1251_file)
    if sod_rules_file:
        st.session_state["sod_rules"] = pd.read_csv(sod_rules_file)
        st.success("✅ SoD Rules loaded.")
    st.success("✅ Files loaded successfully. Navigate using the sidebar.")
else:
    st.warning("👈 Please upload AGR_USERS and AGR_1251 files to proceed.")
