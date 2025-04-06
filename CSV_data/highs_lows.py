import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Get high temperatures from the file
filename = 'nairobi_weather_jan2024.csv'
with open(filename) as fn:
    reader = csv.reader(fn)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[2])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Format plot
plt.title('Daily high temperatures, Nairobi, 2024')
plt.xlabel('')
plt.ylabel('Temperatures')

# Plot data
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.show()
