import streamlit as st
from PIL import Image

def project_6_page():
    # Set page configuration

    # Title and Introduction
    st.title("House Price Prediction")
    st.write("""
    This project focuses on predicting house prices in a specific American state based on sales data from 2016 and 2017. By analyzing historical sales prices and relevant property features, we aim to estimate future property values and provide valuable insights for buyers, sellers, and real estate professionals.
    """)

    # Display Project Image
    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/haus.jpeg")
    st.image(image, caption='', use_column_width=True)

    # Project Objectives
    st.header("Objectives")
    st.write("""
    1. **Analyze Historical Data:** Examine sales data from 2016 and 2017 to identify trends and patterns.
    2. **Predict Future Prices:** Build a predictive model to estimate future house prices based on historical sales and property features.
    3. **Provide Actionable Insights:** Deliver insights that assist in decision-making for real estate stakeholders.
    """)

    # Methodology
    st.header("Methodology")
    st.write("""
    **1. Dataset Preparation:**
       - **Initial Examination:** Assess the dataset for accuracy, including checking for missing values and inconsistencies.
       - **Data Cleaning:** Clean and preprocess the data to ensure it is ready for analysis.

    **2. Exploratory Data Analysis (EDA):**
       - **Feature Distribution:** Analyze key variables such as SALE_PRICE, SQUARE_FEET, and YEAR_BUILT.
       - **Descriptive Statistics:** Generate statistics to summarize the dataset.

    **3. Investigating Relationships:**
       - **Correlation Analysis:** Examine correlations between SALE_PRICE and other features.
       - **Categorical Analysis:** Assess the impact of categorical features like NEIGHBORHOOD on property prices.

    **4. Anomaly Detection:**
       - **Outlier Identification:** Detect and evaluate outliers to understand their impact on the model.

    **5. Predictive Modeling:**
       - **Model Selection:** Employ **RandomForestRegressor** to create a robust predictive model.
       - **Performance Metrics:** Use metrics such as Mean Squared Error (MSE) and R-squared (R²) to evaluate model performance.
       - **Hyperparameter Tuning:** Optimize the model using **GridSearchCV**.
       - **Feature Importance Analysis:** Determine which features are most influential in predicting house prices.
    """)

    # Dataset Details
    st.header("Dataset Details")
    st.write("""
    The dataset includes sales data for houses from 2016 and 2017, encompassing various property attributes such as dimensions, sale prices, and other relevant features. This comprehensive dataset provides a solid foundation for analysis and prediction.
    """)

    # Key Findings
    st.header("Key Findings")
    st.write("""
    - **Influential Factors:** Identified key factors affecting house prices, including SQUARE_FEET and PROPERTY_TYPE.
    - **Correlations:** Found significant correlations with features such as LOCATION and YEAR_BUILT.
    - **Model Performance:** Achieved an R² score of 0.85, reflecting strong predictive accuracy.
    """)

    # Visualizations
    st.header("Visualizations")
    st.write("""
    **Correlation Heatmap:** Visual representation of relationships between key variables.
    **Feature Importance Chart:** Highlights the impact of different features on the model's predictions.
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    This project delivers a detailed analysis of house prices based on historical sales data. By applying advanced statistical and machine learning techniques, we provide a reliable tool for predicting future property values and understanding market dynamics.
    """)

    # Significance
    st.header("Significance")
    st.write("""
    Accurate predictions and insights into house prices are crucial for making informed real estate decisions. This project offers valuable information that can help stakeholders make strategic choices in the housing market.
    """)



# Business Benefits of House Price Prediction Projects

    st.header("Business Benefits of House Price Prediction Projects")
    st.write("""
    House price prediction projects can provide significant benefits to the business world in various ways:

    **1. Supports Investment Decisions**
    - **Risk Reduction:** Helps investors minimize risks by predicting future property values based on historical data.
    - **Return on Investment (ROI):** Enables investors to optimize returns by making informed purchasing decisions.

    **2. Market Analysis and Strategy Development**
    - **Understanding Market Trends:** Provides insights into market trends and price movements to align business strategies.
    - **Competitive Analysis:** Helps analyze competitors' pricing strategies and market positions.

    **3. Enhances Sales and Marketing Strategies**
    - **Targeting:** Improves targeting by identifying key demographics and market segments.
    - **Pricing Strategies:** Assists in setting accurate prices for properties to attract potential buyers.

    **4. Financial Planning and Management**
    - **Budgeting:** Helps companies manage budgets and financial planning by predicting property values.
    - **Valuation:** Provides precise valuations for assets on the balance sheet and investment assessments.

    **5. Risk Management and Insurance**
    - **Insurance Coverage:** Aids in determining insurance policy coverage and premiums based on predicted property values.
    - **Risk Analysis:** Analyzes the impact of market fluctuations and economic changes on property values.

    **6. Customer Relationships and Satisfaction**
    - **Informed Decisions:** Provides customers with reliable information to make better purchasing or selling decisions.
    - **Consulting:** Supports real estate consultants with valuable data and insights for advising clients.

    **7. Investment in AI and Data Analytics**
    - **Technology Utilization:** Leverages modern technologies like AI and data analytics to gain a competitive edge.
    - **Innovative Approaches:** Enhances business processes with data-driven insights and predictive models.

    **8. Real Estate Development and Project Management**
    - **Project Valuation:** Assists in assessing the financial value of new real estate projects.
    - **Demand Forecasting:** Helps developers understand regional demand and optimize project strategies.
    """)

    st.markdown("""
                    To see the full demonstration of the project, please click the following link:
                    """)

    st.write("")

    st.markdown(" [Click here](https://github.com/Sicakyuz/NYC_project/blob/master/nya-project2.ipynb/) ")
