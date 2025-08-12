import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('IRIS相關資訊')
df = pd.read_csv('iris.csv')
st.write(df.head()) #展示前5筆資料
st.write('### iris樣本散布圖')


mapping = {'Setosa':0, 'Versicolor':1, 'Virginica':2} 
colors=['red','green','blue']

# 依Tab顯示不同欄位的分布情形
tab1, tab2 = st.tabs(['[依 花 萼 的 長 寬]','[依 花 瓣 的 長 寬]'])
fig1, ax1 = plt.subplots()
with tab1:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax1.scatter(subset['sepal.length'],subset['sepal.width'],label=i, c=colors[s])
    ax1.set_xlabel('sepal.length')
    ax1.set_ylabel('sepal.width')
    ax1.legend()
    st.pyplot(fig1)

fig2, ax2 = plt.subplots()
with tab2:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax2.scatter(subset['petal.length'],subset['petal.width'],label=i, c=colors[s])
    ax2.set_xlabel('petal.length')
    ax2.set_ylabel('petal.width')
    ax2.legend()
    st.pyplot(fig2)
