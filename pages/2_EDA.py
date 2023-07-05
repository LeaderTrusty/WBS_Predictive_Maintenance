import streamlit as st

# st.header('Hoho')



from streamlit_pandas_profiling import st_profile_report

# with open(r'/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/data/report.html', 'r') as f:
#     html = f.read()

with open(r'C:\Users\arbab\Documents\Repositories\WBS_Predictive_Maintenance\data\report.html', 'r') as f:
    html = f.read()
    
st.components.v1.html(html=html, height=1000, scrolling=True)