import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Financial Analyzer",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #666666;
    margin-bottom: 25px;
}

.metric-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    background-color: #fafafa;
    text-align: center;
}

.metric-title {
    font-size: 15px;
    color: #666666;
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("📊 Financial Analyzer")

    st.write(
        "Upload financial data to automatically "
        "clean, analyze and visualize company performance."
    )

    st.divider()

    st.subheader("📁 Required Columns")

    st.write("Your file should contain:")

    st.write("• Date")
    st.write("• Revenue")
    st.write("• Expenses")
    st.write("• Assets")
    st.write("• Liabilities")
    st.write("• Equity")

    st.divider()

    st.subheader("🛠️ Technologies")

    st.write("🐍 Python")
    st.write("🐼 Pandas")
    st.write("📊 Plotly")
    st.write("🌐 Streamlit")

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">📊 Financial Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Automated financial data cleaning, analysis and visualization'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# FILE UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📁 Upload your financial file",
    type=["csv", "xlsx", "xls"]
)

# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    try:

        # -------------------------------------------------
        # READ FILE
        # -------------------------------------------------

        if uploaded_file.name.lower().endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.lower().endswith(".xlsx"):

            df = pd.read_excel(
                uploaded_file,
                engine="openpyxl"
            )

        else:

            df = pd.read_excel(
                uploaded_file,
                engine="xlrd"
            )

        # -------------------------------------------------
        # CLEAN COLUMN NAMES
        # -------------------------------------------------

        df.columns = df.columns.str.strip()

        required_columns = [
            "Date",
            "Revenue",
            "Expenses",
            "Assets",
            "Liabilities",
            "Equity"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:

            st.error("❌ Required columns are missing.")

            st.write("Your file must contain:")

            for column in required_columns:
                st.write(f"• {column}")

            st.write("Missing:")

            for column in missing_columns:
                st.write(f"• {column}")

            st.stop()

        # -------------------------------------------------
        # DATA CLEANING
        # -------------------------------------------------

        original_rows = len(df)

        df = df.drop_duplicates()

        duplicates_removed = (
            original_rows - len(df)
        )

        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

        financial_columns = [
            "Revenue",
            "Expenses",
            "Assets",
            "Liabilities",
            "Equity"
        ]

        for column in financial_columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

        missing_values = (
            df[financial_columns]
            .isnull()
            .sum()
            .sum()
        )

        df[financial_columns] = (
            df[financial_columns]
            .fillna(0)
        )

        df = df.sort_values("Date")

        # -------------------------------------------------
        # FINANCIAL CALCULATIONS
        # -------------------------------------------------

        df["Profit"] = (
            df["Revenue"] -
            df["Expenses"]
        )

        df["Profit_Margin_%"] = (
            df["Profit"] /
            df["Revenue"].replace(0, pd.NA)
        ) * 100

        df["Revenue_Growth_%"] = (
            df["Revenue"].pct_change() * 100
        )

        df["Profit_Growth_%"] = (
            df["Profit"].pct_change() * 100
        )

        df["ROA_%"] = (
            df["Profit"] /
            df["Assets"].replace(0, pd.NA)
        ) * 100

        df["ROE_%"] = (
            df["Profit"] /
            df["Equity"].replace(0, pd.NA)
        ) * 100

        df["Debt_to_Equity"] = (
            df["Liabilities"] /
            df["Equity"].replace(0, pd.NA)
        )

        st.success(
            "✅ File uploaded and analyzed successfully!"
        )

        # =================================================
        # KPI CALCULATIONS
        # =================================================

        total_revenue = df["Revenue"].sum()

        total_expenses = df["Expenses"].sum()

        total_profit = df["Profit"].sum()

        overall_margin = (
            total_profit /
            total_revenue *
            100
            if total_revenue != 0
            else 0
        )

        average_roa = df["ROA_%"].mean()

        average_roe = df["ROE_%"].mean()

        average_debt_equity = (
            df["Debt_to_Equity"].mean()
        )

        # =================================================
        # DASHBOARD KPIs
        # =================================================

        st.subheader("💰 Financial Overview")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Revenue",
            f"₹{total_revenue:,.0f}"
        )

        c2.metric(
            "Total Expenses",
            f"₹{total_expenses:,.0f}"
        )

        c3.metric(
            "Total Profit",
            f"₹{total_profit:,.0f}"
        )

        c4.metric(
            "Profit Margin",
            f"{overall_margin:.2f}%"
        )

        st.divider()

        # =================================================
        # TABS
        # =================================================

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📋 Data",
                "📈 Performance",
                "📊 Ratios",
                "💡 Insights"
            ]
        )

        # =================================================
        # TAB 1 — DATA
        # =================================================

        with tab1:

            st.subheader(
                "🧹 Data Cleaning Summary"
            )

            d1, d2, d3 = st.columns(3)

            d1.metric(
                "Original Rows",
                original_rows
            )

            d2.metric(
                "Duplicates Removed",
                duplicates_removed
            )

            d3.metric(
                "Missing Values Handled",
                missing_values
            )

            st.subheader(
                "📋 Analyzed Financial Data"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        # =================================================
        # TAB 2 — PERFORMANCE
        # =================================================

        with tab2:

            st.subheader(
                "📈 Revenue vs Expenses"
            )

            chart1 = px.line(
                df,
                x="Date",
                y=[
                    "Revenue",
                    "Expenses"
                ],
                markers=True,
                title="Revenue vs Expenses Over Time"
            )

            st.plotly_chart(
                chart1,
                use_container_width=True
            )

            st.subheader(
                "💰 Profit Trend"
            )

            chart2 = px.line(
                df,
                x="Date",
                y="Profit",
                markers=True,
                title="Profit Trend"
            )

            st.plotly_chart(
                chart2,
                use_container_width=True
            )

            st.subheader(
                "📊 Profit Margin"
            )

            chart3 = px.line(
                df,
                x="Date",
                y="Profit_Margin_%",
                markers=True,
                title="Profit Margin Trend"
            )

            st.plotly_chart(
                chart3,
                use_container_width=True
            )

            st.subheader(
                "📈 Revenue & Profit Growth"
            )

            chart4 = px.line(
                df,
                x="Date",
                y=[
                    "Revenue_Growth_%",
                    "Profit_Growth_%"
                ],
                markers=True,
                title="Growth Analysis"
            )

            st.plotly_chart(
                chart4,
                use_container_width=True
            )

        # =================================================
        # TAB 3 — RATIOS
        # =================================================

        with tab3:

            st.subheader(
                "📊 Financial Ratios"
            )

            r1, r2, r3 = st.columns(3)

            r1.metric(
                "Average ROA",
                f"{average_roa:.2f}%"
            )

            r2.metric(
                "Average ROE",
                f"{average_roe:.2f}%"
            )

            r3.metric(
                "Debt-to-Equity",
                f"{average_debt_equity:.2f}"
            )

            st.subheader(
                "⚖️ ROA vs ROE"
            )

            chart5 = px.line(
                df,
                x="Date",
                y=[
                    "ROA_%",
                    "ROE_%"
                ],
                markers=True,
                title="Return on Assets vs Return on Equity"
            )

            st.plotly_chart(
                chart5,
                use_container_width=True
            )

            st.subheader(
                "🏦 Debt-to-Equity Trend"
            )

            chart6 = px.line(
                df,
                x="Date",
                y="Debt_to_Equity",
                markers=True,
                title="Debt-to-Equity Ratio"
            )

            st.plotly_chart(
                chart6,
                use_container_width=True
            )

        # =================================================
        # TAB 4 — INSIGHTS
        # =================================================

        with tab4:

            st.subheader(
                "💡 Automatic Financial Insights"
            )

            highest_revenue = df.loc[
                df["Revenue"].idxmax()
            ]

            highest_profit = df.loc[
                df["Profit"].idxmax()
            ]

            lowest_profit = df.loc[
                df["Profit"].idxmin()
            ]

            highest_margin = df.loc[
                df["Profit_Margin_%"].idxmax()
            ]

            highest_roa = df.loc[
                df["ROA_%"].idxmax()
            ]

            highest_roe = df.loc[
                df["ROE_%"].idxmax()
            ]

            highest_debt = df.loc[
                df["Debt_to_Equity"].idxmax()
            ]

            st.info(
                f"📈 **Highest Revenue:** "
                f"₹{highest_revenue['Revenue']:,.0f} "
                f"in {highest_revenue['Date'].strftime('%Y-%m-%d')}"
            )

            st.info(
                f"💰 **Highest Profit:** "
                f"₹{highest_profit['Profit']:,.0f} "
                f"in {highest_profit['Date'].strftime('%Y-%m-%d')}"
            )

            st.info(
                f"📉 **Lowest Profit:** "
                f"₹{lowest_profit['Profit']:,.0f} "
                f"in {lowest_profit['Date'].strftime('%Y-%m-%d')}"
            )

            st.info(
                f"📊 **Highest Profit Margin:** "
                f"{highest_margin['Profit_Margin_%']:.2f}% "
                f"in {highest_margin['Date'].strftime('%Y-%m-%d')}"
            )

            st.info(
                f"🏦 **Highest ROA:** "
                f"{highest_roa['ROA_%']:.2f}% "
                f"in {highest_roa['Date'].strftime('%Y-%m-%d')}"
            )

            st.info(
                f"💼 **Highest ROE:** "
                f"{highest_roe['ROE_%']:.2f}% "
                f"in {highest_roe['Date'].strftime('%Y-%m-%d')}"
            )

            st.info(
                f"⚠️ **Highest Debt-to-Equity:** "
                f"{highest_debt['Debt_to_Equity']:.2f} "
                f"in {highest_debt['Date'].strftime('%Y-%m-%d')}"
            )

            st.subheader(
                "📌 Overall Assessment"
            )

            if overall_margin >= 30:

                st.success(
                    "🟢 Strong profitability — "
                    "the company has a healthy overall profit margin."
                )

            elif overall_margin >= 15:

                st.warning(
                    "🟡 Moderate profitability — "
                    "the company has a reasonable overall profit margin."
                )

            else:

                st.error(
                    "🔴 Low profitability — "
                    "the company may need to improve revenue "
                    "or control expenses."
                )

        # =================================================
        # DOWNLOAD
        # =================================================

        st.divider()

        st.subheader(
            "📥 Download Your Analysis"
        )

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇️ Download Financial Analysis CSV",
            data=csv_data,
            file_name="financial_analysis_report.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error(
            "❌ The file could not be processed."
        )

        st.info(
            "Make sure your file contains: "
            "Date, Revenue, Expenses, Assets, "
            "Liabilities and Equity."
        )

        st.write(
            "Technical details:",
            e
        )