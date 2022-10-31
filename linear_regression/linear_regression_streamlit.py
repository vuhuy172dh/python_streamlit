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
        return df
        

def main():
    file_csv = []
    st.subheader('Upload your csv')

    fileUpLoad = FileUpload()
    file_csv = fileUpLoad.run()
    print(file_csv)

    


      
if __name__ == '__main__':
    main()