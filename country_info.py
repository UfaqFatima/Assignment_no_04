import streamlit as st
import requests

# API URL
API_URL = "https://restcountries.com/v3.1/name/"

# Page Config
st.set_page_config(page_title="🌍 Country Info Explorer", layout="centered")

st.title("🌐 Country Info Explorer")
st.caption("🔎 Enter any country name and explore its basic information in Urdu!")

# User Input
country = st.text_input("🌍 ملک کا نام درج کریں:")

# When user clicks the button
if st.button("🔍 تلاش کریں"):
    if country:
        try:
            response = requests.get(API_URL + country.strip())

            if response.status_code == 200:
                data = response.json()[0]

                # Extract details
                name = data["name"]["common"]
                flag = data["flags"]["png"]
                capital = data.get("capital", ["N/A"])[0]
                region = data.get("region", "N/A")
                subregion = data.get("subregion", "N/A")
                population = f"{data.get('population', 0):,}"
                area = f"{data.get('area', 0):,} km²"
                currencies = data.get("currencies", {})
                currency_info = next(iter(currencies.values()))
                currency_name = currency_info.get("name", "N/A")
                currency_symbol = currency_info.get("symbol", "")
                languages = ", ".join(data.get("languages", {}).values())

                # Display Info
                st.image(flag, width=180)
                st.markdown(f"### 📍 ملک: {name}")
                st.markdown(f"**🏛 دارالحکومت:** {capital}")
                st.markdown(f"**🌐 علاقہ:** {region} | **📌 ذیلی علاقہ:** {subregion}")
                st.markdown(f"**👥 آبادی:** {population}")
                st.markdown(f"**📏 رقبہ:** {area}")
                st.markdown(f"**💰 کرنسی:** {currency_name} {currency_symbol}")
                st.markdown(f"**🗣 زبانیں:** {languages}")

            else:
                st.error("❌ ملک نہیں ملا! براہ کرم درست نام درج کریں۔")

        except Exception as e:
            st.error(f"⚠️ ایرر آیا: {e}")

    else:
        st.warning("⚠️ براہ کرم ملک کا نام درج کریں!")
#Footer
st.markdown("""
    <hr>
    <p style="text-align: center; color: red; font-size: 16px;">
        <b>💖 Made with Love by UfaqFatima 💖</b>
    </p>
""", unsafe_allow_html=True)