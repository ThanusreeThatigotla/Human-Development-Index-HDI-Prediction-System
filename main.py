import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from flask import Flask, render_template, request

# ==========================
# LOAD DATASET
# ==========================
df = pd.read_csv("hdi.csv")

print("\nFirst 20 rows:")
print(df.head(20))

print("\nFirst 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset info:")
df.info()

print("\nStatistical summary:")
print(df.describe())

print("\nNull values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

if 'Country' in df.columns:
    print("\nCountries:")
    print(df['Country'].unique())
# ==========================
# Null Values Verification
# ==========================
print("\nNull Values Verification")
print("-" * 30)

null_values = df.isnull().sum()

if null_values.sum() == 0:
    print("No null values found in the dataset.")
else:
    print(null_values[null_values > 0])

# ==========================
# VISUALIZATION 1
# ==========================
if 'Mean_Years_Schooling' in df.columns and 'HDI' in df.columns:
    plt.figure(figsize=(8, 5))

    sns.stripplot(
        x='Mean_Years_Schooling',
        y='HDI',
        data=df.head(20),
        jitter=True
    )

    plt.title("Mean Years of Schooling vs HDI")
    plt.xlabel("Mean Years of Schooling")
    plt.ylabel("HDI Score")
    plt.show()

# ==========================
# VISUALIZATION 2
# ==========================
if 'Life_Expectancy' in df.columns and 'HDI' in df.columns:
    plt.figure(figsize=(8, 5))

    sns.stripplot(
        x='Life_Expectancy',
        y='HDI',
        data=df.head(20),
        jitter=True
    )

    plt.title("Life Expectancy vs HDI")
    plt.xlabel("Life Expectancy")
    plt.ylabel("HDI Score")
    plt.show()

# ==========================
# HEATMAP
# ==========================
heatmap_df = df[[
    'HDI',
    'Life_Expectancy',
    'Mean_Years_Schooling',
    'GNI_per_Capita',
    'Internet'
]]

plt.figure(figsize=(8, 6))

sns.heatmap(
    heatmap_df.corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Selected Columns Heatmap')
plt.show()

# ==========================
# MODEL TRAINING
# ==========================
features = [
    'Life_Expectancy',
    'Expected_Years_Schooling',
    'Mean_Years_Schooling',
    'GNI_per_Capita',
    'Human_Inequality',
    'Adult_Literacy',
    'Internet',
    'Electricity',
    'Healthy_LE',
    'Social_Support'
]

X = df[features]
Y = df['HDI']

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

print("\nPredicted HDI values:")
print(y_pred)

r2 = r2_score(Y_test, y_pred)
print("\nR2 Score:", r2)

comparison = pd.DataFrame({
    "Actual HDI": Y_test.values,
    "Predicted HDI": y_pred
})

print("\nComparison:")
print(comparison.head(10))

# ==========================
# SAVE MODEL
# ==========================
with open("hdi_prediction_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")

# ==========================
# LOAD MODEL
# ==========================
with open("hdi_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!")

# ==========================
# FLASK APPLICATION
# ==========================
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Prediction')
def prediction():
    return render_template('indexnew.html')

@app.route('/Home')
def my_home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        input_features = [[
            float(request.form['Life_Expectancy']),
            float(request.form['Expected_Years_Schooling']),
            float(request.form['Mean_Years_Schooling']),
            float(request.form['GNI_per_Capita']),
            float(request.form['Human_Inequality']),
            float(request.form['Adult_Literacy']),
            float(request.form['Internet']),
            float(request.form['Electricity']),
            float(request.form['Healthy_LE']),
            float(request.form['Social_Support'])
        ]]

        input_df = pd.DataFrame(
            input_features,
            columns=features
        )

        prediction = model.predict(input_df)
        hdi = round(float(prediction[0]), 3)

        if hdi < 0.40:
            category = "Low HDI"
        elif hdi < 0.70:
            category = "Medium HDI"
        elif hdi < 0.80:
            category = "High HDI"
        else:
            category = "Very High HDI"

        return render_template(
            "resultnew.html",
            prediction=hdi,
            category=category
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Flask server running...")
    app.run(debug=True, port=5000)