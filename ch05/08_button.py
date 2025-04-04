# -*- coding:utf-8 -*-
import streamlit as st
# 매출액 계산 로직 구현
def calculate_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue

def main():
    st.title("Sales Revenue Calculator")

    price = st.slider("단가:", 1000, 10000, value=5000)
    st.write("가격:", price, "원")
    total_sales = st.slider("전체 판매 갯수", 1, 1000, value=500)
    st.write("판매 갯수:", total_sales, "개")

    if st.button("매출액 계산"):  # 버튼 누르면 반환값 True -> 계산
        revenue = calculate_sales_revenue(price, total_sales)
        st.write("전체 매출액은", revenue, "원(KRW)")


if __name__ == "__main__":
    main()