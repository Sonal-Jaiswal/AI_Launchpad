import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Inventory Management System",
    page_icon="📦",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.title{
    text-align:center;
    padding:20px;
    border-radius:15px;
    color:white;
    background:linear-gradient(90deg,#1e3c72,#2a5298);
    margin-bottom:20px;
}

.metric-card{
    background:linear-gradient(135deg,#11998e,#38ef7d);
    color:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

.stButton > button{
    width:100%;
    border-radius:10px;
    background:#2a5298;
    color:white;
}

.stButton > button:hover{
    transform:scale(1.03);
    transition:0.4s;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------

st.markdown("""
<div class='title'>
<h1>📦 Inventory Management System</h1>
<h4>Product Stock Analysis Dashboard</h4>
</div>
""", unsafe_allow_html=True)

# ---------------- Session State ----------------

if "products" not in st.session_state:
    st.session_state.products = []

# ---------------- Sidebar ----------------

st.sidebar.header("➕ Add Product")

name = st.sidebar.text_input("Product Name")

price = st.sidebar.number_input(
    "Product Price",
    min_value=0.01,
    value=1.0
)

current_stock = st.sidebar.number_input(
    "Current Stock",
    min_value=0,
    step=1
)

minimum_stock = st.sidebar.number_input(
    "Minimum Stock",
    min_value=1,
    step=1
)

# ---------------- Add Product ----------------

if st.sidebar.button("Add Product"):

    if current_stock == 0:
        status = "Out of Stock"
    elif current_stock < minimum_stock:
        status = "Low Stock"
    elif current_stock == minimum_stock:
        status = "Reorder Recommended"
    else:
        status = "Sufficient Stock"

    if current_stock > minimum_stock:
        reorder_qty = 0
    else:
        reorder_qty = minimum_stock * 2 - current_stock

    inventory_value = price * current_stock

    st.session_state.products.append({
        "Product": name,
        "Price": price,
        "Current Stock": current_stock,
        "Min Stock": minimum_stock,
        "Status": status,
        "Reorder Qty": reorder_qty,
        "Inventory Value": inventory_value
    })

    st.success("✅ Product Added Successfully")

# ---------------- Report ----------------

if st.session_state.products:

    df = pd.DataFrame(st.session_state.products)

    st.subheader("📋 Inventory Report")

    st.dataframe(df, use_container_width=True)

    # Metrics

    total_products = len(df)
    total_inventory_value = df["Inventory Value"].sum()

    low_stock_count = len(
        df[df["Status"].isin(
            ["Low Stock", "Reorder Recommended", "Out of Stock"]
        )]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='metric-card'>📦 Products<br>{total_products}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='metric-card'>💰 Inventory Value<br>₹{total_inventory_value:,.2f}</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"<div class='metric-card'>⚠️ Reorder Needed<br>{low_stock_count}</div>",
            unsafe_allow_html=True
        )

    # List Comprehensions

    out_of_stock = [
        p["Product"]
        for p in st.session_state.products
        if p["Status"] == "Out of Stock"
    ]

    reorder_products = [
        p["Product"]
        for p in st.session_state.products
        if p["Status"] in
        ["Low Stock", "Reorder Recommended", "Out of Stock"]
    ]

    high_value_products = [
        p["Product"]
        for p in st.session_state.products
        if p["Inventory Value"] > 10000
    ]

    # Display Lists

    st.subheader("📌 Inventory Analysis")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.error("🚫 Out Of Stock Products")
        st.write(out_of_stock)

    with c2:
        st.warning("📦 Products Requiring Reorder")
        st.write(reorder_products)

    with c3:
        st.success("💰 Inventory Value > ₹10,000")
        st.write(high_value_products)

    # Charts

    st.subheader("📊 Stock Status Distribution")

    status_counts = df["Status"].value_counts()

    st.bar_chart(status_counts)

    st.subheader("💰 Inventory Value by Product")

    value_chart = df.set_index("Product")["Inventory Value"]

    st.bar_chart(value_chart)

    st.subheader("📦 Current Stock Levels")

    stock_chart = df.set_index("Product")["Current Stock"]

    st.line_chart(stock_chart)

else:
    st.info("Add products from the sidebar to generate the inventory report.")