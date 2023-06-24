from fastapi import FastAPI
from typing import Optional
import pandas as pd
import numpy as np
#import ml_api_data as data
import datetime
import joblib

# import data from another py file
#train_data = data.train_data
#train_df = data.train_df
#df_assets = data.df_assets

# Assets dataframe
df_assets = pd.DataFrame({'id_asset' : [1,2,3],
                         'name' : ['BTCUSDT', 'ETHBTC', 'ETHUSDT']})


# import model arima
with open('arima.pkl', 'rb') as pkl:
    model = joblib.load(pkl)


# Create FastAPI App
app = FastAPI()

# Get all assets
@app.get("/api/assets")
def assets(id: Optional[int] = None):
    if id:
        if id not in list(df_assets.id_asset):
            return "Please enter the id nummer between 1-3"
    
        if id in list(df_assets.id_asset):
            df_id = df_assets.loc[df_assets.id_asset == id]
            ids = list(df_id.id_asset)
            names = list(df_id.name)
            return {"data" : [{ "ids": ids,
                              "names" : names}]}
    else:
        ids = list(df_assets.id_asset)
        names = list(df_assets.name)
        return {"data" : [{ "ids": ids,
                          "names" : names}]}


# Predict tomorrow price
@app.get("/api/predict")
def predict(periods : Optional[int] = None):
    if periods:
        yhat = model.predict(n_periods = periods)
        return { "data" : {"prediction" : list(yhat)}  }
    
    else:
        yhat = model.predict(n_periods=1)
        return { "data" : {"prediction" : list(yhat)}  }



# Predict tomorrow price
@app.get("/api/predict_tomorrow_price")
def predict_tomorrow_price(days : int = 1):
    d, p, r, d_plus_1  = arima_predict_tomorrow_price()

    return {
           "data": {"last_date" : d[0],
                    "prediction_date" : str(d_plus_1)[8:18],
                    "prediction_price" :p,
                    "yesterday_price" : r,
                    }
          }
