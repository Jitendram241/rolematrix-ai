
import streamlit as st
import pandas as pd

st.title("🛠️ Role Simulator — Impact of Role Removal")

agr_users = st.session_state.get("agr_users")
agr_1251 = st.session_state.get("agr_1251")

if agr_users is not None and agr_1251 is not None:
    selected_user = st.selectbox("Select User", agr_users['USER'].unique())
    user_roles = agr_users[agr_users['USER'] == selected_user]['ROLE'].tolist()
    selected_role = st.selectbox("Select Role to Remove", user_roles)

    all_tcodes = agr_1251[
        (agr_1251['ROLE'].isin(user_roles)) & 
        (agr_1251['OBJECT'] == 'S_TCODE')
    ]['VALUE'].unique()

    remaining_roles = [r for r in user_roles if r != selected_role]
    remaining_tcodes = agr_1251[
        (agr_1251['ROLE'].isin(remaining_roles)) & 
        (agr_1251['OBJECT'] == 'S_TCODE')
    ]['VALUE'].unique()

    lost_tcodes = sorted(set(all_tcodes) - set(remaining_tcodes))

    st.write(f"🧾 Removing `{selected_role}` will revoke access to:")
    st.dataframe(pd.DataFrame({'Lost Tcodes': lost_tcodes}))
else:
    st.warning("Upload data from main page to proceed.")
