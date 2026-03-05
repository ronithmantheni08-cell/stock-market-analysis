import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Download NVIDIA data
df = yf.download("NVDA", period="1y")

# 2. Calculate the 20-day Moving Average
df['MA20'] = df['Close'].rolling(window=20).mean()

# 3. Create the Visual
plt.figure(figsize=(10,5))
plt.plot(df['Close'], label='NVDA Price', color='blue', alpha=0.5)
plt.plot(df['MA20'], label='20-Day Trend', color='red', lw=2)
plt.title('NVIDIA Market Analysis')
plt.legend()

# 4. Show the graph
plt.show()