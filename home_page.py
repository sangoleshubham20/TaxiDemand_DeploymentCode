import streamlit as st
from PIL import Image


def show_home_page():
    """
    This function displays the Home Page.
    """
    st.write("### **Forcasting pickup densities for Yellow Taxi services in Manhattan**")
    st.text("")
    st.text("")
    img = Image.open("car_home.png")
    st.image(img)
    st.text("")

    st.markdown("**OVERVIEW**")
    st.write("""Those who have travelled to New York City know that the streets are teeming with yellow cabs. These
                ubiquitous vehicles are constantly patrolling looking for those who need a ride. Back during the Great
                Depression, which lasted from 1929 through most of the 1930s, working men were laid off by the thousands
                every day. With basically nowhere else to turn, thousands of those men became NYC taxi cab drivers.
                Almost overnight the number of cabs on the road exploded, and suddenly supply was far greater than the
                demand. The cab industry was destined for destruction, so the government stepped in to regulate it. In
                1937, New York City created the taxi cab medallion system.
             """)
    st.markdown("""The NYC cab medallion is a piece of metal that is attached to the hood of the car signifying that the
                vehicle is legally able to operate as a cab in New York. **As of February 2023, there are about 13,500
                medallion cabs in New York City**.
             """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**PURPOSE OF THIS PROJECT & IT'S RELEVANCE**")
    st.markdown("""While working on this project, I had mainly two objectives in my mind. **Firstly, I wanted my project
                to potentially be profitable in the real world taxi market**. If a taxi driver could precisely know in
                advance which boroughs or areas are going to have the highest demand, he could optimize his workday by
                driving only around those areas. This will help him manage his time appropriately and earn more money
                while also saving some time for his family/personal life. Either way, it will improve his life.
             """)
    st.markdown("""**Secondly, I wanted to solve an existing problem which exists in the taxi industry**. There has been
                   an active debate regarding "how services like Uber and Lyft are literally crushing the traditional
                   street hail taxi market in New York City". Taxi drivers are afraid that they cannot compete with the
                   kind of on demand fare adjusted service Uber provides based on cutting-edge technology. To compete
                   with such big players in the industry, I think this machine learning app could help these traditional
                   taxi drivers to improve their service and profitability.
                """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**BUSINESS PROBLEM**")
    st.markdown("""Modeling the trip records is a non trivial task because analyzing this time series data that too on
                such a scale is very challenging. **We need to build a machine learning application for taxi drivers 
                that is not intimidating & is easy to use**. This will help them reduce their workload to some extent.
                A taxi driver can easily install this application on his smartphone and run it in a couple of seconds to
                look at the most demanding areas and plan his journey for the next 3 days.
              """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**BUSINESS CONSTRAINTS**")
    st.markdown("""* **Interpretability of the model** is not that consequential because a taxi driver doesn't need to
                   know why the model has predicted a certain value.
                """)
    st.markdown("""* There are **no low-latency requirements** but at the same time, we also don't want our
                   latency to be in several minutes.
                """)
    st.markdown("""* **Errors can be costly** because the driver may loose potential pickups in other areas if provided
                with incorrect predictions.
                """)
    st.markdown("""* Since it's a regression problem, **we don't need probabilities**.
                """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**MAPPING THE PROBLEM TO A MACHINE LEARNING PROBLEM**")
    st.markdown("* **Time-series forecasting**.")
    st.markdown("""* Given the location co-ordinates(latitude and longitude), date & time of a trip in the query region
                   and surrounding regions, **we need to predict the number of pickups**.
                """)
    st.markdown("""* Since the number of pickups are real values, it is a **Regression problem.**
                """)
    st.markdown("""* **Performance metric(s) :** Mean Absolute Percentage Error (MAPE), Mean Squared Error(MSE)
                """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**DATA ACQUISITION**")
    st.markdown("""* **2019 Yellow Taxis data:** I downloaded this dataset from NYC Taxi & Limousine Commission, a free
                   public data source of New York City. You can download the **[dataset here]
                   (https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)**. The dataset includes 17 fields. You
                   can have a look at the **[data dictionary here]
                   (https://drive.google.com/file/d/1fDe5SjM46DqFyG4veNqGOpIilvPsuaar/view?usp=drive_link)**.
                    """)
    st.markdown("""* **Weather precipitation history:** I wanted to include precipitation data to train the models, as
                   it is sensible to think that rain would play a vital role in predicting the pickups. I downloaded it
                   from the **[NOAA](https://www.ncdc.noaa.gov/cdo-web/datasets#LCD)**
                   (National Centers for Environmental Information).
                """)
    st.markdown("""* **Polygon shape file:** In order to visualize the results I needed geometric data. This ".shp" file
                   represents the boundary zones for taxi pickups as delimited by the New York City Taxi and Limousine
                   Commission (TLC). You can download the file from **[here]
                   (https://archive.nyu.edu/handle/2451/36743)**.
                """)
    img_boundary = Image.open("boundary.jpg")
    st.image(img_boundary)
    st.markdown("""* **Weather Precipitation Forecast:** I used Selenium Webdriver to scrape weather precipitation
                   forecast in real time from **[wunderground](https://www.wunderground.com/)** to get the predictions.
                    """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.markdown("**INTERNAL STRUCTURE**")
    st.markdown("""I have divided this project into 3 parts: **Data Processing, Modeling and Front-End**. The first part
                includes exploratory data analysis on the taxis and weather datasets to find anomalies, patterns,
                insights, test hypothesis, etc. The second part outputs a trained model packed in a pickle file. The
                third part generates a web application which interactively shows predictions to the final user.
             """)
    img_structure = Image.open("structure.png")
    st.image(img_structure)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**MACHINE LEARNING TECHNIQUES**")
    st.markdown("**Baseline Models:**")
    st.markdown("* Moving averages")
    st.markdown("* Weighted moving averages")
    st.markdown("* Exponential weighted moving averages")
    st.markdown("**Linear & Non-linear Regression Models:**")
    st.markdown("* Linear Regression")
    st.markdown("* K-Nearest Neighbours")
    st.markdown("**Ensemble learning:**")
    st.markdown("* Random Forest")
    st.markdown("* XGBoost")
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**FRONT-END**")
    st.write("""The front-end is a web application that a taxi driver can run every day to plan his journey. It performs
                the following three actions:
             """)
    st.markdown("""* **Generate Model Inputs:** It generates datetime features based on the current date and shapes the
                   data appropriately including LocationID of Manhattan’s zones. Also, it scrapes the precipitation
                   weather forecast in real time from **[wunderground](https://www.wunderground.com/)** and attach the
                   data to the previous one.
                """)
    st.markdown("""* **Generate Predictions:** It unpacks the pickle model and makes predictions using the features
                generated above.
                """)
    st.markdown("""* **Visualize Results:** It takes the predictions and shapes the data so that it can be shown
                   interactively in a choropleth map and a multiple line chart. Charts are made with Bokeh and Altair,
                   while the web application is made with Streamlit.
                """)
    st.markdown("""<hr style="height:0.5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    st.markdown("**DEPENDENCIES & MODULES**")
    st.write("You need the following dependencies and modules installed in your environment:")
    st.markdown("""**`altair`, `base58`, `bokeh`, `datetime`, `descartes`, `geopandas`, `matplotlib`, `numpy`, `pandas`,
                `pickle`, `PIL`, `scikit-learn`, `scipy`, `seaborn`, `selenium`, `shapely` `streamlit`**""")
