# 🌍 Human Development Index (HDI) Prediction System

## 📌 Project Overview

The Human Development Index (HDI) Prediction System is a Machine Learning web application developed using Python, Flask, and Linear Regression. This application predicts the Human Development Index (HDI) of a country based on various socio-economic indicators such as life expectancy, education, income, internet access, and social support.

The project integrates Machine Learning with a web-based user interface to provide an interactive prediction system.

---

## 🎯 Objectives

- Predict the Human Development Index (HDI) score.
- Classify countries into HDI categories.
- Build a user-friendly web application using Flask.
- Apply Machine Learning concepts to real-world data.
- Visualize and analyze development indicators.

---
# 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Linear Regression

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Web Development
- Flask
- HTML
- CSS

### Model Serialization
- Pickle

### Version Control
- Git
- GitHub


---

# 📊 Dataset Features

The model predicts HDI using the following indicators:

| Feature |
|---------|
| Life Expectancy |
| Expected Years Schooling |
| Mean Years Schooling |
| GNI per Capita |
| Human Inequality |
| Adult Literacy |
| Internet Users |
| Electricity Access |
| Healthy Life Expectancy |
| Social Support |

---

# 🤖 Machine Learning Model

### Algorithm Used


Linear Regression


### Model Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Saving
9. Web Deployment

---

## 📊 Visualizations

### Correlation Heatmap

<img width="800" height="600" alt="heatmap" src="https://github.com/user-attachments/assets/54fc22f3-e07e-49b8-99f1-87d16c51c508" />


---

### Mean_Year_Schooling vs  HDI

<img width="1000" height="600" alt="scatter plot (Mean years of schooling vs hdi)" src="https://github.com/user-attachments/assets/6710c58f-8048-4238-9239-1b2a889bd43c" />


---

### Life Expectancy vs HDI

<img width="640" height="480" alt="life_expency vs hdi" src="https://github.com/user-attachments/assets/4a80269a-0eaf-4cad-bba9-210a72aaadc7" />



---
# 📈 Performance Evaluation

### Evaluation Metric


R² Score


The model performance is evaluated using the coefficient of determination (R² score).

---

## 🏆 HDI Classification

| HDI Score | Category |
|-----------|----------|
| < 0.40 | Low HDI |
| 0.40 - 0.69 | Medium HDI |
| 0.70 - 0.79 | High HDI |
| ≥ 0.80 | Very High HDI |

---

## 📁 Project Structure

```
HDI-Prediction-System/
│
├── app.py
├── hdi.csv
├── hdi_prediction_model.pkl
├── requirements.txt
├── README.md
│
└── templates/
    ├── home.html
    ├── indexnew.html
    └── resultnew.html
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone
https://github.com/ThanusreeThatigotla/Human-Development-Index-HDI-Prediction-System/edit/main/README.md
```

### Navigate to project directory

```bash
cd HDI-Prediction-System
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

---

## 🌐 Open in Browser

Visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. Open Home Page
2. Click "Start Prediction"
3. Enter development indicators
4. Click "Predict HDI"
5. View predicted HDI score and category

---

## 📈 Sample Prediction

| Feature | Value |
|---------|-------|
| Life Expectancy | 75 |
| Expected Years Schooling | 16 |
| Mean Years Schooling | 12 |
| GNI per Capita | 25000 |
| Human Inequality | 20 |
| Adult Literacy | 95 |
| Internet Users | 85 |
| Electricity Access | 100 |
| Healthy Life Expectancy | 70 |
| Social Support | 0.85 |

### Prediction Output

```
Predicted HDI Score: 0.709
HDI Category: High HDI
```

---
# Project Output UI Be Like:

<img width="1607" height="858" alt="Screenshot 2026-07-02 090146" src="https://github.com/user-attachments/assets/70062548-cc80-4ba1-8566-170df804d540" />

<img width="1592" height="847" alt="Screenshot 2026-07-02 090310" src="https://github.com/user-attachments/assets/916506bd-8e05-44f5-b7f3-ca873e6b376a" />

<img width="1548" height="833" alt="Screenshot 2026-07-02 090521" src="https://github.com/user-attachments/assets/99d20147-2d6e-4913-952d-d1376bc37c1a" />



## 🔮 Future Enhancements

- Deploy the application online
- Add graphical visualizations
- Compare multiple countries
- Implement additional machine learning models
- Improve prediction accuracy

---

## 👩‍💻 Developer

**Thanusree Thatigotla**

B.Tech (Artificial Intelligence and Machine Learning)

---
