from flask import Flask, render_template, request
import joblib

# Load trained classification models
svc_model = joblib.load("C:\VS CODE\internship_3rd_semester_24105117001\PROJECTS\CustomerSatisfactionPrediction\model.lb")
knn_model = joblib.load("C:\VS CODE\internship_3rd_semester_24105117001\PROJECTS\CustomerSatisfactionPrediction\model2.lb")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction_svc = None
    prediction_knn = None

    if request.method == "POST":
        customer_type = int(request.form['customer_type'])
        type_of_travel = int(request.form['type_of_travel'])
        travel_class = int(request.form['travel_class'])
        flight_distance = int(request.form['flight_distance'])
        inflight_entertainment = int(request.form['inflight_entertainment'])
        baggage_handling = int(request.form['baggage_handling'])
        cleanliness = int(request.form['cleanliness'])
        departure_delay = int(request.form['departure_delay'])

        # ⚠ EXACT TRAINING ORDER
        features = [[
            customer_type,
            type_of_travel,
            travel_class,
            flight_distance,
            inflight_entertainment,
            baggage_handling,
            cleanliness,
            departure_delay
        ]]

        svc_pred = svc_model.predict(features)[0]
        knn_pred = knn_model.predict(features)[0]

        prediction_svc = "Satisfied" if svc_pred == 1 else "Not Satisfied"
        prediction_knn = "Satisfied" if knn_pred == 1 else "Not Satisfied"

    return render_template(
        "project.html",
        prediction_svc=prediction_svc,
        prediction_knn=prediction_knn
    )

if __name__ == "__main__":
    app.run(debug=True)
