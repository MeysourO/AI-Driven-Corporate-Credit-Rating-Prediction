import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("model_LR.pkl", "rb") as f:
    model = pickle.load(f)
with open("transformer.pkl", "rb") as f:
    transformer = pickle.load(f)
with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

def preprocess_data(data, transformer, encoder):
    numerical_features = data.select_dtypes(include=[np.number])
    categorical_features = data.select_dtypes(exclude=[np.number])
    transformed_numericals = transformer.transform(numerical_features)
    transformed_categoricals = encoder.transform(categorical_features)
    transformed_data = np.concatenate((transformed_numericals, transformed_categoricals.toarray()), axis=1)
    return transformed_data

st.title("Credit Rating Prediction")

company_symbol = st.text_input("Enter the company's symbol:")
year = st.text_input("Enter the year (yyyy):")
sector = st.text_input("Enter the sector:")
netProfitMargin = st.text_input("Enter Net Profit Margin ratio:")
returnOnAssets = st.text_input("Enter Return On Assets ratio:")
debtRatio = st.text_input("Enter Debt Ratio:")
freeCashFlowOperatingCashFlowRatio = st.text_input("Enter Free Cash Flow/Operating Cash Flow Ratio:")
freeCashFlowPerShare = st.text_input("Enter Free Cash Flow Per Share ratio:")
operatingCashFlowSalesRatio = st.text_input("Enter Operating Cash Flow/Sales Ratio:")

if company_symbol and year and netProfitMargin and returnOnAssets and debtRatio and freeCashFlowOperatingCashFlowRatio and freeCashFlowPerShare and operatingCashFlowSalesRatio:
    data = {
        "Symbol": [company_symbol.upper()],
        "Year": [int(year)],
        "Sector":[sector.upper()],
        "netProfitMargin": [float(netProfitMargin)],
        "returnOnAssets": [float(returnOnAssets)],
        "debtRatio": [float(debtRatio)],
        "freeCashFlowOperatingCashFlowRatio": [float(freeCashFlowOperatingCashFlowRatio)],
        "freeCashFlowPerShare": [float(freeCashFlowPerShare)],
        "operatingCashFlowSalesRatio": [float(operatingCashFlowSalesRatio)]
    }
    data_df = pd.DataFrame.from_dict(data)

    X_val = preprocess_data(data_df, transformer, encoder)

    y_pred = model.predict(X_val)

    st.write(f"The predicted credit rating for {company_symbol.upper()} in {year} is: {y_pred[0]}")

