import streamlit as st
import requests, json

st.title("🛒 SuperKart Sales Forecaster")
st.markdown("Enter product and store details to predict quarterly sales revenue.")

col1, col2 = st.columns(2)
with col1:
    product_type = st.selectbox("Product Type", [
        "Dairy","Frozen Foods","Snack Foods","Canned","Baking Goods",
        "Meat","Household","Fruits and Vegetables","Soft Drinks","Hard Drinks",
        "Health and Hygiene","Starchy Foods","Breads","Seafood","Breakfast","Others"])
    product_weight = st.number_input("Product Weight (kg)", 4.0, 22.0, 12.7)
    product_mrp = st.number_input("Product MRP ($)", 10.0, 300.0, 150.0)
    sugar_content = st.selectbox("Sugar Content", ["No Sugar","Low Sugar","Regular"])
    allocated_area = st.slider("Allocated Area Ratio", 0.01, 0.15, 0.06)

with col2:
    store_type = st.selectbox("Store Type", [
        "Departmental Store","Supermarket Type1","Supermarket Type2","Food Mart"])
    store_size = st.selectbox("Store Size", ["Small","Medium","High"])
    city_tier = st.selectbox("City Tier", ["Tier 1","Tier 2","Tier 3"])
    est_year = st.slider("Store Establishment Year", 1987, 2009, 1999)

if st.button("Predict Sales"):
    payload = {
        "Product_Type": product_type, "Product_Weight": product_weight,
        "Product_MRP": product_mrp, "Product_Sugar_Content": sugar_content,
        "Product_Allocated_Area": allocated_area, "Store_Type": store_type,
        "Store_Size": store_size, "Store_Location_City_Type": city_tier,
        "Store_Establishment_Year": est_year
    }
    resp = requests.post("https://rburjanr-superkart-backend.hf.space/predict", json=payload)
    pred = resp.json()["predicted_sales"]
    st.success(f"💰 Predicted Sales Revenue: **${pred:,.2f}**")