import numpy as np
import pickle
import streamlit as st
import base64
from streamlit_option_menu import option_menu

regressorRF_CO = pickle.load(open("C:/Users/medha/Desktop/New folder/Random_Forest_model_2.sav", 'rb'))
regressorRF_NOX = pickle.load(open('C:/Users/medha/Desktop/New folder/Random_Forest_model_1.sav','rb'))

def CO_prediction(input_array):
    # Create input array for prediction
    input_array = np.array(input_array)

    # Reshape input array for compatibility with the model
    reshaped_input_array = np.reshape(input_array, (1, 9))

    # Make prediction using the trained model
    prediction2 = regressorRF_CO.predict(reshaped_input_array)

    return prediction2

def NOX_prediction(input_array):
    # Create input array for prediction
    input_array = np.array(input_array)

    # Reshape input array for compatibility with the model
    reshaped_input_array = np.reshape(input_array, (1, 9))

    # Make prediction using the trained model
    prediction1 = regressorRF_NOX.predict(reshaped_input_array)

    return prediction1

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("C:/Users/medha/Desktop/New folder/Praticle/Pages/image (2).jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.alphacoders.com/476/476012.jpg");
background-size: 150%;
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
def main():
    st.title("Prediction of Gas Emissions")
    st.sidebar.header("Configuration")

    select = st.sidebar.radio(label='Choose gas to predict', options=['NOx gas', 'CO gas'])

    if select == 'NOx gas':
        st.title("Prediction of NOx gas")
        col1, col2, col3 = st.columns(3)
        with col1:
            AT = st.text_input('Ambient Temperature')
        with col2:
            AP = st.text_input('Ambient Pressure')
        with col3:
            AH = st.text_input('Ambient Humidity')
        with col1:
            AFDP = st.text_input('Air Filter Difference Pressure')
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

        if st.button("Predict NOx Gas Emissions"):
            # Collect input values
            input_array = [AT, AP, AH, AFDP, GTEP, TIT, TAT, TEY, CDP]

            # Validate input values
            for i in range(len(input_array)):
                if input_array[i] == '':
                    st.error('Please enter all the input values.')
                    break
                try:
                    input_array[i] = float(input_array[i])
                except:
                    st.error('Please enter valid input values.')
                    break
            else:
                # Make prediction
                prediction = NOX_prediction(input_array)

                # Display prediction
                st.success(f'Predicted NOx gas emissions: {prediction[0]:.2f}')

    elif select == 'CO gas':
        st.title("Prediction of CO gas")
        col1, col2, col3 = st.columns(3)
        with col1:
            AT = st.text_input('Ambient Temperature')
        with col2:
            AP = st.text_input('Ambient Pressure')
        with col3:
            AH = st.text_input('Ambient Humidity')
        with col1:
            AFDP = st.text_input('Air Filter Difference Pressure')
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

        if st.button("Predict CO Gas Emissions"):
            # Collect input values
            input_array = [AT, AP, AH, AFDP, GTEP, TIT, TAT, TEY, CDP]

            # Validate input values
            for i in range(len(input_array)):
                if input_array[i] == '':
                    st.error('Please enter all the input values.')
                    break
                try:
                    input_array[i] = float(input_array[i])
                except:
                    st.error('Please enter valid input values.')
                    break
            else:
                # Make prediction
                prediction_1 = CO_prediction(input_array)

                # Display prediction
                st.success(f'Predicted CO gas emissions: {prediction_1[0]:.2f}')


if __name__ == '__main__':
    main()

