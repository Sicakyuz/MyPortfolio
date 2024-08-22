import streamlit as st
from PIL import Image
def project_4_page():


    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/img_2.png")
    st.image(image, caption='', use_column_width=True)
    st.header("Customer Analytics and Customer Lifetime Value Prediction")

    # Title and Introduction
    st.subheader("The Importance of Project")
    st.info("Customer Relationship Management (CRM) is a crucial strategy for optimizing customer interactions and establishing long-term relationships in businesses. It consists of strategic, operational, and analytic CRM categories, with the primary goal of establishing enduring relationships with valuable customers. ")
    st.markdown("""
            - Customer-focused marketing is essential in today's business environment, focusing on understanding customer needs, targeting specific markets, and offering compelling value propositions. 
            - Analyzing customer behavior is crucial for market assessment, forecasting future trends, and optimizing resource allocation. 
            - As transaction data expands, it is essential to categorize customers into clusters with similar traits for effective market segmentation. 
                This analysis helps businesses understand customers' buying habits and assess their overall worth, resulting in Customer Lifetime Value (CLV).
    """, unsafe_allow_html=True)
    st.markdown("""
        The primary goal of this analysis was to understand customer buying behavior, segment customers based on their purchasing patterns, and predict future buying potential, which collectively aid in enhancing marketing strategies and optimizing resource allocation. The RFM model uses three key variables: F, R, and M to identify significant customers in vast datasets. 
        - F measures the number of transactions, R indicates the time since last purchase, and M represents total expenditure.
        - This Streamlit application analyzes customer behavior and predicts their lifetime value (CLV) using advanced RFM and BG/GG models. By understanding customer segments and their purchasing patterns, businesses can optimize their marketing and sales strategies to maximize customer retention and profitability.
    """, unsafe_allow_html=True)
    st.markdown("""This application enable to
            - Upload your customer data in Excel format.
            - Explore descriptive statistics, top categories by sales, and geographic distribution of customers.
            - Analyze sales trends and purchase patterns for individual categories.
            - Visualize the data through interactive charts and maps.
        """)

    # RFM Analysis
    st.header("RFM Analysis")
    st.info("**Customer segmentation** involves using various customer attributes to tailor marketing strategies, identify trends, and create advertising campaigns. "
            ""
            "**The RFM model** is a commonly used model for segmenting customers, identifying important customers and adjusting marketing strategies.")
    st.markdown("""
        - Calculate RFM (Recency, Frequency, Monetary) scores for each customer.
        - Segment customers into distinct groups such as "Loyal Customers", "At-Risk", etc.
        - Analyze the distribution of customers across different segments and their purchasing behavior.
        - Visualize the relationship between RFM scores and customer value.
    """)

    # CLV Prediction
    st.header("CLV Prediction")
    st.write("In application you will be able to")
    st.markdown(""" 
        - Predict the CLV for each customer using Beta-Geometric/Gamma-Gamma (BG/GG) models.
        - Specify the prediction horizon (in months) for CLV calculations.
        - Analyze the factors influencing CLV, such as RFM characteristics and purchase history.
        - Visualize the distribution of predicted CLV across different customer segments.
    """)

    # New Customer Segmentation
    st.header("New Customer Segmentation")
    st.markdown("""
        - Segment a new customer based on their RFM scores.
        - Input the customer's recency, frequency, and monetary values.
        - The application will predict their segment based on predefined rules and historical data.
    """)

    st.write("#### *Comparative Analysis Over Time Periods*")
    st.markdown("""
        When comparing the 6-month, 12-month, 18-month, and 24-month predictions:
        - **Increase in CLV:** Longer prediction periods generally show an increase in CLV for most segments, especially for 'Champions' and 'Loyal Customers'. This suggests a compounding benefit of maintaining strong relationships with these segments.
        - **Segment Shifts:** Some segments like 'At Risk' or 'Need Attention' may not show as significant an increase in CLV over time, which highlights the risk of customer attrition and the need for immediate engagement strategies.
        - **Emerging Patterns:** Newer segments such as 'New Customers' and 'Potential Loyalists' show more variation between different forecasting periods. This variability is crucial for understanding how early interactions with the brand influence long-term value.
        """)
    # Streamlit Application Design
    st.header("Streamlit Application Design")
    st.markdown("""
            - The application is designed with a user-friendly interface and interactive visualizations.
            - Users can easily explore the data, perform analysis, and visualize the results.
            - Tooltips provide additional information about the data and visualizations.
            - The application is responsive and adapts to different screen sizes.
        """)
    # Benefits
    st.header("Benefits")
    st.write("With this application you can")
    st.markdown("""
            - Upload your customer data in Excel format.
            - Explore descriptive statistics, top categories by sales, and geographic distribution of customers.
            - Analyze sales trends and purchase patterns for individual categories.
            - Visualize the data through interactive charts and maps.
        """)
    st.write("and")
    st.markdown(""" 
        - Identify valuable customer segments for targeted marketing campaigns.
        - Prioritize customer acquisition and retention efforts based on predicted CLV.
        - Make data-driven decisions based on customer insights.
        - Improve customer understanding and optimize marketing strategies.
    """)
    st.write("")
    st.subheader('Project Demo')
    st.markdown("""
                To see the full demonstration of the project, including the interactive Streamlit application and results, please see the following video:
                """)
    st.markdown("""
            [Watch the video on Google Drive](https://drive.google.com/file/d/1acOJykQdrSbKpdodZiw7I_o1DxcloU1b/view?usp=share_link)
            """)
    st.write("")

    st.markdown("Click [here](https://customercltv.streamlit.app/) to try the app.")
