🏠 California House Price Prediction Web Application

An end-to-end **Machine Learning web application** that predicts house prices using the **California Housing Dataset**, built with **Flask** and **Scikit-learn**.

This project demonstrates the complete ML lifecycle — from data preprocessing and model training to web deployment and user interaction.

---

## 📌 Project Highlights

- Real-world regression problem
- Handles both **numerical and categorical features**
- Uses **ML Pipelines** for preprocessing + modeling
- Interactive **web-based UI**
- Clean project structure with Git & GitHub version control

---

## 🚀 Tech Stack

| Category | Technologies |
|--------|-------------|
| Language | Python 3.11 |
| Backend | Flask |
| ML | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Frontend | HTML, CSS |
| Version Control | Git, GitHub |

---

## 📊 Dataset

- **Name:** California Housing Dataset  
- **Features:**
  - longitude  
  - latitude  
  - housing_median_age  
  - total_rooms  
  - total_bedrooms  
  - population  
  - households  
  - median_income  
  - ocean_proximity (categorical)
- **Target Variable:** `median_house_value`

---

## 🧠 Machine Learning Approach

- Missing values handled using median imputation
- Categorical feature encoded using **One-Hot Encoding**
- **ColumnTransformer** used for preprocessing
- **Linear Regression** model used for prediction
- End-to-end **Pipeline** ensures consistency during training and inference

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vamshi-boini/House-price-prediction-using-ml.git
cd House-price-prediction-using-ml/backend
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Train the Model
bash
Copy code
python train_model.py
5️⃣ Run the Flask App
bash
Copy code
python app.py
6️⃣ Open in Browser
cpp
Copy code
http://127.0.0.1:5000/
🖥️ Application Workflow
User enters housing details via web form

Flask backend receives input

Data is preprocessed using trained pipeline

ML model predicts house price

Result is displayed on the web interface

📁 Project Structure
powershell
Copy code
House-price-prediction-using-ml/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│   ├── templates/
│   └── static/
│
├── data/
│   └── housing.csv
│
├── .gitignore
├── README.md
🎯 Learning Outcomes
Practical understanding of ML regression problems

Experience with real-world datasets

Building ML pipelines for deployment

Flask-based backend development

GitHub project structuring and version control

📌 Future Enhancements
Add advanced models (Random Forest, XGBoost)

Include model evaluation metrics (RMSE, R²)

Convert Flask backend to FastAPI

Deploy application on cloud platforms (Render / AWS)

Improve UI with charts and validation

👤 Author
Boini Vamshi
Final Year B.Tech Student
Aspiring Machine Learning & Software Engineer


---







