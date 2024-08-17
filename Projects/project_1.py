import streamlit as st
from PIL import Image

def project_1_page():

    image = Image.open("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/img_1.png")
    st.image(image, caption='', use_column_width=True)
    st.markdown(" ")

    st.header('Cluster Analysis for Breast Cancer Dataset')

    st.write(
        'In this project, we aimed to apply clustering algorithms to a breast cancer dataset to identify patterns and potentially distinguish between benign and malignant cases. The dataset contains various features extracted from digitized images of breast mass, and the goal was to cluster the data points into meaningful groups and evaluate the performance of different clustering algorithms.')

    st.subheader('Data Preprocessing')
    st.write(
        'The dataset was first inspected for missing values, outliers, and unnecessary columns. Missing values were handled using the mean strategy. Outliers were addressed using the IQR method. Categorical columns were label-encoded.')

    st.subheader('Clustering Algorithms')
    st.write(
        'Four clustering algorithms were utilized: KMeans, Agglomerative Clustering, Gaussian Mixture, and Mean Shift. These algorithms were chosen for their effectiveness in clustering tasks and their ability to handle different types of data distributions.')

    st.subheader('Evaluation Metrics')
    st.write(
        'To evaluate the clustering results, several metrics were used, including silhouette score, Calinski-Harabasz index, and Davies-Bouldin index. These metrics help assess the quality of the clusters and compare the performance of different algorithms.')

    st.subheader('Results and Findings')
    st.write(
        'The clustering algorithms were applied to the preprocessed dataset, and cluster labels were assigned to each data point. Visualizations, such as scatter plots and bar plots, were created to illustrate the cluster distributions and their relationship with the diagnosis labels. Evaluation metrics were calculated to assess the clustering performance, with the Gaussian Mixture model showing the best performance based on the silhouette score and other metrics.')
    st.write("This algorithm was able to accurately detect approximately 99% of real cancer patients. The following graph compares the classes of real values (Diagnosis) and predicted values (Cluster). Based on the health data of 569 individuals, the actual numbers of cancer patients and healthy individuals, as well as the predicted numbers of cancer patients and healthy individuals, can be clearly seen.")
    st.image("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Images/diabet/breast_cancer_distribution.png")
    st.subheader('Conclusion')
    st.write(
        'The project demonstrated the application of clustering algorithms to a real-world dataset and their effectiveness in identifying patterns in breast cancer data. The findings suggest that clustering can be a useful tool for analyzing breast cancer data and potentially aiding in the diagnosis and treatment of the disease.')

    st.subheader('Benefits and Contributions')
    st.write(
        'The project provides insights into the application of clustering algorithms to healthcare datasets, particularly in the field of breast cancer research. The visualizations and analysis can help researchers and healthcare professionals better understand the data and potentially identify subgroups of patients with different characteristics.')

    st.subheader('Future Directions')
    st.write(
        'Future work could involve refining the clustering algorithms and exploring other machine learning techniques to further improve the clustering performance. Additionally, incorporating more features and data sources could enhance the analysis and provide more comprehensive insights into breast cancer data.')

    st.subheader('Presentation and Visuals')
    st.write(
        'The project presentation will include visualizations such as scatter plots, bar plots, and cluster visualizations to illustrate the clustering results effectively. Visuals will be used to highlight key findings and showcase the performance of different algorithms.')

    st.video("/Users/asmir/Desktop/MyPortfolio/Portfolio/Projects/Videos/unsuperwised.webm")

    st.markdown("<h5></i>Click here to see the link and download the application \U0001F447</i></h5>", unsafe_allow_html=True)

    # https://breastcancerpredictionapp.streamlit.app/
    st.markdown("**[App](https://breastcancerpredictionapp.streamlit.app/)**", unsafe_allow_html=True)

