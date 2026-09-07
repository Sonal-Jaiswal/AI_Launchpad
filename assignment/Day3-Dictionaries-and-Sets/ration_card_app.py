import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Government Ration Card Benefit Tracking System",
    page_icon="🏛️",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f8fb;
}

.title {
    text-align:center;
    color:white;
    padding:20px;
    border-radius:15px;
    background: linear-gradient(90deg,#0077b6,#00b4d8);
    animation: fadeIn 1.5s;
}

.card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.2);
    transition:0.3s;
}

.card:hover {
    transform:scale(1.03);
}

.metric-box {
    background:linear-gradient(135deg,#4CAF50,#2E7D32);
    color:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    font-size:18px;
    font-weight:bold;
}

@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------

st.markdown(
    """
    <div class='title'>
    <h1>🏛 Government Ration Card Benefit Tracking System</h1>
    <h4>Food Distribution Department Dashboard</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- Input Form ----------------

if "records" not in st.session_state:
    st.session_state.records = []

with st.form("ration_form"):

    st.subheader("Citizen Details")

    name = st.text_input("Citizen Name")

    card_type = st.selectbox(
        "Ration Card Type",
        ["APL", "BPL", "AAY"]
    )

    family_members = st.number_input(
        "Family Members Count",
        min_value=1,
        step=1
    )

    subsidy = st.number_input(
        "Monthly Subsidy Amount (₹)",
        min_value=1.0
    )

    submit = st.form_submit_button("Add Citizen")

if submit:

    benefit_category = {
        "AAY": "Highest Benefit",
        "BPL": "Medium Benefit",
        "APL": "Standard Benefit"
    }

    if family_members <= 3:
        family_category = "Small Family"
    elif family_members <= 6:
        family_category = "Medium Family"
    else:
        family_category = "Large Family"

    st.session_state.records.append({
        "Name": name,
        "Card Type": card_type,
        "Family Members": family_members,
        "Subsidy": subsidy,
        "Benefit Category": benefit_category[card_type],
        "Family Category": family_category
    })

    st.success("Citizen Added Successfully ✅")

# ---------------- Display Records ----------------

if st.session_state.records:

    df = pd.DataFrame(st.session_state.records)

    st.subheader("📋 Citizen Records")
    st.dataframe(df, use_container_width=True)

    total_citizens = len(df)
    total_subsidy = df["Subsidy"].sum()
    average_subsidy = df["Subsidy"].mean()

    st.subheader("📊 Overall Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='metric-box'>👥 Citizens<br>{total_citizens}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='metric-box'>💰 Total Subsidy<br>₹{total_subsidy:.2f}</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"<div class='metric-box'>📈 Average Subsidy<br>₹{average_subsidy:.2f}</div>",
            unsafe_allow_html=True
        )

    st.write("")

    # ---------------- List Comprehensions ----------------

    above_3000 = [
        x["Name"]
        for x in st.session_state.records
        if x["Subsidy"] > 3000
    ]

    bpl_holders = [
        x["Name"]
        for x in st.session_state.records
        if x["Card Type"] == "BPL"
    ]

    increased_subsidy = [
        round(x["Subsidy"] * 1.10, 2)
        for x in st.session_state.records
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💰 Subsidy Above ₹3000")
        st.write(above_3000)

        st.subheader("👨‍👩‍👧‍👦 BPL Card Holders")
        st.write(bpl_holders)

    with col2:
        st.subheader("📈 Subsidy After 10% Increase")
        st.write(increased_subsidy)

    # ---------------- Card Wise Statistics ----------------

    st.subheader("🏷 Ration Card Wise Statistics")

    apl_count = 0
    bpl_count = 0
    aay_count = 0

    for record in st.session_state.records:

        if record["Card Type"] == "APL":
            apl_count += 1

        elif record["Card Type"] == "BPL":
            bpl_count += 1

        elif record["Card Type"] == "AAY":
            aay_count += 1

    card_stats = pd.DataFrame({
        "Card Type": ["APL", "BPL", "AAY"],
        "Citizens": [apl_count, bpl_count, aay_count]
    })

    st.table(card_stats)

    # ---------------- Charts ----------------

    st.subheader("📊 Visual Analysis")

    chart_df = card_stats.set_index("Card Type")

    st.bar_chart(chart_df)

    st.subheader("💵 Subsidy Distribution")

    subsidy_chart = df.groupby(
        "Card Type"
    )["Subsidy"].sum()

    st.line_chart(subsidy_chart)

    st.subheader("🎯 Benefit Category Distribution")

    benefit_counts = (
        df["Benefit Category"]
        .value_counts()
    )

    st.bar_chart(benefit_counts)

else:
    st.info("Add citizen records to generate report.")