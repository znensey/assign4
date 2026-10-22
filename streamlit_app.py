# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Zahra Nensey")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "💰 Stock Summary",  "🔎 Interactive Explorer"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Stock Summary
with tabs[3]:
    st.subheader("Microsoft Stock Summary")
    st.write("Average Closing Price: $", round(df["Close"].mean(), 2))
    st.write("Highest Closing Price: $", df["Close"].max())
    st.write("Lowest Closing Price: $", df["Close"].min())


# Tab 5: Interactive Stock Explorer
with tabs[4]:
    st.subheader("Interactive Microsoft Stock Explorer")

    # Prepare stock data
    stock = df.copy()
    stock["Date"] = pd.to_datetime(stock["Date"])
    stock = stock.sort_values("Date")

    # Choose what to analyze
    metric = st.selectbox(
        "Choose a metric:",
        ["Closing Price", "Trading Volume"]
    )

    # Choose how many recent trading days to display
    days = st.slider(
        "Number of trading days:",
        min_value=2,
        max_value=len(stock),
        value=len(stock)
    )

    filtered = stock.tail(days).set_index("Date")

    # Interactive chart
    if metric == "Closing Price":
        st.line_chart(filtered["Close"])
        st.metric(
            "Average Closing Price",
            f"${filtered['Close'].mean():.2f}"
        )
    else:
        st.bar_chart(filtered["Volume"])
        st.metric(
            "Total Trading Volume",
            f"{filtered['Volume'].sum():,.0f}"
        )
