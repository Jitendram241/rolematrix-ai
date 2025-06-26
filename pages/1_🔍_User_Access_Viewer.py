
import streamlit as st
import pandas as pd

st.title("🔍 Explore SAP User Access")

agr_users = st.session_state.get("agr_users")
agr_1251 = st.session_state.get("agr_1251")

if agr_users is not None and agr_1251 is not None:
    selected_user = st.selectbox("Select User", agr_users['USER'].unique())
    user_roles = agr_users[agr_users['USER'] == selected_user]['ROLE'].tolist()
    user_tcodes = agr_1251[
        (agr_1251['ROLE'].isin(user_roles)) & 
        (agr_1251['OBJECT'] == 'S_TCODE')
    ]['VALUE'].unique()

    st.write(f"User **{selected_user}** has roles: {user_roles}")
    st.dataframe(pd.DataFrame({'Tcodes': sorted(user_tcodes)}))

    tcode_search = st.text_input("🔎 Search Roles by Tcode")
    if tcode_search:
        roles = agr_1251[
            (agr_1251['OBJECT'] == 'S_TCODE') & 
            (agr_1251['VALUE'].str.upper() == tcode_search.upper())
        ]['ROLE'].unique()
        st.write(f"Roles containing `{tcode_search}`:")
        st.dataframe(roles)
else:
    st.warning("Upload data from main page to proceed.")
