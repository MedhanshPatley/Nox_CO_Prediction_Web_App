# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st
import base64


regressorRF_CO = pickle.load(open("C:/Users/medha/Desktop/New folder/Random_Forest_model_2.sav", 'rb'))





#creating the function
def CO_prediction(input_array):
  
    

    # Create input array for prediction
    input_array = np.array(input_array)

    # Scale input values using the same scaler object used during training
    # scaled_input_array = scaler.transform(input_array)

    # Reshape input array for compatibility with the model
    reshaped_input_array = np.reshape(input_array, (1, 9))

    # Make prediction using the trained model
    prediction2 = regressorRF_CO.predict(reshaped_input_array)
    
    # Print the predicted values

    print("Predicted NOX value: ", prediction2)
 
    
    return prediction2
   
@ st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("C:/Users/medha/.spyder-py3/Deployment/image (2).jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.alphacoders.com/476/476012.jpg");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}


[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Prediction of CO Gas")
st.sidebar.header("Configuration")



def main():
    
    
    
    
    
    with st.sidebar:
       select = st.radio(label='Predicting NOX CO gas using Various Maching Learning Models',options =['Prediction CO gas',
                                                                                                       ], )
        
       if select == 'Prediction CO gas':
           
           st.title("Prediction CO gas")
            
    col1,col2,col3= st.columns(3)
    with col1:
           AT = st.text_input('Ambient Temperature')
           

    with col2:
            AP = st.text_input('Ambient Pressure')
    with col3:
            AH = st.text_input('Ambient Humidity')
    with col1:
            AFDP = st.text_input('Air Filter Difference Pressure ')
    with col2:
            GTEP = st.text_input('Gas Turbine Exhaust Pressure')
    with col3:
            TIT = st.text_input('Turbine Inlet Temperature')
    with col1:
            TAT = st.text_input('Turbine After Temperature')
    with col2:
            TEY = st.text_input('Turbine Energy Yield')
    with col3:
            CDP = st.text_input('Compressor Discharge Pressure')
            
            # getting the input data from the user
        # AT AP AH AFDP GTEP TIT TAT TEY CDP
       
    
        # code for prediction
    CO_RF = ''
    
        # creating a button for prediction
    if st.button('CO predicted VALUES'):
            CO_RF = CO_prediction([[AT, AP, AH, AFDP, GTEP, TIT, TAT, TEY, CDP]])
    
    st.success(CO_RF)

if __name__ == '__main__':
    main()