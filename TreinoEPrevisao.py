import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Carregar os dados
csv_path = 'Dataset/merged_hemispheres.csv'  # Substitua pelo caminho correto
data = pd.read_csv(csv_path)

# Preparar os dados para o Prophet
data['date'] = pd.to_datetime(data['Year'].astype(str) + data['Month'], format='%Y%b')
data = data.set_index('date')
data = data[['NorthHemisphere', 'SouthHemisphere']]
data = data.asfreq('MS', fill_value=0.0)

# Plotar as duas séries temporais para comparação
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar as mudanças de temperatura para o hemisfério sul e norte
ax.plot(data.index.year, data['SouthHemisphere'], label='South Hemisphere', color='blue')
ax.plot(data.index.year, data['NorthHemisphere'], label='North Hemisphere', color='red')

# Adicionar rótulos e título
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomalies (°C)')
plt.title('Mudanças de Temperatura: Hemisfério Norte vs Hemisfério Sul')

# Adicionar a legenda
ax.legend()

# Exibir o gráfico
plt.show()

# Dividir os dados em treino e teste
steps = 300  # Número de meses para o conjunto de teste
data_train = data[:-steps]
data_test = data[-steps:]

# Prophet exige que o dataframe tenha as colunas 'ds' (data) e 'y' (valor a ser previsto)
data_prophet = data_train.reset_index().rename(columns={'date': 'ds', 'SouthHemisphere': 'y'})

# Adicionar o NorthHemisphere como um regressor (variável exógena)
model = Prophet(changepoint_prior_scale=1)
model.add_regressor('NorthHemisphere')

# Adicionar sazonalidades personalizadas
#model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)
#model.add_seasonality(name='semiannual', period=182.5, fourier_order=10)
model.add_seasonality(name='yearly', period=365.25, fourier_order=60)

# Ajustar o modelo aos dados de treino
model.fit(data_prophet)

# Preparar os dados futuros para previsão, incluindo a variável exógena
future = data_test.reset_index().rename(columns={'date': 'ds'})[['ds', 'NorthHemisphere']]

# Fazer previsões
forecast = model.predict(future)

# Extrair previsões para o período de teste
predictions = forecast[['ds', 'yhat']].set_index('ds')

# Plotar os valores reais vs. previsões
fig, ax = plt.subplots(figsize=(12, 9))
data_train['SouthHemisphere'].plot(ax=ax, label='South Hemisphere - train')
data_test['SouthHemisphere'].plot(ax=ax, label='South Hemisphere - test', color='red')
predictions['yhat'].plot(ax=ax, label='Predictions', color='green')
ax.legend()
plt.show()

# Calcular métricas de erro: RMSE, MAE, MAPE
y_true = data_test['SouthHemisphere']
y_pred = predictions['yhat']

# RMSE
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print(f'RMSE: {rmse}')

# MAE
mae = mean_absolute_error(y_true, y_pred)
print(f'MAE: {mae}')

# MAPE (Mean Absolute Percentage Error)
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
print(f'MAPE: {mape}%')
