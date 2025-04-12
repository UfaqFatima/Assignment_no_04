import streamlit as st
import qrcode  # type: ignore
from PIL import Image
from io import BytesIO
# Page settings
st.set_page_config(page_title="QR Code Generator", layout="centered")
st.title("🔳 Ultimate QR Code Generator")
st.write("Enter any text or link to generate a QR code.")

# User input
data = st.text_input("Enter your text or URL here:", "https://www.google.com")

# Button to generate QR code
if st.button("Generate QR Code"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Convert QR code to PIL image
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Convert image to bytes for Streamlit
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Show QR code image
    st.image(byte_im, caption="Here is your QR Code!", use_container_width=False)

    # Download button
    st.download_button(
        label="📥 Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png"
    )
# Footer
st.markdown(
    "<div style='text-align: center; padding: 10px; color: #FF0000;'>Made with love by Ufaq Fatima🚀</div>",
    unsafe_allow_html=True
)
