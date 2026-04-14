# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the dataset
# df = pd.read_csv('sales.csv')

# # Show the first few rows
# print("First 5 rows of the dataset:")
# print(df.head())

# # Total units sold and revenue
# total_units = df['units_sold'].sum()
# total_revenue = df['revenue'].sum()
# print(f"\nTotal units sold: {total_units}")
# print(f"Total revenue: ${total_revenue}")

# # Best-selling product by units sold
# best_product = df.groupby('product')['units_sold'].sum().idxmax()
# print(f"\nBest-selling product: {best_product}")

# # Group by date to show total revenue per day
# daily_revenue = df.groupby('date')['revenue'].sum()
# print("\nDaily Revenue:")
# print(daily_revenue)

# # Plot total revenue over time
# plt.figure(figsize=(8,5))
# sns.lineplot(data=daily_revenue)
# plt.title('Daily Revenue Over Time')
# plt.xlabel('Date')
# plt.ylabel('Revenue')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Plot units sold by product
# plt.figure(figsize=(8,5))
# product_units = df.groupby('product')['units_sold'].sum().sort_values(ascending=False)
# sns.barplot(x=product_units.index, y=product_units.values)
# plt.title('Total Units Sold by Product')
# plt.xlabel('Product')
# plt.ylabel('Units Sold')
# plt.tight_layout()
# plt.show()



# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import uuid
import joblib
import os
from ml_model import train_or_load_model, predict_risk

app = Flask(__name__)
CORS(app)

# simple in-memory stores (for prototype)
SENSORS = []           # store raw sensor reports
HELP_REQUESTS = []     # store help requests
ALERTS = []            # store generated alerts

MODEL_PATH = "backend/risk_model.joblib"
model = train_or_load_model(MODEL_PATH)

@app.route("/ingest_sensor", methods=["POST"])
def ingest_sensor():
    """
    Expected JSON:
    {
      "sensor_id": "...",
      "location": {"lat": xx, "lon": yy},
      "timestamp": "ISO string",
      "rain_mm": float,
      "soil_moisture": float,
      "river_level_m": float,
      "wind_speed": float,
      "temperature": float
    }
    """
    data = request.get_json()
    data["received_at"] = datetime.datetime.utcnow().isoformat()
    data["id"] = str(uuid.uuid4())
    SENSORS.append(data)

    # Run a quick risk prediction
    risk_prob = predict_risk(model, data)
    if risk_prob >= 0.5:
        alert = {
            "id": str(uuid.uuid4()),
            "level": "HIGH" if risk_prob >= 0.8 else "MEDIUM",
            "message": f"High flood/fire risk detected (score={risk_prob:.2f})",
            "location": data.get("location"),
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        ALERTS.append(alert)
        # in real system: push notifications / SMS / WhatsApp via integrations
    return jsonify({"status": "ok", "risk": float(risk_prob)}), 201

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify(ALERTS)

@app.route("/help_request", methods=["POST"])
def help_request():
    """
    {
      "name": "Ramesh",
      "contact": "7000xxxxxx",
      "location": {"lat":.., "lon":..},
      "needs": ["rescue","food"]
    }
    """
    data = request.get_json()
    data["id"] = str(uuid.uuid4())
    data["timestamp"] = datetime.datetime.utcnow().isoformat()
    HELP_REQUESTS.append(data)
    # For prototype, create a small alert for volunteers
    ALERTS.append({
        "id": str(uuid.uuid4()),
        "level": "REQUEST",
        "message": f"Help requested by {data.get('name')} - {', '.join(data.get('needs',[]))}",
        "location": data.get("location"),
        "timestamp": data["timestamp"]
    })
    return jsonify({"status": "ok", "request_id": data["id"]}), 201

@app.route("/help_requests", methods=["GET"])
def list_help_requests():
    return jsonify(HELP_REQUESTS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
