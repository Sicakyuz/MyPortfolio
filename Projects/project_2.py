import streamlit as st
from PIL import Image

def project_2_page():

    image = Image.open("Projects/Images/diabet.png")
    st.image(image, caption='', use_column_width=True)
    # Project Overview
    st.header("Prediction of Diabetes Risk")

    st.write("""
    ## Problem Definition
    Diabetes is a chronic disease that affects millions of people worldwide. Early detection and intervention are crucial to managing the condition and reducing its impact on health. This project aims to develop a predictive model to identify individuals at risk of diabetes based on various health parameters.

    ## Objectives
    - Develop a predictive model to identify individuals at risk of diabetes.
    - Use historical health data on patients' health metrics such as glucose levels, insulin levels, BMI (Body Mass Index), age, and other relevant factors.
    - Enable healthcare professionals to identify individuals at risk of diabetes for early intervention and personalized healthcare management strategies.

    ## Project Steps
    1. **Data Loading and Exploration:** Load the dataset containing historical health data of individuals and perform initial exploration to understand the structure of the data.
    2. **Exploratory Data Analysis (EDA):** Conduct in-depth analysis of the data to gain insights into the distribution and relationships between different variables. Explore categorical and numerical variables, and investigate correlations between variables.
    3. **Feature Engineering:** Handle zero values and missing values, detect and treat outliers, and create new features that may capture important relationships or patterns in the data.
    4. **Model Development:** Split the dataset into training and testing sets, standardize numerical features, and train a Random Forest Classifier, a robust machine learning algorithm capable of handling complex datasets and capturing nonlinear relationships.
    5. **Model Evaluation:** Make predictions using the trained model on the test set, evaluate model performance using metrics such as accuracy, precision, recall, F1 score, and ROC AUC score, and summarize the results in a tabular format to compare the performance of the model.

    ## Results and Conclusion
    - The project identifies strong correlations between "Glucose," "BMI," "Age," and "Outcome" (diabetes risk), indicating their significance in predicting diabetes risk.
    - The Random Forest Classifier achieves an accuracy of 77.9%, precision of 79.5%, recall of 54.4%, F1 score of 64.6%, and an ROC AUC score of 0.731, demonstrating its predictive power.
    - Further feature engineering and experimentation with different models or ensemble techniques could enhance the model's performance.
    - Healthcare practitioners can leverage these insights to better assess diabetes risk factors and implement preventive measures effectively, leading to improved patient outcomes.

    By developing a reliable predictive model, this project aims to contribute to early detection and personalized management of diabetes, ultimately improving the quality of life for individuals at risk.
    """)


