import streamlit as st
from PIL import Image

import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def project_7_page():
    st.markdown("""
        <style>
        .title {
            font-size: 32px;
            color: #ff6600;
            font-weight: bold;
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 5px;
            background-color: #f0f9ff;
            font-family: 'Arial', sans-serif
            color: black;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: black;
            margin-bottom: 10px;
            padding: 5px;
            border-radius: 5px;
            background-color: #f0f9ff;
            font-family: 'Arial', sans-serif
            color: black;
        }
        .content {
            font-size: 18px;
            color: black;
            padding: 15px;
            border-radius: 5px;
            background-color: #f0f9ff;
        }
        .section-title {
            font-size: 24px;
            color: black;
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 5px;
            background-color: #f0f9ff;
            font-family: 'Arial', sans-serif
            color: black;
        }
        .section-content {
            font-size: 18px;
            color: black;
            padding: 15px;
            border-radius: 5px;
            background-color: #f0f9ff;
            font-family: 'Arial', sans-serif
        }
        .subsection-title {
            font-size: 14px;
            color: #ff6600;
            margin-bottom: 5px;
            padding: 5px;
            font-family: 'Arial', sans-serif
        }
        .subsection-content {
            font-size: 14px;
            color: black;
            padding: 10px;
            margin-bottom: 10px;
            font-family: 'Arial', sans-serif
        }
        .subsection-content ul {
            font-size: 14px;
            font-family: 'Arial', sans-serif
        }
        .link {
            font-size: 18px;
            color: #ff6600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
        }
        .link img {
            margin-left: 8px;
        }
        .image-link img {
            width: 100%;
            height: auto;
        }
        }
        </style>
    """, unsafe_allow_html=True)

    # Title of the page
    st.markdown("<div class='title'>Energy Demand Prediction</div>", unsafe_allow_html=True)

    # Display Project Image
    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/energyTurkey.jpeg")
    st.image(image, caption='', use_column_width=True)

    # Section 1: Project Overview
    st.markdown("<div class='subheader'>1. Project Overview</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            Energy is a cornerstone of modern economies and plays a crucial role in national development. Turkey, with its rapidly growing population and dynamic economy, needs to manage its energy resources efficiently. Analyzing and forecasting energy consumption and production not only supports sustainable development but also enhances economic stability and environmental sustainability.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Project Objectives</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            This project aims to provide a comprehensive view of Turkey’s energy sector by:
            <ul>
                <li><strong>Analyzing Energy Production:</strong> Understanding regional contributions and identifying potential inefficiencies or areas for improvement.</li>
                <li><strong>Forecasting Energy Needs:</strong> Predicting future energy requirements to anticipate demand fluctuations and address potential challenges.</li>
                <li><strong>Detecting Anomalies:</strong> Identifying anomalies in energy consumption and production patterns to uncover underlying causes or optimization opportunities.</li>
                <li><strong>Providing Actionable Insights:</strong> Offering actionable insights through interactive maps and data visualizations to aid policymakers, businesses, and researchers in making informed decisions regarding energy management and strategy.</li>
            </ul>
            By leveraging advanced data analysis techniques and forecasting models, this application aims to promote a more informed and efficient approach to managing Turkey’s energy resources and contribute to positive changes in the sector.
        </div>
    """, unsafe_allow_html=True)

    # Add a horizontal line
    #st.markdown("---")

    # Section 2: Data Preparation
    st.markdown("<div class='subheader'>2. Data Preparation</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Data Cleaning and Transformation</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Date and Consumption Data:</strong> The initial step involves cleaning the data by focusing on the date and consumption columns.
            - <strong>Monthly Aggregations:</strong> Data is aggregated on a monthly basis to handle missing values and ensure a consistent time series.
        </div>
    """, unsafe_allow_html=True)

    # Add a horizontal line
    #st.markdown("---")

    # Section 3: Model Selection
    st.markdown("<div class='subheader'>3. Model Selection</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Time Series Models</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>SARIMA Model:</strong> This model accounts for seasonal components and trends in time series forecasting.
            - <strong>Prophet:</strong> Developed by Facebook, Prophet incorporates seasonality and holiday effects to enhance prediction accuracy.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Machine Learning Models</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Random Forest:</strong> An ensemble learning method for regression that improves prediction through multiple decision trees.
            - <strong>Gradient Boosting:</strong> A technique that builds models sequentially, focusing on errors of previous models to enhance performance.
            - <strong>Linear Regression:</strong> A fundamental approach to model the relationship between dependent and independent variables.
        </div>
    """, unsafe_allow_html=True)

    # Add a horizontal line
    #st.markdown("---")

    # Section 4: Model Training and Evaluation
    st.markdown("<div class='subheader'>4. Model Training and Evaluation</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Model Training</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>SARIMA and Prophet:</strong> These models are trained on historical data to forecast future energy consumption and production.
            - <strong>Machine Learning Models:</strong> Features are scaled, and data is split into training and testing sets to train and evaluate models. Performance metrics include RMSE, MAE, MAPE, and MSE.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Evaluation Metrics</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Performance Assessment:</strong> Each model’s effectiveness is measured and compared based on various metrics to determine the best fit for forecasting energy needs.
        </div>
    """, unsafe_allow_html=True)

    # Add a horizontal line
    #st.markdown("---")

    # Section 5: Results and Visualization
    st.markdown("<div class='subheader'>5. Results and Visualization</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Model Performance</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Performance Metrics:</strong> A detailed comparison of performance metrics for each model.
            - <strong>Forecasting Results:</strong> Visualization of actual versus predicted values for better understanding of model accuracy.
        </div>
    """, unsafe_allow_html=True)

    st.write(
        "<i>The Prophet model has been the most successful in predicting Turkey's overall energy consumption. Therefore, the information and outputs related to the Prophet model are provided below.</i>",
        unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Seasonal Decomposition</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Energy Consumption Patterns:</strong> Decomposition of time series data to analyze seasonal patterns and trends in energy consumption.
        </div>
    """, unsafe_allow_html=True)

    # Display analysis and forecasting
    st.markdown("<div class='section-title'>🔮 Prophet Forecast</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-content">
            <p>The Prophet model forecast provides predictions for future electricity consumption based on past data:</p>
            <ul>
                <li><strong>The blue line</strong> represents actual observed values, showing a clear dip during the COVID-19 pandemic in 2020.</li>
                <li><strong>The red line</strong> represents forecasted values, capturing both seasonal patterns and overall trends, including the recovery post-2020.</li>
                <li><strong>The uncertainty intervals</strong> (shaded areas) around the forecast suggest the model's confidence. Larger uncertainty during the pandemic reflects the unpredictable nature of demand during that time.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.image("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/timeseries1/newplot.png")

    st.markdown("<div class='section-title'>🔍 Time Series Decomposition Analysis</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-content">
            <p>The time series decomposition breaks down the electricity consumption data into its key components:</p>
            <ul>
                <li><strong>Observed:</strong> Shows noticeable fluctuations with a slight upward trend and a significant dip around 2020, reflecting the impact of the COVID-19 pandemic.</li>
                <li><strong>Trend:</strong> Highlights a general increase in consumption over time with a pronounced dip in 2020, consistent with the global economic slowdown and pandemic impacts.</li>
                <li><strong>Seasonal:</strong> Shows consistent patterns of higher consumption during certain times of the year, reflecting regular cyclical demands such as heating or cooling needs.</li>
                <li><strong>Residual:</strong> Reflects irregularities not explained by trend or seasonal components, particularly volatile during 2020 due to pandemic effects.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.image("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/timeseries1/decomposition1.png")

    st.markdown("<div class='section-title'>📊 Model Performance Metrics</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-content">
            <div class="metric">
                <span style="color: blue;">Mean Absolute Error (MAE):</span> <span>688,534.92 — Average prediction error of around 688,535 units, reasonable given the pandemic disruptions.</span>
            </div>
            <div class="metric">
                <span style="color: blue;">Mean Squared Error (MSE):</span> <span>767,293,866,815.38 — High MSE due to larger errors from the 2020 drop and recovery.</span>
            </div>
            <div class="metric">
                <span style="color: blue;">Root Mean Squared Error (RMSE):</span> <span>875,953.12 — Typical error of around 875,953 units, reflecting difficulties during the pandemic.</span>
            </div>
            <div class="metric">
                <span style="color: blue;">Mean Absolute Percentage Error (MAPE):</span> <span>3.45% — Model's predictions are within 3.45% of actual values, quite accurate considering pandemic challenges.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Add a horizontal line
    #st.markdown("---")

    # Section 6: Interactive Map
    st.markdown("<div class='subheader'>6. Interactive Map</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Map Features</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Energy Consumption and Production Forecasts:</strong> The map provides visualizations of energy consumption and production forecasts across Turkey.
            - <strong>User Interaction:</strong> Users can explore different aspects of energy data through interactive features.
        </div>
    """, unsafe_allow_html=True)
    st.image("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/timeseries1/map_energy.png")

    # Conclusion and Future Work
    st.markdown("<div class='subheader'>Conclusion and Future Work</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-content">
            The model effectively captures the trend and seasonality of electricity consumption, even during the volatile COVID-19 period. The trend analysis reflects the sharp dip in 2020, and the Prophet model adjusts accordingly, predicting a recovery. The accuracy metrics indicate that despite challenges, the model provides reliable forecasts, making it a valuable tool for predicting future electricity demands in similar unpredictable scenarios.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Key Takeaways</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            - <strong>Insights:</strong> The project offers valuable insights into Turkey’s energy consumption and production patterns.
            - <strong>Recommendations:</strong> Suggestions for future improvements and potential areas of further research.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='subheader'>7. Contributions</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
            Here’s the contributions of this project to the business world:
            <div class='subsection-title'>1. Energy Management and Planning</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Capacity Planning:</strong> Forecasting energy consumption helps optimize energy supply to meet demand, aiding in capacity planning for energy production facilities.</li>
                    <li><strong>Infrastructure Investment:</strong> Anticipating changes in energy demand supports effective infrastructure investment planning.</li>
                </ul>
            </div>
            <div class='subsection-title'>2. Cost and Efficiency</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Cost Savings:</strong> Energy consumption forecasts and analysis help energy suppliers determine the most cost-effective procurement strategies, reducing costs.</li>
                    <li><strong>Increased Efficiency:</strong> Identifying anomalies and inefficiencies in energy consumption improves energy efficiency and reduces operational costs.</li>
                </ul>
            </div>
            <div class='subsection-title'>3. Risk Management</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Supply Chain Management:</strong> Forecasting demand fluctuations helps identify risks in the energy supply chain and develop risk management strategies.</li>
                    <li><strong>Crisis Management:</strong> Proactive measures can be taken to address sudden demand spikes or production issues, enabling quicker and more effective responses.</li>
                </ul>
            </div>
            <div class='subsection-title'>4. Sustainability and Environmental Impact</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Sustainable Energy Use:</strong> The project provides recommendations for making energy production and consumption more sustainable, reducing environmental impact.</li>
                    <li><strong>Carbon Footprint Reduction:</strong> Optimizing energy use through better management and forecasting can reduce the carbon footprint.</li>
                </ul>
            </div>
            <div class='subsection-title'>5. Policy and Strategy Development</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Policy Formulation:</strong> Analysis of energy consumption and production helps governments and local authorities create energy policies and strategies based on scientific data.</li>
                    <li><strong>Investment Strategies:</strong> Investors and companies can make more informed investment decisions by understanding future energy demands and production trends.</li>
                </ul>
            </div>
            <div class='subsection-title'>6. Competitive Advantage</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Market Analysis:</strong> Energy forecasts and production analysis help companies understand market trends and gain a competitive edge.</li>
                    <li><strong>Innovative Solutions:</strong> The project provides insights into innovative solutions and technologies in the energy sector, helping companies stay ahead of industry changes.</li>
                </ul>
            </div>
            <div class='subsection-title'>7. Customer Satisfaction</div>
            <div class='subsection-content'>
                <ul>
                    <li><strong>Service Quality:</strong> Energy companies can use forecasts and analysis to offer more reliable and uninterrupted energy services, improving customer satisfaction.</li>
                </ul>
            </div>
            <br>
            This project provides valuable information to all stakeholders in the energy sector, enabling more efficient, sustainable, and cost-effective energy management and decision-making.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Next Steps</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-content'>
        <ul>
            <li> <strong>Model Enhancements:</strong> Future work will focus on refining models and incorporating additional data sources for improved accuracy.
            <li> <strong>Broader Applications:</strong> Exploring applications of the forecasting models in other regions or sectors.
       <ul>
        </div>
    """, unsafe_allow_html=True)
    # Add a horizontal line
    st.markdown("---")
    st.markdown("<div class='section-title'>Project Demo</div>", unsafe_allow_html=True)
    st.markdown("<h5>Click here to see the link and download the application 👇</h5>", unsafe_allow_html=True)
    st.markdown("To see the full demonstration of the project, please click the following link or picture:")
    st.markdown("""
              [Watch the video on Google Drive](https://drive.google.com/file/d/1-xq6GA9BGTVsazeNpdKhhzVsXsjit-kQ/view?usp=sharing)
              """)
    st.write("")
    # Example clickable image
    image_path = "/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/timeseries1/app_photo.png"  # Yerel dosya yolunu buraya yazın
    base64_image = image_to_base64(image_path)

    # Tıklanabilir resim ekleme
    st.markdown(f"""
            <div class="section-content">
                <a href="https://drive.google.com/file/d/1-xq6GA9BGTVsazeNpdKhhzVsXsjit-kQ/view?usp=sharing" target="_blank" class="image-link">
                    <img src="data:image/png;base64,{base64_image}" alt="Clickable Image">
                </a>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("Click here to try the **[App](https://energy-prediction-tr.streamlit.app/)**", unsafe_allow_html=True)
    st.write("")

    st.write("Check the details on GitHub.")
    st.markdown("""
        <a href="https://github.com/Sicakyuz/EnergyDemandPrediction" class="link" target="_blank">
            **Click here** 
            <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" alt="GitHub" width="30" height="30">
        </a>
    """, unsafe_allow_html=True)
