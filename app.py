# Core pkgs
import streamlit as st
import streamlit.components.v1 as stc

from eda_app import run_eda_app
from ml_app import run_ml_app


PAGE_CONFIG = {
    "initial_sidebar_state" : 'expanded'
}
st.set_page_config(**PAGE_CONFIG)

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""


def main():
    # st.title("Main App")
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("""
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")

    elif choice == "EDA":
        run_eda_app()

    elif choice == "ML":
        run_ml_app()

    # elif choice == "About":
    #     st.subheader("About")


if __name__ == '__main__':
    main()