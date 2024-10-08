import streamlit as st
import streamlit_option_menu
import streamlit.components.v1 as components
from PIL import Image


def publications_page():
    st.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex: 1; text-align: left;">
                <img src="https://img.icons8.com/ios-glyphs/30/000000/book.png"/>
            </div>
            <div style="flex: 4; text-align: left;">
                <h2>Publications</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        /* Expander bileşeninin iç ve dış kenarlıkları */
        [data-testid="stExpander"] {
            background-color: #f5fafd; /* İç arka plan rengi (açık mavi) */
            border: 0px solid #d0d0d0; /* Dış kenarlık rengi (ince gri) */
            border-radius: 10px; /* Köşeleri yuvarlama */
            padding: 0; /* İçerik ile kenarlık arasındaki mesafeyi kaldırma */
            box-shadow: none;
            margin: 0; /* Kenarlık dışındaki boşluğu kaldırma */
        }
        /* Expander başlığının rengi */
        [data-testid="stExpander"] > div:first-child {
            color: #e0f2f1; /* Başlığın rengi (koyu mavi) */
            margin: 0; /* Başlık ile içeriğin arasındaki boşluğu kaldırma */
            padding: 0; /* Başlık içindeki paddingi kaldırma */
        }
        /* Expander içindeki metnin rengi */
        [data-testid="stExpander"] div[data-testid="stMarkdownContainer"] {
            color: #000000; /* İçerik metninin rengi (siyah) */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.expander("Designing the home healthcare supply chain during a health crisis"):
        st.write("**Abstract**")
        st.write(
                "During the COVID-19 pandemic, sectoral contributors to home healthcare supply chain (HHCSC) corporations highlighted the role of home care services. Pharmacies are located where patients are allocated to them, and nurses are routed and scheduled according to their patients' needs. It is the first study to propose an integrated location-allocation-routing model, which includes all preliminaries necessary to make these decisions. We implement the LP-metric and epsilon-constraint methods to solve this model, and then we discuss the results of these methods. A comparison is also made regarding the objective function values and the time taken to solve the problem. The average, mean ideal distance (MID) (3.74;3.19), the rate of achievement of two objectives simultaneously (RAS) (1.71;3.56), and computational time (CPU time) (1.92;24.92) for two ɛ-constraint and LP-Metric methods is calculated. The superior technique is finally selected by utilizing the TOPSIS. To solve the study’s mathematical model, the LP-metric method is worth implementing. Based on these results, the suggested model for HHCSC companies, and employees’ performance, is efficient during the COVID-19 pandemic.")
        st.write("**Keywords**")
        st.write("Home healthcare supply chain, Location-allocation, LP-metric, Epsilon-constraint, TOPSIS method")
        st.markdown("[Read more](https://www.sciencedirect.com/science/article/pii/S2307187723000998)")

    with st.expander("An Integrated Q-Rung Orthopair Fuzzy (Q-ROF) for the Selection of Supply-Chain Management"):

        st.write("**Abstract**")
        st.write(
                "The integration of sustainable indicators into supply-chain management (SCM), including cost, innovation capability, quality, service capability, long-term cooperation, environmental management system, pollution reduction, green image, social responsibility, and employment practices, has become essential for conducting strategic analyses of the entire supply-chain process competitive advantage. This study proposes a fuzzy integration multi-criteria decision-making (MCDM) method to solve SCM issues. To navigate this complexity, a multi-criterion decision-making (MCDM) framework is employed, integrating MCDM methods with fuzzy logic to effectively address subjective environmental criteria. This innovative approach not only enhances supply-chain management (SCM) but also emphasizes the necessity for ongoing innovation in tackling contemporary supply-chain challenges. It serves as a cornerstone for sustainable supplier selection practices and optimizing SCM processes. In this study, a hybrid fuzzy MCDM method is proposed for supplier selection. The method addresses supplier selection by utilizing evaluations from expert decision-makers based on predetermined criteria. This comprehensive approach ensures that all relevant factors are considered, promoting sustainable and efficient supply-chain management.")
        st.write("**Keywords**")
        st.write(
                "multi-criteria decision-making (MCDM); fuzzy set; q-rung orthopair fuzzy (Q-ROF);supply-chain management (SCM")
        st.markdown("[Read more](https://doi.org/10.3390/su16124901)")

    with st.expander("Supply chain risk management: A content analysis-based review of existing and emerging topics"):
        st.write("**Abstract**")
        st.write(
            "This paper presents a systematic review of the literature on Supply Chain Risk (SCR) research, focusing on content-based analysis. The study comprehensively examines the general factors associated with key themes and trends in supply chain risk management, encompassing the identification and assessment of risks, risk mitigation strategies, and the influence of emerging technologies on Supply Chain Risk Management (SCRM). The review provides an overview of current and emerging topics in SCRM, while also introducing categorization frameworks to address research gaps and provide a roadmap for future studies, thereby generating valuable insights in this field. The review highlights the significance of effective SCRM in ensuring business continuity and resilience, emphasizing the need for organizations to adopt a proactive approach to risk management. The paper concludes by identifying areas for future research, including the development of novel risk management frameworks and the integration of emerging technologies into supply chain risk management practices. Additionally, a comprehensive evaluation of each classification is presented, highlighting overlooked aspects and unexplored domains, and offering recommendations for potential next steps in SCRM research.")
        st.write("**Keywords**")
        st.write(
                "Existing and emerging topicsRisk publications,Risk factors,Supply chain risk management,Risk assessment,Bibliometric analysis")
        st.markdown("[Read more](https://www.sciencedirect.com/science/article/pii/S2949863523000304)")

    with st.expander(
                "Analyzing Healthcare and Wellness Products’ Quality Embedded in Online Customer Reviews: Assessment with a Hybrid Fuzzy LMAW and Fermatean Fuzzy WASPAS Method"):
        st.write("**Abstract**")
        st.write(
                "With the high impetus in global digitization, online shopping (OS) is anticipated to increase further in the near future. Contrary to this anticipation, however, recent studies have emphasized a certain amount of drop in a considerable number of online purchasing transactions in 2022. One of the reasons might be customer dissatisfaction. To analyze online customer reviews, manual sentiment analysis was conducted to detect which quality criteria cause the dissatisfaction of online shoppers. The quality parameters are categorized into product, delivery service, and aftersales service quality (SQ). These main quality criteria are then divided into sub-factors. Eight health category products, including personal care products, wellness products, and household cleaners, were ranked to the importance of the sub-quality parameters using the multi-criteria decision-making (MCDM) method. In this study, a new hybrid MCDM method was also proposed, which combines the triangular fuzzy logarithm methodology of additive weights (F-LMAW) and the Fermatean fuzzy weighted aggregated sum product assessment method (FF-WASPAS). The study reveals that the most important criteria were products’ performance, as well as their side effects, pay-back, and change possibility, while the products’ reasonable price was the least important criterion. Aftersales service was more significant than delivery service. Furthermore, moisturizing creams and medical pillows were the most popular products bought in OS compared with hair conditioners and washing liquids. The study’s multifold contributions and managerial implications were elaborately discussed.")
        st.write("**Keywords**")
        st.write(
                "customer satisfaction; online shopping; word of mouth; e-commerce; service quality; sustainable competitive advantage; MCDM; F-LMAW; FF-WASPAS")
        st.markdown("[Read more](https://www.mdpi.com/2071-1050/15/4/3428)")

    with st.expander(
                "Is E-Trust a Driver of Sustainability? An Assessment of Turkish E-Commerce Sector with an Extended Intuitionistic Fuzzy ORESTE Approach"):
        st.write("**Abstract**")
        st.write(
                "Due mainly to COVID-19 and the demanding work schedules of many individuals, online purchasing sites have become indispensable. However, the dynamic online environment and everchanging customer demands make sustainable competitiveness challenging for e-commerce platforms. Humans primarily influence the preference for online purchase platforms. This study aimed to discover Türkiye’s top popular online shopping sites by adopting an extended intuitionistic fuzzy ORESTE (Organisation, Rangement Et Synthèse De Données Relationnelles) approach. Our study targeted this by surveying female users of four online shopping platforms using IF-ORESTE. The criteria were determined according to customer preferences. These were as follows: easy accessibility to the platform, providing regular discounts and campaigns, advanced filtering settings, the contractual merchants’ reliability, quick delivery, being more affordable than competing platforms, positive feedback in user comments, having a large brand volume, having an installment option, and having partnered cargo companies. The least important factor was the large volume of brands on the online websites. Quick delivery of orders and positive feedback in reviews were equally important. Similarly, the decision-makers considered regular discounts and promotions and the comprehensive filtering settings as equally critical. However, these criteria were less significant than quick delivery and positive customer feedback. This work’s novelty lies in implementing the IF to the ORESTE in the Turkish e-commerce industry. The implications and future directions are discussed.")
        st.write("**Keywords**")
        st.write(
                "online shopping; ORESTE; multi-criteria decision making (MCDM); intuitionistic fuzzy set; e-commerce website")
        st.markdown("[Read more](https://www.mdpi.com/2071-1050/15/13/10693)")

    with st.expander(
                "Exploring resistance factors on the usage of hospital information systems from the perspective of the Markus's Model and the Technology Acceptance Model"):
        st.write("**Abstract**")
        st.write(
            "Although information systems provide many benefits to the organization, many organizations are experiencing difficulties with the process of change. Resistance to change is one of the most considerable challenges in this phase. This study aimed to investigate the causes of resistance by healthcare personnel to IT in Adana Numune Hastanesi, which is a state-run hospital located in Adana, Turkey. The Technology Acceptance Model (TAM) was expanded by adding factors such as affective commitment, gender, and age. Logistic regression analysis was carried out on the research model through 291 collected survey data using SPSS (version 21). The overall percentage accuracy prediction was 55.3% for parameters of the initial model and 80.8% for the stepwise model after the third step. According to the results, while the factors “perceived usefulness of IT,” “perceived ease of use of IT,” and “affective commitment” were found to have an influence on the resistance of use of IT, demographic factors such as age, gender, position, and tenure were not related. Managers should create an environment for increasing staff commitment by including them in decision-making and process changing. Thus, not only could the manager use the organizations’ resources productively, but also future change projects could be carried out effectively, roughly, and timely. Therefore, through its committed personnel, the hospital could sustainably compete with its competitors in the market and make more profit.")
        st.write("**Keywords**")
        st.write(
                "healthcare information systems; organizational affective commitment; resistance to innovation; change management; Technology Acceptance Model; TAM; Markus’s Model")
        st.markdown("[Read more](https://www.ceeol.com/search/article-detail?id=884832)")

    with st.expander(
                "A review of the COVID-19 pandemic's effects and challenges on worldwide waste management for sustainable development"):
        st.write("**Abstract**")
        st.write(
                "Through an extensive literature review, this study determines the COVID-19 pandemic's impacts and challenges on worldwide waste management for sustainable development. The coronavirus 2019 (COVID-19) pandemic has adversely and harshly affected almost every element of global social, economic, and environmental systems over the past few years. The widespread use of disposables and personal protective equipment (PPE) for infested and healthy people and frontier employees caused unprecedented miscellaneous garbage. Increasing waste volumes caused a problem for standard waste disposal facilities, which harmed the global waste management sector and resulted in a vital global scenario. Since waste management in developing countries is still in its infancy, the pandemic has broken many regions of the globe. The complete assessment gives a synopsis of COVID-19's impacts and difficulties on waste management. This study reviews the COVID-19 pandemic's effects and challenges on worldwide waste management for sustainable development to fill this gap. This analysis refers to the quantitative research method used to analyze bibliographic content. It provides a general overview of a research topic that may be further broken down into publications, authors, and journals. With a few notable exceptions, the results obtained align with accepted wisdom. In this study, we used the VOSviewer software. This study showed that most countries, essential to managing the increased waste, have seen an increase due to the COVID-19 pandemic. Nonetheless, a complete bibliometric examination of the issue still needs to be completed.")
        st.write("**Keywords**")
        st.write("")
        st.markdown("[Read more](https://link.springer.com/article/10.1007/s13762-024-05610-y)")

    with st.expander("How does the global innovation index score affect income? A policy for innovativeness"):
        st.write("**Abstract**")
        st.write(
            "Innovation has been a well-known fact for competition. Countries need to pursue a number of policies and take steps to be considered innovative. The aim of this study is to investigate the contribution of factors constituting the Global Innovation Index (GII), which serves as an indicator of countries’ innovativeness, to the economic level thereof and to draw a road map for the developing countries. Regression analysis was employed to evaluate the effects of the sub-factors that make up the GII score on the countries' GDP per capita. As a result, three factors were found to have a significant effect: Research and development (R&D), the countries' political environments and their general infrastructure have been found to have a significant effect on the economy. This study not only assists developing countries in determining their innovation policies, but also in identifying their deficiencies in order to improve their innovation levels. Thus, focusing on the factors that contribute the most to the country's economy, it will be possible to contribute to the economic level of the country more quickly and effectively. Since R&D studies are mostly done in universities, universities in particular should provide more resources to this unit. This research is significant because it highlights the need for private universities to develop R&D strategies in order to boost their competitiveness, provide laboratories and infrastructure with the necessary machinery and equipment, and retain outstanding researchers.")
        st.write("**Keywords**")
        st.write(
            "comparative innovativeness factors, competitive strategic management, Global Innovation Index, Gross Domestic Product, economic growth")
        st.markdown("[Read more](7https://dergipark.org.tr/en/pub/jrb/article/1022938)")

    with st.expander(
                "Comparison of relationship between global innovation index achievements and university achievements in terms of Countries"):
        st.write("**Abstract**")
        st.write(
            "In this study, analyses were conducted to determine the relationship between the countries’ achievements in the Global Innovation Index and the international achievements of the universities in the relevant countries. For university achievements, the data from HEEACT and ARWU rankings that measure the achievements of the universities worldwide were used. In the study, first, using the Global Innovation Index data of the countries and their respective data in HEEACT and ARWU rankings, Chi-square tests were performed and as a result, a significant relationship was detected. To determine the direction and degree of this relationship, Correlation tests were performed and it was concluded that there was a strong linear correlation between the innovation environment in the countries and the achievements of their universities. Finally, considering the continents and economic-political groups (G7, G20, BRICS) the countries were in, the data was classified using k-Means Cluster Analysis. It was found that GII, HEEACT, and ARWU achievements varied depending on the continent and economic-political groups the countries are in.")
        st.write("**Keywords**")
        st.write(
                "Global innovation Index, University Achievement Ranking, Development of Countries, Innovation Environment")
        st.markdown(
                "[Read more](https://www.researchgate.net/profile/Cigdem-Sicakyuez/publication/360684454_Comparison_of_relationship_between_global_innovation_index_achievements_and_university_achievements_in_terms_of_Countries/links/6285143ba93a5471227a280b/Comparison-of-relationship-between-global-innovation-index-achievements-and-university-achievements-in-terms-of-Countries.pdf)")

    with st.expander(
                "An integrated multiple-criteria decision-making and data envelopment analysis framework for efficiency assessment in sustainable healthcare systems"):
        st.write("**Abstract**")
        st.write(
            "Efficiency is critical in allocating sustainable healthcare resources to ensure that hospitals can effectively care for patients while maintaining high-quality care delivery. Hence, it is necessary to monitor efficiency carefully. This study aims to assess hospital unit effectiveness through a novel comprehensive approach integrating Multiple-Criteria Decision Making (MCDM) with Data Envelopment Analysis (DEA). The proposed MCDM-DEA framework involves allocating varying weights to distinct data categories. It harnesses the capabilities of the q-rung orthopair fuzzy (q-ROF) methodology to address the inherent uncertainties in healthcare performance assessment. The experimental results provide a comprehensively structured ranking system for specific hospital departments. This ranking system allows decision-makers to identify the strengths and weaknesses of each department, enabling them to make informed decisions regarding resource allocation and improvement strategies. Furthermore, the integration of MCDM-DEA provides a robust and objective assessment tool for monitoring and evaluating the performance of hospital departments over time. These rankings offer invaluable insights to decision-makers, equipping them with the strategic information needed to enhance the overall performance of hospital units.")
        st.write("**Keywords**")
        st.write(
                "Multiple-criteria decision-making,Data envelopment analysis,TOPSISQ-rung orthopair fuzzy, Sustainable healthcare,Efficiency assessment")
        st.markdown("[Read more](https://www.sciencedirect.com/science/article/pii/S2772442524000297)")

    with st.expander("Supply chain risk management: A content analysis-based review of existing and emerging topics"):
        st.write("**Abstract**")
        st.write(
            "This paper presents a systematic review of the literature on Supply Chain Risk (SCR) research, focusing on content-based analysis. The study comprehensively examines the general factors associated with key themes and trends in supply chain risk management, encompassing the identification and assessment of risks, risk mitigation strategies, and the influence of emerging technologies on Supply Chain Risk Management (SCRM). The review provides an overview of current and emerging topics in SCRM, while also introducing categorization frameworks to address research gaps and provide a roadmap for future studies, thereby generating valuable insights in this field. The review highlights the significance of effective SCRM in ensuring business continuity and resilience, emphasizing the need for organizations to adopt a proactive approach to risk management. The paper concludes by identifying areas for future research, including the development of novel risk management frameworks and the integration of emerging technologies into supply chain risk management practices. Additionally, a comprehensive evaluation of each classification is presented, highlighting overlooked aspects and unexplored domains, and offering recommendations for potential next steps in SCRM research.")
        st.write("**Keywords**")
        st.write(
                "Existing and emerging topics Risk publications,Risk factors,Supply chain risk management, Risk assessment, Bibliometric analysis")
        st.markdown(
                "[Read more](https://www.researchgate.net/profile/Cigdem-Sicakyuez/publication/373066812_Supply_Chain_Risk_Management_A_Content_Analysis-Based_Review_of_Existing_and_Emerging_Topics/links/64d73fe925837316ee070f99/Supply-Chain-Risk-Management-A-Content-Analysis-Based-Review-of-Existing-and-Emerging-Topics.pdf)")

    with st.expander("Bibliometric Analysis of Data Envelopment Analysis in Supply Chain Management"):
        st.write("**Abstract**")
        st.write(
            "A bibliometric analysis is presented in this paper to examine the use of Data Envelopment Analysis (DEA) in the domain of Supply Chain Management (SCM). The research trends on DEA in SCM from 2000 to 2023 are explored, using data obtained from the Web of Science database (WoS) and VOS viewer software for detailed mapping of the articles. The numerous articles that use DEA in SCM worldwide are analyzed and summarized in this bibliometric study, producing a complete assessment of DEA in the field from 352 academic papers published in high-ranking publications. The articles are classified according to the year of publication, countries of the author(s), working areas, journals, and content of studies. Based on the findings of this research, tremendous potential is shown for DEA as a suitable evaluation instrument for future studies on sustainability concerns in SCM.")
        st.write("**Keywords**")
        st.write("DEA; Supply Chain Management; Bibliometric Analysis; VOSviewer")
        st.markdown(
                "[Read more](https://www.researchgate.net/profile/Cigdem-Sicakyuez/publication/370275250_Bibliometric_Analysis_of_Data_Envelopment_Analysis_in_Supply_Chain_Management/links/644951804af78873523ba418/Bibliometric-Analysis-of-Data-Envelopment-Analysis-in-Supply-Chain-Management.pdf)")

    with st.expander(
            "Comparison of the accuracy of classification algorithms on three data-sets in data mining: Example of 20 classes"):
        st.write("**Abstract**")
        st.write(
                "Data mining, which has different uses such as text mining and web mining, is especially used for clustering and classification purposes. In this study, this method was used for both classification and text mining. The aim of the study was the assessment of the performances of the data mining algorithms on the three datasets. A total of 6631 master's and doctoral dissertations written in the field of industrial engineering were downloaded from the Higher Education Council database. With the help of summary, subject titles and keywords of these dissertations, it was tried to be guessed which sub-field of industrial engineering it belongs to using WEKA program. As a result, it was observed that the data set containing the keywords obtained by weighting the expert opinion was more successful than the other two data sets. And the three most successful classification algorithms were found to be kNN, SMO, and J48, respectively.")
        st.write("**Keywords**")
        st.write("Classification Algorithms, Data Mining, Multiple Classes, Dataset.")
        st.markdown("[Read more](https://www.ajol.info/index.php/ijest/article/view/199714)")

    with st.expander("Managing Change And A Facilitative Proposed Mobile Application In Education"):
        st.write("**Abstract**")
        st.write(
                "In all sectors, technology is changing so rapidly that as one is introduced, another is already inthe pipeline. Owing to the difficulty in keeping up to the rapid changes, some technologies areshelved without being used. Concerning Education, those who do not adopt to innovation andtechnology are teachers and students. In this study, the behaviours of 70 engineering studentsstudying in a university in Turkey were examined on the use of a mobile application in theirlessons. They were randomly categorized in two groups. Only one group was prepared on theuse of the application. The application was downloded by the two groups and their opinionsabout the application were taken via an online questionniare. Data was edited and anindependent t-test was conducted with SPSS Windows (ver. 25). The result showed that therewas a siginificant difference in the behavioural intentions between prepared and unpreparedgroups for change. The prepared students were more willing to use the application. Hence,students should be educated and sensitized on the importance of applications. Additionaly, anew system to incentivize students to easily participate in the change is proposed.")
        st.write("**Keywords**")
        st.write("Mobile Application, Resistance to Change, Readiness to Change, Independent T -Test.")
        st.markdown("[Read more](https://dergipark.org.tr/en/pub/ijma/issue/45813/568366)")
    with st.expander("The resistance factors to using health information technology in Turkey"):
        st.write("**Abstract**")
        st.write(
                "The primary goal of our study is to determine the types of resistance factors to IT are perceived by the healthcare staff. Furthermore, it was examined whether the resistance factors differ according to the individual characteristics for e.g. gender, profession, age, and IT experience of healthcare personnel or not. The questionnaire was distributed to the healthcare personnel of the hospitals in the different cities namely Ankara, Adana, Mardin and Diyarbakır in Turkey. Totally, 551 healthcare personnel were asked what kind of resistance factors to IT were played role when they were using health information systems. This study has revealed the most important resistance factors which have been perceived by the personnel and so required precautions can be tak hospital management can prioritize the resistances and develop necessary strategies so that they can lead and apply the information systems and future technology as well. Place and Du hospitals whose names are Adana Numune, A in April and collected in July 2016. After detailed literature review, 24 resistance fact set. A survey was designed to test the hypotheses and surveys were distributed to the hospitals in different cities. Collecte surveys were statistically analyzed by using Kruskal Wallis method after controlling data va gender does not play role in all examined the resistance factors apart from the factor “complexity of IT”. The position of healthcare was not related with the factors “need for IT training and the complexity of IT. The I the factors “perceived poor performance and complexity of IT. with the barriers of implementing information systems at the hospitals. Additionally, it will give ide manage the change during the implementation of IT. Paying attention to the most important factors can facilitate decision making in IT implementation. The managers will be informed about the affects of individual characteristics such gender, and position on resistance. So they can minimize the training expenses in IT usage by doing customized training plan.")
        st.write("**Keywords**")
        st.write("")
        st.markdown("[Read more](https://www.sciencedirect.com/science/article/pii/S2307187723000998)")
    with st.expander("A systematic literature review of logistics services outsourcing"):
        st.write("**Abstract**")
        st.write(
                "Logistics is critical in every company's supply chain (SC), and outsourcing helps businesses concentrate on their core competencies. Third-party logistics (3 PL) or logistics service providers (LSPs) assist businesses in cutting costs while improving performance, sustainability, and revenue. Logistics evaluation and LSPs choice are complicated and critical components of value delivery. This study aims to review logistics outsourcing literature to understand the trends, prospects, factors, and strategies used in logistics companies' outsourcing choices. This work examines the literature on LSPs selection published between 2010 and 2023. This paper uses VOSviewer (version 1.6.19) to visualize the relationships. Pricing, timely shipment, service quality, reliability, agility, technology, and consumer feedback are the most commonly utilized, whereas societal and environmental factors are seldom used. The study comprises journal publications, the year, selection criteria, and assessment methodologies. Numerous scholars have discovered and employed many critical selection criteria. Many investigators have also embraced multi-criteria decision-making (MCDM) methodologies, and their fuzzy form is widely used. In conclusion, recommendations for theorists and managers, limits, and future directions for research are offered. ")
        st.write("**Keywords**")
        st.write(
                "Supply chainLogistics services outsourcing,Logistics service providers selection,Third-party logistics selection criteria,Third-party logistics selection techniques")
        st.markdown("[Read more](https://www.sciencedirect.com/science/article/pii/S2405844024094052)")

    st.subheader("Conferences")

    with st.expander("Analysis of Decision_Making Capability of BI Software Used in Enterprises in Turkey"):
        st.write("**Abstract**")
        st.write(
                "Abstract Business intelligence is one of the best indicators of digitalization, enabling businesses to control their processes better and make them happen efficiently. In recent years, the Republic of Turkey's Ministry of Industry and Technology's efforts to digitalize SMEs show the importance of business intelligence for the country. This study aims to reveal whether the decision-making capability of Business Intelligence (BI) software differs according to the size of the enterprise. A survey was conducted to determine the decision-making capability of BI software on 50 enterprises participating in the Efficiency and Technology Fair held in June 2021. Business intelligence capability was measured using the Likert-type scale between 1 and 7. For this purpose, Kruskal-Wallis test was conducted considering different business sizes, such as micro, small, medium-sized, and large. The result exhibited that BI decision-making capability did not vary according to the size of the enterprise. Also another result is that approximately 68.9% of the companies use business intelligence, and 30% have a favorable view of business intelligence. 4% of enterprise representatives do not know who uses business intelligence in their company. In addition, it has been revealed that the most preferred business intelligence software is SAP Business Objects and ORACLE.")
        st.write(
                "Conference: International Conference on Science, Engineering Management and Information Technology, Ankara")
        st.write("**Keywords**")
        st.write("Keywords: Business Intelligence, Digitalization, SMEs, Firm awareness.")
        st.markdown("[Read more](https://www.sciencedirect.com/science/article/pii/S2307187723000998)")

    with st.expander("İnternet’in Yazılı Basına Etkisi ve Dijital Gazete Okumayı Etkileyen Faktörler"):
        st.write("**Abstract**")
        st.write(
                "Günümüzde İnternet birçok sektörde paradigmaların değişimine neden olmaya devam etmektedir. İnternet ve sosyal medya tarafından en çok etkilenen sektörlerden birisi de kağıt gazeteyi içeren yazılı basın sektörüdür. İnternet kullanımındaki artış, elektronik ortamda gazete okuma alışkanlığının artması gibi nedenlerden dolayı her geçen gün yazılı basın sektöründe gazeteler kapanmakta ya da küçülmektedir. Bu çalışmanın amacı, internet kullanımının yazılı basın üzerindeki etkisini araştırmaktır. Araştırmada gazete satın alımını etkileyen faktörler; cinsiyet, yaş, eğitim durumu, internette geçirilen süre, internette gazete okuma durumu, internette çıkan yerleşik ilanlar ve kullanılan cihazlar olarak belirlenmiştir. Araştırma verileri elektronik anket aracılığıyla toplanmış, bu anket1936 kişi tarafından görüntülenmiş ve 461 kişi tarafından doldurulmuştur. Elde edilen veriler, SPSS for Windows25 paket programında düzenlenmiş ve lojistik regresyon yöntemi ile analiz edilmiştir. Analiz sonucunda, ele alınan faktörlerden yaşın ve yerleşik ilanların basılı gazete satın alımında pozitif etkisi ve internette geçirilen sürenin negatif etkisi olduğu ortaya çıkmıştır. Araştırmada incelenen diğer faktörlerin ise etkisi olmadığı görülmüştür. Ayrıca, 49 yaş altındaki katılımcıların her beş kişiden bir tanesi basılı gazete okurken, 50 yaş ve üzeri kişilerinde ise bu oran her iki kişiden birisidir. Bu durum ise, ileriki yıllarda yazılı basın sektörünün, dijital gazeteler karşısında dayanıklılığını yitireceğini göstermektedir.")
        st.write("**Conference: Uluslararası Türkiye Vizyonu Kongresi (UTVİK-2019), Adana, Turkey**")
        st.write("İnternet, Yazılı Basın, Dijital Gazete, Lojistik Regresyon")
        st.markdown(
                "[Read more](https://www.researchgate.net/publication/332633570_Internet'in_Yazili_Basina_Etkisi_ve_Dijital_Gazete_Okumayi_Etkileyen_Faktorler)")

    with st.expander("Eğitim ve Katılımcılık: Üniversite Öğrencilerinin Mobil Uygulama Kullanımına Etkisi"):
        st.write("**Abstract**")
        st.write(
                "Günümüz bilgi çağında bilgisayardan İnternete, akıllı telefondan yapay zekaya birçok teknoloji ve sistem hem iş hayatında hem özel yaşamda hem de eğitimde önemli rol oynamaktadır. Bilişim sistemleri ve teknolojisini kullanmayı etkileyen birçok faktör bulunmaktadır. Kimi kullanıcılar bu kullanımı hemen benimserken yüksek oranda bir kesim ise direnç göstermektedir. Bu çalışmada, mühendislik öğrencilerinin bir dersde kullanılması düşünülen bir mobil uygulamayı benimsemelerinde onların fikirlerinin alınmasının ve onlara kısa bir eğitim verilmesinin, ilgili uygulamayı kullanmaları üzerindeki etkisiaraştırılmak istenmiştir. Bu amaçla Çukurova Üniversitesi Endüstri Mühendisliği Bölümü öğrencilerinden 70 kişi rassal olarak iki kategoriye ayrılmış ve bu iki gruptan biri sınıfın dışına alınmış ve diğer gruba ise uygulamanın amacı ve kullanımı hakkında bilgiler verilip, diğer gruba hiçbir bilgi verilmemiştir. Uygulama her iki grup öğrencileri tarafından indirilmiş ve her iki grup tarafından onların uygulamaya ilişkin görüşleri online anket ile alınmıştır. Anket verileri SPSS Windows for 25 paket programı ile derlenmiş ve bağımsız t testi ile analiz edilmiştir. Analiz sonucunda,“uygulama hakkında bilgi verilen grup” ile diğer grup arasında, söz konusu uygulamayı kullanım niyetleri bakımından fark olduğu ortaya çıkmıştır. Yani uygulamanın tanıtımına katılan öğrenciler, katılmayanlara göre uygulamayı daha çok kullanmak istediklerini belirtmişlerdir. Bu sonuç ise herhangi bir yazılımın yaygın ve etkin kullanımı için öğrencilerin bu değişime katılımcı olmaları ve bilgi verilerek hazırlanmaları gerektiğini göstermektedir. Böylelikle öğrenciler değişimin faydasını anlayabilmekte ve o değişime gönülden katılmaktadır.")
        st.write("**Keywords**")
        st.write("Bilişim Sistemleri Benimseme, Değişime Direnç, T Testi")
        st.markdown(
                "[Read more](https://www.researchgate.net/publication/332633412_Egitim_ve_Katilimcilik_Universite_Ogrencilerinin_Mobil_Uygulama_Kullanimina_Etkisi)")

    with st.expander("A Study of Adopter Categories among Healthcare Personnel in a Hospital in Turkey"):
        st.write("**Abstract**")
        st.write(
                "Diffusion of innovations is a theory developed by Rogers that examines to explain how, why, and at what rate new ideas and technology disperse. Rogers suggests that the innovation itself, communication channels, time, and a social system are the main elements of generating new idea, and humans are the key for spreading the innovation.Any idea, practice, process or technology that is perceived as new by people or organization can be considered as innovation. Adopters are individuals, but can also be organizations such as firms, hospitals or schools. Rogers offers five categories of adopters in order to systematize the usage of adopter classes in diffusion research. Adopter categories are defined as pioneers, early adopters, early majority, late majority, and laggards according to the degree of accepting a new idea.The purpose of this study is to classify healthcare personnel in hospitals in Turkey according to their acceptability of new technology (information systems) based on Roger's Diffusion of innovation theory. With this framework, hospital management can have the opportunity to predict the risks of innovation by evaluating their own personnel in an implementation of new technology or idea. Thus the management can manage the change easily.The survey has been applied on a total of 149 health personnel from the hospitals called “Adana Numune” in Adana and the results are compared with Roger's innovation categories. The individual innovation measurement model of Hurt et al. (2013) was used to evaluate the degree of innovativeness of health staff. First, the data were compiled and formulated for each category based on the categories of Rogers with the help of MS Excel (2007). Then the data were analyzed with SPSS 21 software program and descriptive statistics were generated.As a result, while Roger's innovation categories were constructed from five classes, four classes emerged in this study. There were no pioneers among the adopters of health personnel in the hospital. The class of traditionalists known as 'Laggards' was only 7% in this study. According to Roger, this value is 16%. Late Majority (34%) category defined by Roger is greater than the results of this study (21.5%). The percentage of the personnel in the Early Majority group is more than half (61.1%) of the respondents while it was mentioned as 34% according to Rogers. Only 16.8% respondents belong to the Early Adaptors category.In conclusion, the hospital has the most personnel from the category of Early Majority. This means that these employees adopt the innovation longer time later than pioneers and early adopters. Their social statuses are above the average, they are both cost sensitive and also risk averse. The management of the hospital has to support them by convincing the benefits of innovation since seldom they behave as opinion leaders in the system and they prefer to interact frequently with peers.")
        st.write("**Keywords**")
        st.write("Diffusion theory, innovation, adopter categories, healthcare")
        st.markdown("[Read more](International Conference on Advances and Innovations in Engineering (ICAIE))")


    st.markdown('</div>', unsafe_allow_html=True)
