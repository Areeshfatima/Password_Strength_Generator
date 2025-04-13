# import regular expressions

import re
import streamlit as st

# Page Styling

st.set_page_config(page_title= "Password Strength Checker By Areesha", page_icon= "🔐🔑", layout= "centered")

# Custom CSS

st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {text-align: center !important; margin: auto;}
    .stButton button {width: 25%; background-color: grey; color: black; font-size: 18px;}
    .stButton button:hover {background-color: #blue;}
</style>
""", unsafe_allow_html= True)

# Title and Description

st.title("🔐 Password Strength Generator")
st.write(" ##### Enter your password below to check its security level.🔍")

# make function to check password

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1    #score increased by 1
    else:
        feedback.append("🛡️ Your password must be at least 8 characters long for better security.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔠 Make sure your password contains uppercase (A-Z) and lowercase (a-z) characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔐 Make sure your password contains a number (0-9).")
    
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("🔣 Include at least one special character [!@#$%&*].")

    # Display Password Strength
    if score == 4:
        st.success("🛡️ **Great!** Your password is strong and secure!")
    elif score == 3:
        st.info("⚠️ **Your password is moderate** Add more symbols, numbers, or uppercase letters for better security.")
    else:
        st.error("❌ Weak password detected. Strengthen it by following the tips below 👇")

    # feedback
    if feedback:
        with st.expander("**⚠️ Improve your password for better security!🔐**"):
            for item in feedback:
                st.write(item)

password = st.text_input("**🔑 Enter your password:**", type= "password", help= "🔐 Make sure your password is strong enough to protect your account!💪")

#  Button Working

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please input your password to proceed!")   #show if password empty
