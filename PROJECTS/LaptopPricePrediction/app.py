from flask import Flask, render_template, request, url_for
import joblib

# Load trained ML model
model = joblib.load("C:\VS CODE\internship_3rd_semester_24105117001\PROJECTS\LaptopPricePrediction\modelLr.lb")
model_2 = joblib.load("C:\VS CODE\internship_3rd_semester_24105117001\PROJECTS\LaptopPricePrediction\modelsvm.lb")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None   # IMPORTANT for Jinja condition
    prediction_2= None
    if request.method == "POST":
        # Collect already-encoded values from form
        brand = int(request.form['brand'])
        ram = int(request.form['ram'])
        processor_brand = int(request.form['processor_brand'])
        processor_name = int(request.form['processor_name'])
        processor_gnrtn = int(request.form['processor_gnrtn'])
        ssd = int(request.form['ssd'])
        hdd = int(request.form['hdd'])
        os = int(request.form['os'])
        os_bit = int(request.form['os_bit'])
        graphic_card_gb = int(request.form['graphic_card_gb'])
        weight = int(request.form['weight'])
        warranty = int(request.form['warranty'])
        touchscreen = int(request.form['Touchscreen'])
        msoffice = int(request.form['msoffice'])
        ram_type = int(request.form['ram_type'])
        # ⚠ MUST MATCH TRAINING FEATURE ORDER
        features = [[
            brand,
            processor_brand,
            processor_name,
            processor_gnrtn,
            ram,
            ram_type,
            ssd,
            hdd,
            os,
            os_bit,
            graphic_card_gb,
            weight,
            warranty,
            touchscreen,
            msoffice
]]

        # Predict laptop price
        prediction = model.predict(features).item()
        prediction = round(prediction)
        prediction_2 = model_2.predict(features).item()
        prediction_2 = round(prediction_2)

    return render_template(
        "project.html",
        prediction=prediction,
        prediction_2=prediction_2
    )


if __name__ == "__main__":
    app.run(debug=True)
