import streamlit as st
from PIL import Image

def project_3_page():


    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/reviews.jpeg")
    st.image(image, caption='', use_column_width=True)
    st.header('E-Commerce Review Analysis and Classification Using Machine Learning Models')


    st.write('---')

    st.subheader('Project Overview')
    st.markdown("""
        E-commerce is widely used worldwide, and customer reviews can significantly impact potential customers. Analyzing customer reviews is crucial for firms to understand customer needs and desires, enhancing their profitability. This project aims to analyze user reviews from airline customers and classify these reviews using text mining and machine learning techniques. The steps involved include cleaning and preprocessing the user reviews, performing sentiment analysis, and classifying the reviews using various machine learning models. Additionally, hypothesis testing and visualization are conducted on the data to derive meaningful insights.
        """)

    st.write('---')

    st.subheader('Detailed Project Steps')

    st.subheader('1. Data Collection and Loading:')
    st.markdown("""
        - User reviews are collected from various e-commerce platforms. The data includes review text, ratings, and other relevant metadata.
        - The collected data is loaded into the system using Pandas for further analysis.
        """)

    st.subheader('2. Data Cleaning and Preprocessing:')
    st.markdown("""
        - **Text Cleaning:** Removing special characters, punctuation, and unnecessary whitespaces from the review text.
        - **Tokenization:** Splitting the text into individual tokens (words).
        - **Stop Words Removal:** Removing common stop words that do not contribute much to the sentiment or meaning of the text.
        - **Lemmatization/Stemming:** Reducing words to their base or root form to normalize the text.
        """)

    # Add more detailed steps for each stage...

    st.write('---')

    st.subheader('Deployment and User Interface')
    st.markdown("""
        - **Streamlit Application:** Developing an interactive Streamlit application to allow users to input new reviews and get sentiment analysis and classification results in real-time.
        - **Deployment:** Deploying the Streamlit application on Streamlit for accessibility and scalability.
        """)

    st.write('---')

    st.subheader('Importance and Benefits of the Project')
    st.markdown("""
        This project provides valuable insights into user sentiments and opinions, which can help e-commerce platforms improve their services and customer satisfaction. The ability to automatically classify and analyze reviews enables businesses to quickly identify and address customer concerns, enhance product offerings, and make data-driven decisions.
        """)

    st.write('---')

    st.subheader('Conclusion')
    st.markdown("""
        By combining text mining, sentiment analysis, and machine learning techniques, this project offers a comprehensive solution for analyzing and classifying e-commerce reviews. The use of interactive visualizations and a user-friendly interface ensures that the results are accessible and interpretable, adding significant value to the analysis process.
        """)

    st.subheader('Project Demo')
    st.markdown("""
            To see the full demonstration of the project, including the interactive Streamlit application and results, please see the following video:
            """)
    st.markdown("""
            [Watch the video on Google Drive](https://drive.google.com/file/d/1vOMEd_m3s_DTNirt2MJ3NIGlqV_hS4PG/view?usp=share_link)
            """)

    st.markdown("<h5></i>Click here to see the link and download the application \U0001F447</i></h5>",
                unsafe_allow_html=True)

    st.markdown("**[App](https://sentiment06.streamlit.app/)**", unsafe_allow_html=True)
