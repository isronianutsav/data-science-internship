from flask import Flask , render_template,request,url_for #importing classes from library
#url_for is used to call functions in html file
import joblib
model=joblib.load("C:\VS CODE\internship_3rd_semester_24105117001\Pandas\model.lb") #here linear regression model we selected
app= Flask(__name__) #magic keyword

@app.route('/', methods=['GET', 'POST'])
def predict():
    pred = None

    if request.method == "POST":
        kms_driven = int(request.form['kms_driven'])
        owner = int(request.form['owner'])
        age = int(request.form['age'])
        power = int(request.form['power'])
        brand_text = request.form['brand_name']

        brand_dict = {
            'TVS':1, 'Royal Enfield':2, 'Triumph':3, 'Yamaha':4,
            'Honda':5, 'Hero':6, 'Bajaj':7, 'Suzuki':8,
            'Benelli':9, 'KTM':10, 'Mahindra':11, 'Kawasaki':12,
            'Ducati':13, 'Hyosung':14, 'Harley-Davidson':15,
            'Jawa':16, 'BMW':17, 'Indian':18, 'Rajdoot':19,
            'LML':20, 'Yezdi':21, 'MV':22, 'Ideal':23
        }

        brand_code = brand_dict[brand_text]

        # ⚠ MUST MATCH TRAINING ORDER
        lst = [[kms_driven, owner, age, power,brand_code]]
        
        # ✅ SAFE SCALAR EXTRACTION
        pred = model.predict(lst).item()
        pred=round(pred)
    return render_template("bike_price_prediction.html", prediction=pred)


if __name__ =="__main__":
     app.run(debug=True) #if u change code internally , then work on web directly #any change continuously appear in terminal
    #run python app.py in terminal for this...
