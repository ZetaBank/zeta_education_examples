import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load Tesla and Ferrari stock data
tesla_data = pd.read_csv('tesla_quote.csv', parse_dates=True, index_col='Date')
ferrari_data = pd.read_csv('ferrari_quote.csv', parse_dates=True, index_col='Date')

# Define the period for both charts (e.g., '2022-01-01' to '2022-12-31')
start_date = '2022-01-01'
end_date = '2022-12-31'

# Filter dataframes to include only the specified period
tesla_data = tesla_data[(tesla_data.index >= start_date) & (tesla_data.index <= end_date)]
ferrari_data = ferrari_data[(ferrari_data.index >= start_date) & (ferrari_data.index <= end_date)]

# Create subplots with 2 columns to display charts side by side
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

# Define candlestick colors
up_color = 'g'
down_color = 'r'

# Plot Tesla candlesticks and 20-day moving average
for idx, row in tesla_data.iterrows():
    open_price = row['Open']
    close_price = row['Close']
    high_price = row['High']
    low_price = row['Low']

    if close_price > open_price:
        color = up_color
        rect_height = close_price - open_price
        y = open_price
    else:
        color = down_color
        rect_height = open_price - close_price
        y = close_price

    ax1.add_patch(plt.Rectangle((mdates.date2num(idx) - 0.2, y), 0.4, rect_height, fill=True, color=color, zorder=2))
    ax1.plot([mdates.date2num(idx), mdates.date2num(idx)], [low_price, high_price], color='black', zorder=1)

# Calculate 20-day moving average for Tesla based on revised closing price
tesla_data['20D_MA'] = tesla_data['Close'].rolling(window=20).mean()
ax1.plot(tesla_data.index, tesla_data['20D_MA'], label='20-Day MA', color='orange', linestyle='--')

# Calculate 60-day moving average for Tesla based on revised closing price
tesla_data['60D_MA'] = tesla_data['Close'].rolling(window=60).mean()
ax1.plot(tesla_data.index, tesla_data['60D_MA'], label='60-Day MA', color='purple', linestyle='--')

# Set x-axis format for Tesla chart
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
ax1.set_ylabel('Price')
ax1.set_title('Tesla Candlestick Chart with MAs (Revised Closing Price)')
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left')

# Plot Ferrari candlesticks and 20-day moving average
for idx, row in ferrari_data.iterrows():
    open_price = row['Open']
    close_price = row['Close']
    high_price = row['High']
    low_price = row['Low']

    if close_price > open_price:
        color = up_color
        rect_height = close_price - open_price
        y = open_price
    else:
        color = down_color
        rect_height = open_price - close_price
        y = close_price

    ax2.add_patch(plt.Rectangle((mdates.date2num(idx) - 0.2, y), 0.4, rect_height, fill=True, color=color, zorder=2))
    ax2.plot([mdates.date2num(idx), mdates.date2num(idx)], [low_price, high_price], color='black', zorder=1)

# Calculate 20-day moving average for Ferrari based on revised closing price
ferrari_data['20D_MA'] = ferrari_data['Close'].rolling(window=20).mean()
ax2.plot(ferrari_data.index, ferrari_data['20D_MA'], label='20-Day MA', color='orange', linestyle='--')

# Calculate 60-day moving average for Ferrari based on revised closing price
ferrari_data['60D_MA'] = ferrari_data['Close'].rolling(window=60).mean()
ax2.plot(ferrari_data.index, ferrari_data['60D_MA'], label='60-Day MA', color='purple', linestyle='--')

# Set x-axis format for Ferrari chart
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
ax2.set_ylabel('Price')
ax2.set_title('Ferrari Candlestick Chart with MAs (Revised Closing Price)')
ax2.tick_params(axis='x', rotation=45)
ax2.legend(loc='upper left')

# Adjust layout and show both charts
plt.tight_layout()
plt.show()
