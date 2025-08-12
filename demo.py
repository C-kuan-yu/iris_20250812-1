import numpy as np
import pandas as pd
import streamlit as st

#st.title("元件練習")
#st.write("12345699")
#st.write("# 最大的標題") # title的意思 #+空白
#st.write("## 次大的標題") # ##+空白
#st.info("ABC")
#a=100
#st.write(a*100) #網頁版變數的使用

# 顯示表格
arr1 = np.array([10,20,30,40,55])
st.write(arr1)
df = pd.DataFrame([[1,2,3,4],[11,22,33,44]])
st.write(df)
st.table(df)

# 核取方塊
st.write("## 核取方塊")
r1 = st.checkbox('外帶')
if r1:
    st.info("外帶")
else:
    st.info("內用")
checks = st.columns(4) #4個橫向排序的空欄位
txt = ''
with checks[0]: #為欄位命名
    c1 = st.checkbox("A餐")
    if c1:
        txt += 'A餐 '
with checks[1]:
    c2 = st.checkbox("B餐")
    if c2:
        txt += 'B餐 '
with checks[2]:
    c3 = st.checkbox("C餐")
    if c3:
        txt += 'C餐 '
with checks[3]:
    c4 = st.checkbox("D餐")
    if c4:
        txt += 'D餐 '
st.info(txt) #顯示選擇了哪些項目

st.write('## 選項按鈕')
r2 = st.radio("選擇飲料:",('咖啡','奶茶','果汁','啤酒','水','不需要'))
st.info(r2)
r3 = st.radio("選擇飲料:",('咖啡','奶茶','果汁','啤酒','水','不需要'), key='123')
st.info(r3)

#運算表單 選取方塊
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("請輸入任一整數")
with col2:
    num2 = st.number_input("請輸入任一整數", key='num2')
cal = st.radio("請選擇符號:",('＋','－','＊','／'), key='cal')
if cal == '＋':
    result = num1 + num2
elif cal == '－':
    result = num1 - num2
elif cal == '＊':
    result = num1 * num2
elif cal == '／':
    if num2 != 0:
        result = num1/num2
    else:
        result = '除數不能為0'
st.info(f"計算結果: {result}")

# 滑桿
st.write('## 滑桿')
slider = st.slider("請選擇數量:", 1.0,20.0, step=0.5) #需要數就要都寫小數
st.info(slider)
st.write('## 滑桿')
slider = st.slider("請選擇數量:", 1.0,20.0, value=10.0) # value滑桿起始位置
st.info(slider)

# 下拉選單
st.write('## 下拉選單')
select = st.selectbox("城市:", ('台北','新北','桃園','台中','台南','其他'),index=2) 
st.info(select)

# 按鈕
st.write('## 按鈕')
btn1 = st.button("確定")
if btn1:
    st.info("按下確定")
btn2 = st.button("否")
if btn2:
    st.info("按下否")

# 上傳檔案
st.write('## 上傳檔案')
file = st.file_uploader("請選擇csv檔")
if file is not None:
    df = pd.read_csv(file)
    st.write(df.head())

# 側邊欄
st.sidebar.write('## 側邊欄')
select2 = st.sidebar.selectbox("城市:", ('台北','新北','桃園','台中','台南','其他'),
                               index=0, key='se2') 
st.sidebar.info(select2)