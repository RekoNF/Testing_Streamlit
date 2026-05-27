import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression

# 1. Load data
@st.cache_data
def load_data():
    data = pd.read_csv(r'C:\Users\Mareko\OneDrive\Documents\Python Statistika\DataSets\nvidia_stock_data_1999_2026.csv')
    return data

data = load_data()

# 2. Tampilkan data awal
st.title('Analisis Tren Harga Saham Nvidia')
st.subheader('Data Awal')
st.dataframe(data.head(1000))

# 3. Pastikan kolom date bertipe datetime dan urutkan
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values('date')

# 4. Visualisasi tren harga saham (open, close, high, low)
st.subheader('Visualisasi Tren Harga Saham')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['date'], data['open'], label='Open', color='blue')
ax.plot(data['date'], data['close'], label='Close', color='orange')
ax.plot(data['date'], data['high'], label='High', color='green', alpha=0.5)
ax.plot(data['date'], data['low'], label='Low', color='red', alpha=0.5)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga (USD)')
ax.set_title('Tren Harga Saham Nvidia')
ax.legend()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)
st.pyplot(fig)

# 5. Statistik deskriptif tren harga
st.subheader('Statistik Deskriptif Harga')
st.write(data[['open', 'close', 'high', 'low']].describe())

# 6. Moving Average (MA) untuk smoothing tren
data['MA50'] = data['close'].rolling(window=50).mean()
data['MA200'] = data['close'].rolling(window=200).mean()
st.subheader('Moving Average (MA) 50 & 200 Hari')
fig_ma, ax_ma = plt.subplots(figsize=(10, 5))
ax_ma.plot(data['date'], data['close'], label='Close', color='gray', alpha=0.5)
ax_ma.plot(data['date'], data['MA50'], label='MA 50 Hari', color='blue')
ax_ma.plot(data['date'], data['MA200'], label='MA 200 Hari', color='red')
ax_ma.set_xlabel('Tanggal')
ax_ma.set_ylabel('Harga (USD)')
ax_ma.set_title('Moving Average Harga Saham Nvidia')
ax_ma.legend()
ax_ma.xaxis.set_major_locator(mdates.YearLocator())
ax_ma.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)
st.pyplot(fig_ma)

# 7. Regresi Linier Sederhana (date vs close)
st.subheader('Regresi Linier Tren Harga')
data = data.dropna(subset=['close'])
X_time = (data['date'] - data['date'].min()).dt.days.values.reshape(-1, 1)
y_close = data['close'].values
reg = LinearRegression()
reg.fit(X_time, y_close)
trend_pred = reg.predict(X_time)
fig_reg, ax_reg = plt.subplots(figsize=(10, 5))
ax_reg.plot(data['date'], y_close, label='Close', color='gray', alpha=0.5)
ax_reg.plot(data['date'], trend_pred, label='Regresi Linier', color='magenta')
ax_reg.set_xlabel('Tanggal')
ax_reg.set_ylabel('Harga (USD)')
ax_reg.set_title('Regresi Linier Tren Harga Saham Nvidia')
ax_reg.legend()
ax_reg.xaxis.set_major_locator(mdates.YearLocator())
ax_reg.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)
st.pyplot(fig_reg)

# 8. Insight tren
st.subheader('Insight Tren Harga Saham Nvidia')
st.write(f"\n- Harga rata-rata saham Nvidia: {data['close'].mean():.2f} USD")
st.write(f"- Harga minimum: {data['close'].min():.2f} USD pada {data.loc[data['close'].idxmin(), 'date'].date()}")
st.write(f"- Harga maksimum: {data['close'].max():.2f} USD pada {data.loc[data['close'].idxmax(), 'date'].date()}")
st.write(f"- Slope regresi linier (kenaikan rata-rata per hari): {reg.coef_[0]:.4f} USD/hari")
st.write(f"- Kenaikan harga selama periode data: {y_close[-1] - y_close[0]:.2f} USD")
