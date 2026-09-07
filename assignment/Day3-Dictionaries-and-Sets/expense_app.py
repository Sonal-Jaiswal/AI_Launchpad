import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Monthly Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.title{
    text-align:center;
    color:white;
    padding:20px;
    border-radius:15px;
    background:linear-gradient(90deg,#11998e,#38ef7d);
    margin-bottom:20px;
}

.metric-card{
    background:linear-gradient(135deg,#4A00E0,#8E2DE2);
    color:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    background:#11998e;
    color:white;
    border-radius:10px;
}

.stButton>button:hover{
    transform:scale(1.05);
    transition:0.4s;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------

st.markdown("""
<div class='title'>
<h1>💰 Monthly Expense Tracker</h1>
<h4>Budget & Expense Analysis Dashboard</h4>
</div>
""", unsafe_allow_html=True)

# ---------------- Session State ----------------

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if "budget" not in st.session_state:
    st.session_state.budget = 10000.0

# ---------------- Sidebar ----------------

st.sidebar.header("⚙ Budget Settings")

budget = st.sidebar.number_input(
    "Monthly Budget",
    min_value=1.0,
    value=float(st.session_state.budget)
)

st.session_state.budget = budget

st.sidebar.header("➕ Add Expense")

description = st.sidebar.text_input("Expense Description")

category = st.sidebar.selectbox(
    "Expense Category",
    ["Food", "Travel", "Shopping", "Medical",
     "Entertainment", "Education", "Other"]
)

amount = st.sidebar.number_input(
    "Expense Amount",
    min_value=1.0,
    value=100.0
)

# ---------------- Add Expense ----------------

if st.sidebar.button("Add Expense"):

    st.session_state.expenses.append({
        "Description": description,
        "Category": category,
        "Amount": amount
    })

    st.success("✅ Expense Added Successfully")

# ---------------- Dashboard ----------------

if st.session_state.expenses:

    df = pd.DataFrame(st.session_state.expenses)

    total_expenses = df["Amount"].sum()

    remaining_budget = budget - total_expenses

    used_percentage = (total_expenses / budget) * 100

    # Budget Status

    if used_percentage > 100:
        status = "Budget Exceeded 🚨"
    elif used_percentage >= 90:
        status = "Critical ⚠️"
    elif used_percentage >= 75:
        status = "Warning 🟡"
    else:
        status = "Within Budget ✅"

    # ---------------- Metrics ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"<div class='metric-card'>💵 Budget<br>₹{budget:,.2f}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='metric-card'>💸 Expenses<br>₹{total_expenses:,.2f}</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"<div class='metric-card'>💰 Remaining<br>₹{remaining_budget:,.2f}</div>",
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"<div class='metric-card'>📊 Used<br>{used_percentage:.2f}%</div>",
            unsafe_allow_html=True
        )

    # ---------------- Report Table ----------------

    st.subheader("📋 Expense Report")

    st.dataframe(df, use_container_width=True)

    st.success(f"Budget Status: {status}")

    # ---------------- List Comprehensions ----------------

    above_2000 = [
        e["Description"]
        for e in st.session_state.expenses
        if e["Amount"] > 2000
    ]

    travel_expenses = [
        e["Description"]
        for e in st.session_state.expenses
        if e["Category"].lower() == "travel"
    ]

    reduced_expenses = [
        round(e["Amount"] * 0.90, 2)
        for e in st.session_state.expenses
    ]

    # ---------------- Analysis ----------------

    st.subheader("📌 Expense Analysis")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("💰 Expenses Above ₹2000")
        st.write(above_2000)

    with c2:
        st.warning("✈️ Travel Expenses")
        st.write(travel_expenses)

    with c3:
        st.success("📉 After 10% Reduction")
        st.write(reduced_expenses)

    # ---------------- Category Totals ----------------

    category_totals = {}

    for expense in st.session_state.expenses:

        cat = expense["Category"]
        amt = expense["Amount"]

        if cat in category_totals:
            category_totals[cat] += amt
        else:
            category_totals[cat] = amt

    st.subheader("📊 Category Wise Totals")

    category_df = pd.DataFrame(
        list(category_totals.items()),
        columns=["Category", "Total"]
    )

    st.dataframe(category_df, use_container_width=True)

    # ---------------- Charts --d