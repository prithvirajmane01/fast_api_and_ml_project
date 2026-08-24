# FastAPI and Machine Learning Loan Prediction

## 📌 Project Overview

This project combines **Machine Learning** and **FastAPI** to build a loan approval prediction API.

The trained machine learning model receives user information such as:

* Income
* Age
* Loan amount

The API processes this data and returns a loan prediction.

---

## 🛠️ Technologies Used

* Python
* FastAPI
* Scikit-learn
* Pandas
* Uvicorn
* Pydantic

---

## 📂 Project Structure

```text
fast_api_and_ml_project/
│
├── schema/
│   └── user_input.py
│
├── application.py
├── model.py
├── frontend_for_fast.py
├── loan_approval.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/prithvirajmane01/fast_api_and_ml_project.git
```

### 2. Move into the project folder

```bash
cd fast_api_and_ml_project
```

### 3. Create a virtual environment

```bash
python -m venv .fast_ml
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.fast_ml\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the FastAPI Application

Run the application using:

```bash
uvicorn application:app --reload
```

The server should start at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the API directly from the Swagger UI.

---

## 🔮 Prediction Endpoint

### Endpoint

```text
POST /predict
```

The API accepts user input and uses the trained machine learning model to generate a prediction.

Example response:

```json
{
  "prediction_category": 1
}
```

---

## 🧠 Machine Learning Model

The trained machine learning model is stored in:

```text
loan_approval.pkl
```

The FastAPI application loads this model and uses it to make predictions from the input data.

---

## 👨‍💻 Author

**Prithviraj Mane**

GitHub: https://github.com/prithvirajmane01

---

## 📜 License

This project is created for learning and educational purposes.
