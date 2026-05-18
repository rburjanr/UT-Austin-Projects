from flask import Flask, request, jsonify
import joblib, pandas as pd, numpy as np

app = Flask(__name__)
model = joblib.load("superkart_rf_model.pkl")

NUMERIC_FEATURES = ['Product_Weight', 'Product_Allocated_Area',
                    'Product_MRP', 'Store_Age']
ORDINAL_FEATURES = ['Product_Sugar_Content', 'Store_Size',
                    'Store_Location_City_Type', 'MRP_Band']
NOMINAL_FEATURES = ['Product_Type', 'Store_Type']

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df['Store_Age'] = 2024 - int(data.get('Store_Establishment_Year', 2000))
    df['MRP_Band'] = pd.cut([float(data['Product_MRP'])],
                             bins=4, labels=['Budget','Economy','Premium','Luxury'])[0]
    df = pd.get_dummies(df)
    prediction = model.predict(df)[0]
    return jsonify({"predicted_sales": round(float(prediction), 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)