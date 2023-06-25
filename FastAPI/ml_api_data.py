import pandas as pd
import matplotlib.pyplot as plt
#from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
import joblib

path = 'local_path/data'

df01 = pd.read_csv(f'{path}/All_2017_01_01_to_2023_05_31_daily.csv')
df = df01.loc[df01.id_asset == 1]
df.index = df['timestamp']

# Train test split

train_df = df[0:]['close']
train_data = list(train_df)

# Fit ARIMA model
arima = auto_arima(train_data) 

# Serialize with joblib
#joblib.dump(arima, 'arima.pkl')

# Now you can make predictions using the serialized model
with open('arima.pkl', 'rb') as pkl:
    model = joblib.load(pkl)


# Assets dataframe
df_assets = pd.DataFrame({'id_asset' : [1,2,3],
                         'name' : ['BTCUSDT', 'ETHBTC', 'ETHUSDT']})
