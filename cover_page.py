import streamlit as st
from PIL import Image
import numpy as np

def apply_color_filter(image, color, strength):
    """
    Applies a color filter to an image.

    Args:
    - image: The input image.
    - color: The color of the filter as a tuple (R, G, B).
    - strength: The strength of the filter, a value between 0 and 1.

    Returns:
    - The filtered image.
    """
    # Convert image to numpy array
    img_array = np.array(image)

    # Apply color filter
    filtered_img_array = img_array * (1 - strength) + np.array(color) * strength
    filtered_img_array = np.clip(filtered_img_array, 0, 255).astype(np.uint8)

    # Convert back to PIL image
    filtered_image = Image.fromarray(filtered_img_array)

    return filtered_image

def cover_page():
    st.title("Welcome to My Portfolio")
    st.write("This is the cover page of my interactive portfolio.")

    # Load image
    image_path = "//Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/pexels-thepaintedsquare-3361483.jpg"
    img = Image.open(image_path)

    # Resize image
    new_height = int(img.height / 2)
    img_resized = img.resize((img.width, new_height))

    # Apply color filter
    color = (255, 150, 150)  # Warm color (e.g., red)
    strength = 0.2  # Filter strength
    img_filtered = apply_color_filter(img_resized, color, strength)

    # Display filtered image
    st.image(img_filtered, caption="", width=int(img_filtered.width / 2), use_column_width=True)

    # Resmin boyutunu kartın genişliği ile aynı yapma
    with st.container():
        st.write("")
        st.markdown(
            """
            <style>
                .rainbow-divider {
                    width: 100%;
                    height: 1px;
                    background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
                    margin: 20px 0;
                }
            </style>
            <div class="rainbow-divider"></div>
            """,
            unsafe_allow_html=True
        )
    # Expander oluşturma

        # About Me Section

    st.header("About Me")
    st.write("I am a proactive and self-driven professional, always ready to take responsibility and solve problems with a hands-on approach fueled by my insatiable desire to learn. My passion for data science has been present since my academic years and has only grown since then...")
    st.markdown("""
    <details>
    <summary><span style="color: blue;">Read more</span></summary>
      <p>I am a proactive and self-driven professional, always ready to take responsibility and solve problems with a hands-on approach fueled by my insatiable desire to learn. My passion for data science has been present since my academic years and has only grown since then.</p>
      <p>I have a strong command of exploratory data analysis (EDA), data cleaning, data manipulation, data visualization, and feature engineering, data modeling in Python, using libraries such as NumPy, SciPy, Pandas, Scikit-Learn, Matplotlib, Seaborn, and Plotly. Additionally, I am proficient in SQL.</p>
      <p>My extensive experience includes data preparation, descriptive data analysis, A/B testing, and both supervised and unsupervised machine learning modeling. I also have a robust academic background, having conducted numerous analyses and research projects throughout my academic career.</p>
    </details>
    """, unsafe_allow_html=True)
    st.subheader("")
    st.markdown(
        """
        <style>
            .rainbow-divider {
                background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
                height: 3px;
                margin: 20px 0;
                border: none;
            }
        </style>
        """
        , unsafe_allow_html=True)

    st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)
    with st.expander("Technical Skills"):
        # Teknik becerileri madde madde listeleme
        st.markdown("""
        - **Programming Language:** Python, R (strong), C#, Java, Android-401 (basic), Big Query (Google Cloud)
        - **IDE / Tools:** PyCharm, Jupyter, VsCode Notebook
        - **Version Control System:** Git, GitHub
        - **Database Management:** MS SQL, MS Excel, MS Access (Strong), Firebase (basic)
        - **Python Libraries:** NumPy, SciPy, Pandas, Scikit-Learn, Matplotlib, Seaborn, and Plotly
        - **Data Visualization Tools:** Microsoft Power BI, Streamlit
        - **Machine Learning Algorithms:** Linear Regression, Logistic Regression, CART, SVM, KNN, Random Forests, Gradient Boosting Algorithms (GBM, XGBoost, LightGBM, CatBoost), K-Means, PCA
        - **Deep Learning:** NLTK, WordCloud
        - **Time Series:** ARIMA, SARIMAX
        - **Other PC Software:** SPSS, IGrafx, Arena Simulation, MS Project, Lingo, Visio
        """)


    st.markdown("<h2>Certificates</h2>", unsafe_allow_html=True)
    with st.expander("Certificates"):
        # Teknik becerileri madde madde listeleme
        st.markdown("""
        - Data Scentst (2024l): Muul Data Scientist 14. Bootcamp
        - Queryng MS SQL
        - Natural Language Processng Time Seres
        - Web Scrapng wth Selenum and BeatfulSoup
        - Streamlt
        - Git-GtHub
        - Qualty Audit (2022): IS0- 9001,14001,45001,50001, Sgmacert (FQC), Ankara, Turkey.
        - European Unon Project Wrtng, 01.05.2014 -05.05.2014, from AB-lan n Kavaklıdere, Ankara, Turkey .
        - Qualty Engneerng, 16.12.2019 -16.01.2020, Blgnet Academy, Adana, Turkey.
        - C Sharp Programmng (22.01.2019 -28.04.2019), Platon Informaton Academy, Adana, Turkey.
        - MSSQL Database, (22.01.2019 -28.04.2019), Platon Informaton Academy, Adana, 22.01.2019 -28.04.2019, Turkey
        - Entrepreneurship, 10.07.2017 -24.07.2017,Kosgeb, Adana, Turkey.
        - Appled Entrepreneurshp Training (2017), Entrepreneurshp Ecosystem Assocaton (GED), Çukurova Development Agency, Adana, Turkey.
                    """)


