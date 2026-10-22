# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Zahra Nensey")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "💸 Investment Simulator"])

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


# Tab 4: Investment Simulator
with tabs[3]:
    st.subheader("What If I Invested in Microsoft?")

    investment = st.number_input("Enter investment amount ($):", min_value=100, value=1000, step=100)

    # Calculate investment value over time
    stock_prices = df["Close"]
    investment_values = investment * (stock_prices / stock_prices.iloc[0])

    final_value = investment_values.iloc[-1]
    profit = final_value - investment

    st.write("Final Investment Value: $", round(final_value, 2))
    st.write("Profit or Loss: $", round(profit, 2))

    st.subheader("Investment Growth Over Time")
    st.line_chart(investment_values)



