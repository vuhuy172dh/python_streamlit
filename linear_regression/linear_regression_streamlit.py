import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Page layout
st.set_page_config(page_title="Linear Regression App", layout='wide')

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
        

def build_model(df, split_size):
    X = df.iloc[:, :-1] # Using all column except for the last column as X
    Y = df.iloc[:,-1] # Selecting the last column as Y

    # Data spliting 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=(100-split_size)/100)

    # data information
    st.write('Training set')
    st.info(X_train.shape)
    st.write('Testing set')
    st.info(X_test.shape)

    st.write("X varible")
    st.info(list(X.columns))
    st.write("Y variable")
    st.info(Y.name)

    # training modal
    linear_regression = LinearRegression()
    linear_regression.fit(X_train, Y_train)
    pred = linear_regression.predict(X_test)

    mse = mean_squared_error(Y_test, pred)
    st.write(mse)

def main():

    with st.sidebar.header('1. Set Parameters'):
        split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)

    file_csv = []
    st.subheader('Upload your csv')

    fileUpLoad = FileUpload()
    data = fileUpLoad.run()

    build_model(data, split_size=split_size)



      
if __name__ == '__main__':
    main()