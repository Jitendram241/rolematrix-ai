import streamlit as st
import os

# 🌐 Simulated Login
if 'user_email' not in st.session_state:
    st.session_state['user_email'] = st.text_input("Enter your email to continue:")
    st.stop()

# Simulated Pro access
if st.session_state['user_email'] == "pro@user.com":
    st.session_state['is_pro'] = True
else:
    st.session_state['is_pro'] = False

st.title("📊 RoleMatrix.AI - SAP Role Access Analyzer")
st.sidebar.success(f"Logged in as: {st.session_state['user_email']}")