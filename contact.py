import streamlit as st



def contact_page():
    st.title("Contact Me")
    st.markdown(
        """
        <p>If you have any questions or would like to get in touch, please feel free to reach out to me via email or fill out the contact form below.</p>
        <p>Email: <a href="mailto:cigdem.sicakyuz@gmail.com">cigdem.sicakyuz@gmail.com</a></p>
        """, unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.subheader("Contact Form")

    # Contact form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        if not name or not email or not message:
            st.error("Please fill out all fields.")
        else:
            # Here, you could add code to send the email or save the message
            st.success("Thank you for your message. I will get back to you soon.")

    # Styling for form elements
    st.markdown(
        """
        <style>
        .stTextInput > div > div > input {
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .stTextArea > div > div > textarea {
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .stButton > button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True
    )



