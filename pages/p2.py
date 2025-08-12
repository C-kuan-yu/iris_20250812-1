import streamlit as st
import numpy as np
import pandas as pd
import joblib 

st.title('IRIS品種預測')
#載入模型
svm = joblib.load('models/svm.joblib')
LR = joblib.load('models/LR.joblib')
RF = joblib.load('models/RF.joblib')
knn = joblib.load('models/knn.joblib')

#左側側邊欄位:選擇模型
s1 = st.sidebar.selectbox('選擇模型',('SVM',
                                  'KNeighborsClassifier',
                                  'LogisticRegression',
                                  'RandomForestClassifier'))

if s1 == 'SVM':
    model = svm
elif s1 == 'KNeighborsClassifier':
    model = knn
elif s1 == 'LogisticRegression':
    model = LR
elif s1 == 'RandomForestClassifier':
    model = RF

#放入鳶尾花品種照片
st.image('iris.png')


#接收使用者輸入:4個特徵
df = pd.read_csv('iris.csv')
se1 = st.slider("花萼長度(cm)", float(df['sepal.length'].min()),
                float(df['sepal.length'].max()),
                float(df['sepal.length'].mean()))
se2 = st.slider("花萼寬度(cm)", float(df['sepal.width'].min()),
                float(df['sepal.width'].max()),
                float(df['sepal.width'].mean()))
se3 = st.slider("花瓣長度(cm)", float(df['petal.length'].min()),
                float(df['petal.length'].max()),
                float(df['petal.length'].mean()))
se4 = st.slider("花瓣寬度(cm)", float(df['petal.width'].min()),
                float(df['petal.width'].max()),
                float(df['petal.width'].mean()))

labels = ['Setosa', 'Versicolor', 'Virginica']
if st.button("進行預測"):
    X = np.array([[se1, se2, se3, se4]])
    y = model.predict(X)
    st.write(f'### 預測結果:{y}')
    st.write(f'### 品種名稱:{labels[y[0]]}')
