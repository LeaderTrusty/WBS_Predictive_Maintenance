import pandas as pd
import pandas_profiling
import streamlit as st
from PIL import Image
st.set_page_config(layout='wide')


st.markdown("<h1 style='text-align: center; background-color: #19376D; color: #A5D7E8;'>Eliminate surprises, maximize reliability!</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; background-color: #19376D; color: white;'>Start every day with predictive analytics and zero surprises with SmartSignal from OHM-Group. SmartSignal is an integral part of a predictive maintenance strategy that can detect and prevent equipment failures. Drive improved reliability, maximum efficiency and reduced maintenance costs.</h3>", unsafe_allow_html=True)

image = Image.open(r'C:\Users\arbab\Documents\Repositories\WBS_Predictive_Maintenance\image\Global Networks 2030 Banner Image.jpeg')
st.image(image, caption='Sunrise by the mountains')


# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
#         width: 400px;
#     }
#     [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
#         width: 400px;
#         margin-left: -400px;
#     }
    
#     </style>
    
#     """,
    
#     unsafe_allow_html=True
# )

# from streamlit_pandas_profiling import st_profile_report

# # with open(r'/home/hristo/Documents/WBS_Data_Science/WBS_Predictive_Maintenance/data/report.html', 'r') as f:
# #     html = f.read()

# with open(r'C:\Users\arbab\Documents\Repositories\WBS_Predictive_Maintenance\data\report.html', 'r') as f:
#     html = f.read()


    

    
#     tab0, tab1 = st.tabs(['Introduction', 'EDA'])

# with tab0:

#     container = st.container()
#     container.title(":blue[Eliminate surprises, maximize reliability]")
    
#     container.subheader("Start every day with predictive analytics and zero surprises with SmartSignal from GE Digital. SmartSignal is an integral part of a predictive maintenance strategy that can detect and prevent equipment failures. Drive improved reliability, maximum efficiency and reduced maintenance costs based on over 340 performance Digital Twin blueprints.")

#     st.write("This is inside too")
    
# #    st.components.v1.html(html=html, height=500, scrolling=True)

# with tab1:

#     # online

#     # offline
#     st.components.v1.html(html=html, height=1000, scrolling=True)
    
    
    


# # Set container background color using CSS styling
# st.markdown(
#      """
#      <style>
#      .container {
#          background-color: #F0F0F0;  /* Replace with your desired background color */
#          padding: 20px;
#      }
#      </style>
#      """,
#     unsafe_allow_html=True,
# )

# Create a container
# container = st.container()

# # Add content to the container
# container.title(":blue[Eliminate surprises, maximize reliability]")
# container.subheader("Start every day with predictive analytics and zero surprises with SmartSignal from GE Digital. SmartSignal is an integral part of a predictive maintenance strategy that can detect and prevent equipment failures. Drive improved reliability, maximum efficiency and reduced maintenance costs based on over 340 performance Digital Twin blueprints.")
# st.write("This is inside too")
