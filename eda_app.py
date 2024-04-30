import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px


#load data
@st.cache_data
def load_data(data):
    df =  pd.read_csv(data)
    return df

def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    df_clean = pd.read_csv("data/diabetes_data_upload_clean.csv")
    df = load_data("data/diabetes_data_upload.csv")
    freq_df = load_data("data/freqdist_of_age_data.csv")
    # st.dataframe(df)

    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])

    if submenu == "Descriptive":
        
        st.dataframe(df)

        with st.expander("Data Types Summary"):
            st.dataframe(df.dtypes) 
            pass      

        with st.expander("Descriptive Summary"):
            st.dataframe(df_clean.describe())

        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())

        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())

    else:
        st.subheader("Plots")

        # Layouts
        
        with st.expander("Dist Plot of Gender"):
            col1,col2 = st.columns([2,1])
            with col1:

                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type','Counts']
                # st.dataframe(gen_df)
                p01 = px.pie(gen_df,names='Gender Type',values='Counts')
                st.plotly_chart(p01,use_container_width=True)
            

            with col2:
                st.dataframe(df['Gender'].value_counts())


        with st.expander("Dist Plot of Class"):
            col1,col2 = st.columns([2,1])
            with col1:

                # with st.expander("Dist Plot of Class"):
                fig = plt.figure()
                sns.countplot(data=df, x='class')
                st.pyplot(fig)
            

            with col2:
                st.dataframe(df['class'].value_counts())
            

        with st.expander("Frequency Dist Plot of Age"):
            # fig,ax = plt.subplots()
            # ax.bar(freq_df['Age'],freq_df['count'])
            # plt.ylabel('Counts')
            # plt.title('Frequency Count of Age')
            # plt.xticks(rotation=45)
            # st.pyplot(fig)

            p = px.bar(freq_df,x='Age',y='count')
            st.plotly_chart(p)

            p2 = px.line(freq_df,x='Age',y='count')
            st.plotly_chart(p2)

        with st.expander("Outlier Detection Plot"):
            # outlier_df = 
            fig = plt.figure()
            sns.boxplot(df['Age'])
            st.pyplot(fig)

            p3 = px.box(df,x='Age',color='Gender')
            st.plotly_chart(p3)

        with st.expander("Correlation Plot"):
            corr_matrix = df_clean.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix,annot=True)
            st.pyplot(fig)

            p3 = px.imshow(corr_matrix)
            st.plotly_chart(p3)
