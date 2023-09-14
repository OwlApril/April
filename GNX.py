import pandas as pd
import streamlit as st

st.title('기넥신 성장 금액 계산기📈')


num1 = st.number_input("☘️ 1주일 진료일수", value=4)
num2 = st.number_input("☘️ 하루 기넥신 처방 환자", value=0)
num3 = st.radio("☘️ 처방 용량(mg)", options=[40, 80, 240],horizontal=True)
pday = st.slider("☘️ 의료인 평균 처방 일수", 0, 120, 1)


num3_dic = {40: 127, 80: 185, 240: 550}
result = num1*num2*num3_dic[num3]*pday*4


if st.button('확인👍'):
    st.subheader(f"월 성장 예상금액은 **:green[{result:,}]** 원 입니다.")
else:
    st.write('')
