import streamlit as st
from PIL import Image

def project_5_page():

    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/img_3.png")
    st.image(image, caption='', use_column_width=True)

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .main {
            padding: 20px;
        }
        .section-header {
            background-color: #f0f0f0;
            padding: 10px;
            margin-top: 20px;
            border-radius: 5px;
        }
        .section-content {
            margin-top: 10px;
            margin-bottom: 20px;
        }
        .sub-header {
            color: #333333;
            font-size: 18px;
            font-weight: bold;
        }
        .text {
            color: #666666;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # CSS styling for a modern look
    st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333333;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .header {
            font-size: 24px;
            color: #333333;
            text-decoration: underline;
            margin-bottom: 20px;
        }
        .sub-header {
            font-size: 20px;
            color: #555555;
            margin-bottom: 10px;
        }
        .text {
            font-size: 16px;
            color: #777777;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title
    st.title('Customer Churn Prediction')

    # Problem
    st.header('Problem')
    st.write(
        'The task is to develop a machine learning model to predict which customers are likely to leave the company. Understanding and anticipating customer churn can help the company take proactive measures to retain customers, reducing revenue loss.')

    # Dataset Description
    st.header('Dataset Description')
    st.write(
        'The dataset contains information about 7043 customers of a hypothetical telecom company. It includes various features such as customer demographics, account information, and services used. The target variable is "Churn", indicating whether the customer left the company.')

    # Purpose of the Project
    st.header('Purpose of the Project')
    st.write(
        'The project aims to predict customer churn, a crucial metric for businesses to understand customer behavior and enhance customer retention strategies.')

    # What has been done
    st.subheader('Project Steps')
    st.write("___")
    st.write('**Data Loading**')
    st.write(
        'Implemented a feature to upload a CSV file containing customer data, enabling seamless data ingestion for analysis.')
    st.write('**Data Preprocessing**')
    st.write(
        '- Handled Missing Values: Columns with more than 40% missing values are dropped. Rows with remaining missing values are also removed.')
    st.write('- Data Type Conversion: Converted the "TotalCharges" column to numeric format.')
    st.write(
        '- Feature Engineering: Created new features like "ServiceCount", "AverageMonthlyBill", and "AverageServiceCost" to enrich the dataset.')
    st.write('**Exploratory Data Analysis (EDA)**')
    st.write(
        'Provided summary statistics, distribution plots for numerical columns, summary tables, and various plots for categorical columns.')
    st.write('**Model Building**')
    st.write('Used Logistic Regression after encoding categorical features to predict customer churn.')
    st.write('**Hyperparameter Optimization**')
    st.write('Used GridSearchCV to find the best hyperparameters for the Logistic Regression model.')
    st.write('**Model Evaluation**')
    st.write('Rigorously evaluated the model using a test set. Displayed a classification report and ROC curve.')

    # Results
    st.header('Results')
    st.write(
        "The model achieved an accuracy of 86%. Precision, Recall, F1-Score: The precision, recall, and F1-score for class 0 (non-churn) were higher compared to class 1 (churn), indicating better performance in predicting customers who did not churn. ROC-AUC: The ROC-AUC score was also calculated to assess the model's ability to distinguish between churn and non-churn classes.The project provides a comprehensive solution for customer churn prediction, integrating data loading, preprocessing, modeling, and evaluation into a user-friendly interface.")
    st.write("___")
    # Interpretation and Recommendations

    st.write(
        'The model performs well in predicting customers who will not churn but is less effective in predicting those who will churn. Recommendations include analyzing feature importance, focusing on customer retention programs, and further model tuning.')

    # Contribution to the Business World
    st.header('Contribution to the Business World')
    st.write(
        'Businesses can leverage the project to analyze customer data, predict churn, and develop targeted strategies to retain customers. The project can help businesses improve customer satisfaction, reduce churn rates, and drive sustainable growth in revenue and market share.Provides valuable insights into customer behavior and factors leading to churn. Enables the company to take proactive measures to retain customers, thus reducing churn rates and increasing customer lifetime value.')

    st.write("")
    st.subheader('Project Demo')
    st.video("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Videos/churn.mov")
    st.markdown("""
                    To see the full demonstration of the project, including the interactive Streamlit application and results, please see the following video:
                    """)

    st.write("")

    st.markdown("Click [here](https://customerchurnapp.streamlit.app/) to try the app.")


