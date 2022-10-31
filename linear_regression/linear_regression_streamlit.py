import pandas as pd
import streamlit as st

class FileUpload(object):
    def __init__(self):
        self.fileTypes = ['csv']
    
    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file = st.empty()
        if not file:
            show_file.info("Please upload a file of type: .csv")
            return

        df = pd.read_csv(file)
        st.dataframe(df)
        file.close()
        

def main():
    activity = [ 'Linear regression', 'Upload your csv', 'About']
    choice = st.sidebar.selectbox('Menu', activity)

    if choice == 'Linear regression':
        st.subheader('Linear Regression')
    
    if choice == 'Upload your csv':
        st.subheader('Upload your csv')

        fileUpLoad = FileUpload()
        fileUpLoad.run()


      
if __name__ == '__main__':
    main()