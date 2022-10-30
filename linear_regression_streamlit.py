import streamlit as st
import sklearn
import joblib,os
import numpy as np
import pandas as pd
import plotly.express as px

# def read_data(data_file):
#     csvreader = csv.reader(open(data_file))
#     header = []
#     header = next(csvreader)

def get_data(file_name):
    salary_data = pd.read_csv(file_name)
    salary_data = salary_data.set_index('YearsExperience', drop=True)
    return salary_data


# Loading Models
def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def main():
    # very simple Linear Regression App
    st.title('Salary Determination Application')

    activity = ['Salary Determination', 'Data', 'About']
    choice = st.sidebar.selectbox("Menu", activity)

    # Salary Determination CHOICE
    if choice == 'Salary Determination':
        
        st.subheader('Salary Determination')

        experience = st.slider("Years of Experience", 0,20)

        # st.write(type(experience))

        if st.button("Determination"):
            regressor = load_prediction_model("./models/linear_regression_salary.pkl")
            experience_reshaped = np.array(experience).reshape(-1, 1)

            # st.write(type(experience_reshaped))
            # st.write(experience_reshaped)
            # st.write(experience_reshaped.shape)

            predicted_salary = regressor.predict(experience_reshaped)

            st.info("Salary related to {} years of experience: {}".format(experience, (predicted_salary[0][0].round(2))))


    # Data CHOICE
    if choice == 'Data':
        st.subheader('Data flow')
        st.write("Here's our first attempt at using data to create a table:")

        
        salary_data = get_data("./data/salary.csv")

        print(salary_data)

        fig = px.line(salary_data)
        st.write(fig)



    # About CHOICE
    if choice == 'About':

        st.subheader('About')
        st.markdown("""
        ## Very Simple Linear Regression App

        ##### By
        + **[Huy Vu](https://github.com/vuhuy172dh)**
        + [huyvu123dh@gmail.com](mailto:huyvu123dh@gmail.com)
        """)
    


if __name__ == '__main__':
    main()
