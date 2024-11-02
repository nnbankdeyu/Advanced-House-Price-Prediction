import streamlit as st
import joblib
import numpy as np

# Function to load models
@st.cache_data()
def load_model(file_path):
    model = joblib.load(file_path)
    return model

# Load both models
ridge_model = load_model("D:\\Python\\housing price prediction\\ridge_final.pkl")
elastic_net_model = load_model("D:\\Python\\housing price prediction\\elastic_net_final.pkl")

# Model selection
model_options = {"Ridge Regression": ridge_model, "Elastic Net": elastic_net_model}
model_choice = st.selectbox("Choose a model for prediction", list(model_options.keys()))
model = model_options[model_choice]

# Title and description
st.title("House Price Prediction App")
st.write("Select a model and enter values for the following features to predict the house price:")

# Input fields for the 10 selected features
overall_qual = st.number_input("Overall Quality (OverallQual)", min_value=0.0, value=1.0, step=0.01)
garage_area = st.number_input("Garage Area (GarageArea) in square feet", min_value=0.0, value=1.0, step=0.01)
fireplaces = st.number_input("Number of Fireplaces (Fireplaces)", min_value=0.0, value=1.0, step=0.01)
bsmt_qual_ex = st.number_input("Basement Quality Excellent (BsmtQual_Ex)", min_value=0.0, value=0.0, step=0.01)
bedroom_abv_gr = st.number_input("Bedrooms Above Grade (BedroomAbvGr)", min_value=0.0, value=1.0, step=0.01)
lot_area = st.number_input("Lot Area (LotArea) in square feet", min_value=0.0, value=1.0, step=0.01)
bsmt_qual_gd = st.number_input("Basement Quality Good (BsmtQual_Gd)", min_value=0.0, value=0.0, step=0.01)
bsmt_fin_type1_glq = st.number_input("Basement Fin Type 1 GLQ (BsmtFinType1_GLQ)", min_value=0.0, value=0.0, step=0.01)
overall_cond = st.number_input("Overall Condition (OverallCond)", min_value=0.0, value=1.0, step=0.01)
remodeled_age = st.number_input("Remodeled Age (RemodeledAge)", min_value=0.0, value=0.0, step=0.01)

# Create input array for prediction with all 10 features
input_features = np.zeros(10)  # Initialize array with 10 features
input_features[0] = overall_qual         # OverallQual
input_features[1] = garage_area           # GarageArea
input_features[2] = fireplaces             # Fireplaces
input_features[3] = bsmt_qual_ex          # BsmtQual_Ex
input_features[4] = bedroom_abv_gr        # BedroomAbvGr
input_features[5] = lot_area              # LotArea
input_features[6] = bsmt_qual_gd          # BsmtQual_Gd
input_features[7] = bsmt_fin_type1_glq    # BsmtFinType1_GLQ
input_features[8] = overall_cond           # OverallCond
input_features[9] = remodeled_age          # RemodeledAge

# Predict button
if st.button("Predict"):
    prediction = model.predict([input_features])  # Provide a list containing input_features
    st.write("Predicted House Price: $", round(prediction[0], 2))