import streamlit as st
import langchainhelper
st.title("Software service product information")
software_company=st.sidebar.selectbox("Pick a company",("TCS","WIPRO","MICROSOFT","APPLE","AMAZON"))

if software_company:
    response=langchainhelper.generate_software_servicename(software_company)
    st.header(response['service'])
    Domain_name=response['Domain_name'].split(",")
    st.write("***Domain services***")
    for item in Domain_name:
        st.write(item)


