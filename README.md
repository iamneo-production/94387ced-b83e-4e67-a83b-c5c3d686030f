
# AQI-prediction-using-Temporal-Fusion-Transformer
The Temporal Fusion Transformer (TFT) is a deep learning model for time series forecasting, introduced in a 2019 paper by Bryan Lim, et al. The TFT is based on the Transformer architecture, which was originally developed for natural language processing tasks.

The TFT is designed to handle complex time series data, such as those with multiple seasonalities, irregular sampling intervals, and missing values. It works by encoding the input time series data using stacked self-attention layers, similar to the original Transformer architecture. The output of the encoder is then passed through a decoder that predicts the future values of the time series.

One key innovation of the TFT is the use of a "temporal attention" mechanism, which allows the model to selectively attend to different time points in the input data. This helps the model to better capture complex patterns in the time series data, and allows it to make more accurate predictions.

Overall, the TFT has shown promising results on a variety of time series forecasting tasks, including predicting electricity demand, stock prices, and weather patterns. It is a powerful tool for anyone working with time series data who needs to make accurate forecasts.

### Mean Absolue Error - 13.9366

### Mean Absolue Percentage Error - 17.0010
