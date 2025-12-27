# 🐍💻 Laptop Price Prediction System (Flask Web App)

This repository contains a **Flask-based machine learning web application** designed to predict **laptop prices** based on multiple hardware and software specifications.  
The system integrates trained ML models with a web interface to provide real-time price predictions.

---

## 📌 Project Overview

The Laptop Price Prediction System demonstrates **end-to-end ML deployment** using Flask.  
Users enter laptop configuration details through a web form, and the backend generates predicted prices using trained regression models.

This project is suitable for:
- Data Science & Machine Learning internships
- Flask backend development practice
- ML model deployment demonstrations
- Academic and portfolio projects

---

## ⚙️ Application Workflow
- User submits laptop specifications via a web form
- Backend processes encoded feature values
- Trained ML models predict laptop prices
- Predictions are displayed dynamically on the web page
- Deployed as a template-based Flask web application using Jinja2 templates
---

## 🛠 Libraries & Frameworks Used

### 🐍 `Flask`
Flask is a **lightweight Python web framework** used to:
- Build the backend web application
- Handle routing and HTTP requests
- Connect machine learning logic with frontend templates
- Serve prediction results dynamically

---

### 🐍 `render_template`
Used for:
- Rendering HTML templates
- Displaying prediction results and dynamic content on web pages

---

### 🐍 `request`
Used for:
- Collecting form data submitted by users
- Handling POST requests securely within the Flask application

---

### 🐍 `url_for`
Used for:
- Dynamically generating URLs
- Linking Flask routes with frontend HTML files safely

---

### 🐍 `joblib`
Joblib is used for:
- Loading pre-trained machine learning models
- Efficient model serialization and deserialization
- Integrating ML models into production-ready applications

---

## 🤖 Machine Learning Models Used
- **Linear Regression Model**
- **Support Vector Machine (SVM) Regression Model**

Both models independently generate predictions to allow comparative analysis.

---

## ⚙️ Technical Details
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Model Type:** Regression
- **Input Method:** Web-based form
- **Output:** Predicted laptop price (₹)
- **Development Mode:** Debug enabled

---

## 🔑 Execution Requirements
- Python 3.x installed
- Flask installed
- Joblib installed
- Trained ML model files available
- Web browser for application access

---

## ▶️ How to Run
1. Open terminal in the project directory  
2. Run the Flask application:
```bash
python app.py
```
3. Open the local server URL in a browser  
4. Enter laptop specifications and view predictions  

---

## 📚 Learning Outcomes
- Deployment of ML models using Flask  
- Integration of frontend and backend systems  
- Practical ML inference pipeline implementation  
- Understanding feature-based prediction systems  

---

## 🚀 Future Enhancements
- Improve prediction accuracy with additional features  
- Add database support for storing predictions  
- Enhance UI/UX design  
- Add authentication and user sessions  
- Deploy application to cloud platforms  

---

## 👤 Author
**isronianutsav**  
B.Tech Engineering Student  
🐍 Python | Flask | Machine Learning | Model Deployment 🚀