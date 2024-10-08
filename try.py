import calplot
import pandas as pd
import matplotlib.pyplot as plt

# Sample JSON data
data = {
    "1704067200": 1, "1704153600": 1, "1704240000": 1, "1704326400": 1, "1704412800": 1,
    "1704585600": 15, "1705190400": 1, "1705536000": 1, "1705708800": 3, "1705881600": 2,
    "1705968000": 2, "1706313600": 2, "1706659200": 2, "1707264000": 1, "1707350400": 1,
    "1711497600": 2, "1711929600": 6, "1712016000": 3, "1712361600": 2, "1712707200": 6,
    "1712793600": 2, "1712880000": 1, "1713139200": 3, "1713225600": 3, "1713312000": 2,
    "1713398400": 1, "1713571200": 1, "1716940800": 3, "1717027200": 2, "1717113600": 3,
    "1717200000": 1, "1717286400": 11, "1717459200": 3, "1717718400": 4, "1718841600": 9,
    "1718928000": 3, "1719100800": 1, "1719187200": 2, "1719273600": 5, "1719360000": 1,
    "1719446400": 2, "1719705600": 1, "1719792000": 7, "1719878400": 6, "1719964800": 4,
    "1720051200": 4, "1720137600": 1, "1720224000": 7, "1720310400": 3, "1720483200": 5,
    "1720569600": 5, "1722211200": 1, "1722297600": 1, "1722384000": 1, "1690934400": 2,
    "1691107200": 2, "1691193600": 3, "1694390400": 1, "1694822400": 1, "1694908800": 1,
    "1696723200": 7, "1696982400": 2, "1697328000": 5, "1697414400": 1, "1702512000": 4,
    "1703289600": 7, "1703721600": 3, "1703808000": 3, "1703894400": 1, "1703980800": 3
}

# Convert the data to a DataFrame
df = pd.DataFrame(list(data.items()), columns=['Timestamp', 'Count'])

# Convert timestamps to datetime
df['Date'] = pd.to_datetime(df['Timestamp'].astype(int), unit='s')

# Set the date as the index
df.set_index('Date', inplace=True)

# Resample data by day and fill missing values with 0
daily_counts = df['Count'].resample('D').sum().fillna(0)

# Plot the calendar heatmap
plt.figure(figsize=(12, 6))
calplot.calplot(daily_counts, cmap='YlGnBu', figsize=(12, 6))
plt.title('Submission Calendar Heatmap')
plt.show()
