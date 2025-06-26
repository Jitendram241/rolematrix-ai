
import streamlit as st
import pandas as pd
from itertools import combinations

st.title("⚠️ SoD Conflict Analyzer")

agr_users = st.session_state.get("agr_users")
agr_1251 = st.session_state.get("agr_1251")
sod_rules = st.session_state.get("sod_rules")

if agr_users is not None and agr_1251 is not None and sod_rules is not None:
    sod_set = set([tuple(sorted([r['TCODE_1'], r['TCODE_2']])) for _, r in sod_rules.iterrows()])
    results = []

    for user in agr_users['USER'].unique():
        roles = agr_users[agr_users['USER'] == user]['ROLE'].tolist()
        tcodes = agr_1251[
            (agr_1251['ROLE'].isin(roles)) & 
            (agr_1251['OBJECT'] == 'S_TCODE')
        ]['VALUE'].unique()

        for t1, t2 in combinations(tcodes, 2):
            if tuple(sorted([t1, t2])) in sod_set:
                results.append({'USER': user, 'Tcode 1': t1, 'Tcode 2': t2})

    df_conflicts = pd.DataFrame(results)
    st.write("⚠️ Users with SoD Violations:")
    st.dataframe(df_conflicts)

    if not df_conflicts.empty:
        st.download_button("📥 Download Violations CSV", df_conflicts.to_csv(index=False), "sod_violations.csv")
else:
    st.warning("Upload SoD rules along with user/role files.")
