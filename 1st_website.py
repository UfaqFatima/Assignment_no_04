import streamlit as st

# Website Title
st.set_page_config(page_title="My First Streamlit Website", page_icon="🌸")

# Header
st.title("Welcome to My Streamlit Website! 💖")
st.write("This is a simple web app built using Python and Streamlit.")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.header("Home Page 🏠")
    st.write("Enjoy this refreshing greenery view! 🌿🍃✨")

    # Beautiful Green Nature Image for Home Page
    home_image = "https://images.unsplash.com/photo-1563298723-dcfebaa392e3"
    st.image(home_image, caption="Beautiful Green Forest 🌳🍀", use_container_width=True)

# About Page
elif page == "About":
    st.header("About Me 👩‍💻")
    st.write("Hi! I'm a full stack developer,and My name is Syeda Farzana Shah and I love building web apps with Streamlit, I have a cooding skills very well.")

    # Girls-Themed Image for About Page
    about_image = "https://images.unsplash.com/photo-1524255684952-d7185b509571"
    st.image(about_image, caption="Aesthetic Girl Developer 💕", use_container_width=True)

# Contact Page
elif page == "Contact":
    st.header("Contact Me 📩")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success(f"Thanks {name}, your message has been sent!")
        else:
            st.error("Please fill in all fields.")

# Stylish Pink Footer for Girls' Theme
st.markdown("""
    <hr>
    <p style="text-align: center; color: red; font-size: 16px;">
        <b>💖 Made with Love by UfaqFatima 💖</b>
    </p>
""", unsafe_allow_html=True)