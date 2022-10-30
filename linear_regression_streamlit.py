import streamlit as st
import sklearn
import joblib,os
import numpy as np

def main():
    # very simple Linear Regression App
    st.title('Salary Determination Application')

    activity = ['Salary Determination', 'About']
    choice = st.sidebar.selectbox("Menu", activity)

    # Salary Determination CHOICE
    if choice == 'Salary Determination':
        
        st.subheader('Salary Determination')

        experience = st.slider("Years of Experience", 0,20)

        st.write(type(experience))


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
