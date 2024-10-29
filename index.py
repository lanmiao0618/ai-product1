"""
streamlit多页面程序的入口文件
"""
import streamlit as st

st.title("AI大模型应用产品网")
co1, co2 = st.columns(2)
# 语言大模型应用程序入口
with co1:
    st.image("https://tse2-mm.cn.bing.net/th/id/OIP-C.qmIh5R-d_DmDKOYgzN09agHaJQ?rs=1&pid=ImgDetMain",use_column_width=True)
    flag = st.button("赛迩绘言", use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")
# 文生图大模型应用程序入口
with co2:
    st.image("https://tse2-mm.cn.bing.net/th/id/OIP-C.qmIh5R-d_DmDKOYgzN09agHaJQ?rs=1&pid=ImgDetMain",use_column_width=True)
    flag = st.button("赛迩绘图", use_container_width=True)
    if flag:
        st.switch_page("pages/textToimage.py")
