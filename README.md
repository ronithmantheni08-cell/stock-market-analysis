# Financial Intelligence: NVIDIA (NVDA) Market Analysis
**Technical Stack:** Python (yfinance, Pandas, Matplotlib)

## 📌 Project Overview
This project leverages the yfinance API to pull real-time financial data for NVIDIA. I developed a trend-tracking engine to visualize moving averages, helping to filter market noise and identify long-term price momentum.

## ⚙️ The Technical Process
- **Data Acquisition:** Automated the retrieval of 1-year historical trading data using the `yfinance` library.
- **Feature Engineering:** Calculated a **20-Day Moving Average (MA20)** using Pandas' rolling window function to smooth out daily volatility.
- **Visualization:** Built a dual-axis line chart comparing the raw closing price against the 20-day trend line to highlight breakout points.

## 💡 Visual Output

![NVIDIA Market Trend](" src="https://github.com/user-attachments/assets/75e36260-9fb4-409a-96f7-6a7724d06e4b" />)
*(Pictured: The NVDA price trend showing the 20-day moving average identifying momentum shifts in late 2025.)*
