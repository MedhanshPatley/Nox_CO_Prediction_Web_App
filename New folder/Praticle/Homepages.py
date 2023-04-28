import streamlit as st
import base64
# st.set_page_config(
#     page_title="Multi Pages"

# )
# with st.sidebar:
#        select = st.radio(label='sicsdos',options =['gk gbk',])
                                                                                                       

# st.title("Main Page")
@ st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("C:/Users/medha/Desktop/New folder/Praticle/Pages/image (2).jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1467533003447-e295ff1b0435?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}


# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

text1 = "<h2 style='color: velvet; text-decoration: underline;'>Lets begin the Turbine journey.</h2>"

st.write(text1, unsafe_allow_html=True)

# import streamlit as st


# text2= "<p style='color: white; font-weight: bold; font-family: Arial, sans-serif;'>The dataset comprises 36,733 observations of 11 distinct sensor measurements, which were averaged or summed over the course of an hour. These measurements were taken from a gas turbine located in the northwest region of Turkey. The objective of the study was to investigate the flue gas emissions of CO and NOx (NO + NO2).</p>"


# css = """
# @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap');


# """

# st.write(f'<style>{css}</style>', unsafe_allow_html=True)



# st.markdown(text2, unsafe_allow_html=True)




# text2 = "<p style='color: white; font-weight: bold; font-family: Optima, Arial, sans-serif;'>The dataset comprises 36,733 observations of 11 distinct sensor measurements, which were averaged or summed over the course of an hour. These measurements were taken from a gas turbine located in the northwest region of Turkey. The objective of the study was to investigate the flue gas emissions of CO and NOx (NO + NO2).</p>"


# # text3 = "<p style='color: black;font-weight: bold;'>This study shows how supervised machine learning algorithms may be used to precisely anticipate and analyze NOx and CO emissions from gas turbines. With the aid of these predictive models, engineers and operators can optimize gas turbine operations to lower emissions and increase efficiency, creating a more environmentally friendly and sustainable energy sector.</p>"

# st.markdown(text2, unsafe_allow_html=True)
# st.markdown(text3, unsafe_allow_///ht/ml=True/)
# st.title("Its Turbine Time")
# st.write("The dataset consists of 36733 occurrences of 11 sensor measurements that were averaged or summed over the course of an hour from a gas turbine in Turkey's northwest in order to examine CO and NOx (NO + NO2) flue gas emissions.")
# st.write(" this study shows how supervised machine learning algorithms may be used to precisely anticipate and analyze NOx and CO emissions from gas turbines. With the aid of these predictive models, engineers and operators can optimize gas turbine operations to lower emissions and increase efficiency, creating a more environmentally friendly and sustainable energy sector.")
# # st.sidebar.header("Configuration")

