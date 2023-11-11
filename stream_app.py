import streamlit as st
import pickle
import pandas as pd
with open('customer_churn.pkl','rb')as f:
   model=pickle.load(f)
columns=[
   'Gender','Senior Citizen','Partner','Dependents','tenure','Phone Service','Multiple Lines','Internet Service','Online Security','Online Backup','Device Protection','Tech Support','Streaming TV','Streaming Movies','Contract','Paperless Billing','Payment Method','Monthly Charges']
dict = {
    'Male': 1,
    'Female': 0,
    'Yes': 1,
    'No': 0,
    'No phone service': 2,
    'No internet service': 2,
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2,
    'Bank transfer (automatic)': 0,
    'Credit card (automatic)': 1,
    'Electronic check': 2,
    'Mailed check': 3,
    'DSL': 2,
    'Fiber optic': 2,

}
def main():
    with open('css_file.css')as file:
        st.markdown(f'<style>{file.read()}</style>',unsafe_allow_html=True)

    st.markdown("""
    
    <style>
    .st-emotion-cache-cio0dv.ea3mdgi1
    {
    visibility:hidden
    }
    </style>
    """,unsafe_allow_html=True)
    st.image('Churn.png')
    st.markdown("<h2 style='text-align:center;color:black;'>CUSTOMER CHARGE PREDICTION</h2>",unsafe_allow_html=True)
    Gender= st.selectbox("Gender", ['Male','Female'])
    Gender=dict.get(Gender)

    Senior_citizen= st.selectbox("Senior_citizen", ['Yes','No'])

    Senior_citizen=dict.get(Senior_citizen)

    partner=st.selectbox("Partner", ['Yes','No'])
    partner=dict.get(partner)

    Dependents=st.selectbox("Dependents",  ['Yes','No'])
    Dependents=dict.get(Dependents)

    tenure = st.slider('Tenure (months)', 0, 100, 1)

    Phone_Service=st.selectbox("Phone service", ['Yes','No'])
    Phone_Service=dict.get(Phone_Service)


    multiple_lines=st.selectbox("Multiple Lines",['No phone service', 'No', 'Yes'])
    multiple_lines=dict.get(multiple_lines)

    internet_service=st.selectbox("Internet_service",['DSL', 'Fiber optic', 'No'])
    internet_service=dict.get(internet_service)

    online_security=st.selectbox("Online_security",['No', 'Yes', 'No internet service'])
    online_security=dict.get(online_security)

    Online_Backup=st.selectbox('Online backup',['Yes', 'No', 'No internet service'])
    Online_Backup=dict.get(Online_Backup)

    Device_Protection=st.selectbox('Device_protection',['No', 'Yes', 'No internet service'])
    Device_Protection=dict.get(Device_Protection)

    Tech_Support=st.selectbox('Tech support',['No', 'Yes', 'No internet service'])
    Tech_Support=dict.get(Tech_Support)

    Streaming_TV=st.selectbox('Streaming_TV',['No', 'Yes', 'No internet service'])
    Streaming_TV=dict.get(Streaming_TV)

    Streaming_Movies=st.selectbox('Streaming_Movies',['No', 'Yes', 'No internet service'])
    Streaming_Movies=dict.get(Streaming_Movies)

    Contract=st.selectbox('Contract',['Month-to-month', 'One year', 'Two year'])
    Contract=dict.get(Contract)

    Paperless_Billing=st.selectbox("Paperless billing", ['Yes', 'No'])
    Paperless_Billing=dict.get(Paperless_Billing)

    Payment_Method=st.selectbox("Payment_method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'])
    Payment_Method=dict.get(Payment_Method)

    Monthly_Charges= st.number_input("Monthly Charges")

    input = {
        "Gender": Gender,
        "Senior Citizen": Senior_citizen,
        "Partner": partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "Phone Service": Phone_Service,
        "Multiple Lines": multiple_lines,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": Online_Backup,
        "Device Protection": Device_Protection,
        "Tech Support": Tech_Support,
        "Streaming TV": Streaming_TV,
        "Streaming Movies": Streaming_Movies,
        "Contract": Contract,
        "Paperless Billing": Paperless_Billing,
        "Payment Method": Payment_Method,
        "Monthly Charges": Monthly_Charges,

    }
    if st.button('Predict'):
        if Monthly_Charges==0.00:
            st.warning('Please fill all above details correctly !!')
        else:
            st.success('Submitted Succesfully')

            input_df = pd.DataFrame([input], columns=columns)
            st.write(input_df)
            total_charges=model.predict(input_df)
            st.write("<h2 style='text-align:center;color:black;'>Total charge is</h2>",unsafe_allow_html=True)
            st.write(f'<p style="text-align:center;font-size:75px;color:black">{total_charges}</p>',unsafe_allow_html=True)

if __name__ == '__main__':
    main()















