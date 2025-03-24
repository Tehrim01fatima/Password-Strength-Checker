import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the Ultimate Password Strength Checker!  
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.  
We will give you helpful tips to create a **strong password** 🔒.
""")

password = st.text_input("Enter Your Password", type="password")
feedback = []
score = 0

if password:
   
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both **uppercase** and **lowercase** characters.")

   
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least **one digit**.")


    if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least **one special character** [!@#$%^&*()].")


    st.markdown("## 🔍 Password Strength Analysis")

    if score == 4:
        st.success("✅ Your Password is **Strong**! 🎉")
    elif score == 3:
        st.warning("🟡 Your Password is **Medium Strength**. It could be stronger.")
    else:
        st.error("🔴 Your Password is **Weak**. Please improve it.")

  
    if feedback:
        st.markdown("### 💡 Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)

else:
    st.info("💡 Please enter your password to get started.")
