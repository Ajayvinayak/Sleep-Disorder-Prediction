
# Sleep Disorder Prediction

This project is a machine learning-based web application for predicting sleep disorders using patient data. It leverages a **LightGBM classifier** integrated with rule-based logic to provide accurate predictions for three categories: **Normal**, **Insomnia**, and **Sleep Apnea**. 

The web interface is built using **Streamlit**, making it user-friendly and accessible for healthcare professionals and individuals.

---

## Table of Contents

1. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
2. [Model Training and Testing](#model-training-and-testing)
3. [How the Model Works](#how-the-model-works)
4. [Uses of the Project](#uses-of-the-project)
5. [Setup Instructions](#setup-instructions)
6. [Authors](#authors)

---

## Exploratory Data Analysis (EDA)

EDA provided insights into the dataset and identified key correlations:

- **Data Distribution**: Features include `Sleep Duration`, `Stress Level`, `Daily Steps`, and `BMI Category`. 
- **Class Imbalance**: The dataset had more "Normal" cases compared to "Sleep Apnea" and "Insomnia". **SMOTE** was applied to balance the class distribution.
- **Correlations**:
  - Short sleep duration and high stress levels were linked to **Insomnia**.
  - BMI and age correlated with **Sleep Apnea**.
- **Feature Engineering**: Features like systolic and diastolic BP were extracted from the `Blood Pressure` column for improved granularity.

---

## Model Training and Testing

### Model Details:
- **Algorithm**: LightGBM (Gradient Boosting Framework)
- **Tuning**: Hyperparameters (e.g., `num_leaves`, `learning_rate`, `n_estimators`) were optimized using **GridSearchCV**.
- **Data Balancing**: SMOTE ensured fair representation of all classes.

### Accuracy Metrics:
- **Training Accuracy**: **97.22%**
- **Testing Accuracy**: **95%**

These results demonstrate the model's ability to generalize well on unseen data.

---

## How the Model Works

### Steps:
1. **Data Preprocessing**:
   - Categorical features (e.g., `Gender`, `BMI Category`) are label-encoded.
   - Numerical features are normalized and fed into the model.

2. **Rule-Based Overrides**:
   - **Insomnia**: If:
     - Sleep Duration < 5.5 hours
     - Stress Level > 7
     - Quality of Sleep < 4
   - **Normal**: If:
     - Sleep Duration > 6.5 hours
     - Stress Level < 5
     - Quality of Sleep > 5

3. **LightGBM Classifier**:
   - Predicts the sleep disorder based on features such as sleep duration, stress level, BMI category, etc.
   - Handles imbalanced datasets effectively with SMOTE.

4. **User Interface**:
   - A **Streamlit** app takes user inputs via sliders and dropdowns, making it easy for users to interact with the model.

### Workflow:
- The user provides input data via the app.
- The model processes the data and outputs a prediction (e.g., **Normal**, **Sleep Apnea**, **Insomnia**).
- A warning is displayed if the input matches predefined rules for **Insomnia**.

---

## Uses of the Project

### 1. **Healthcare Assistance**
- Assists doctors in identifying sleep disorders early, enabling timely intervention.

### 2. **Personalized Wellness**
- Individuals can use this tool to monitor their sleep health and adopt better sleep habits.

### 3. **Telemedicine Integration**
- Can be integrated into telemedicine platforms for remote diagnosis and consultations.

### 4. **Academic and Research Purposes**
- A showcase of how machine learning can be effectively applied in healthcare.

### 5. **Awareness Campaigns**
- Promotes better sleep hygiene by highlighting correlations between sleep patterns and disorders.

---

## Setup Instructions

### Prerequisites:
1. **Python**: Ensure Python 3.7 or higher is installed.
2. **Libraries**: Install required libraries using the command:
   ```bash
   pip install -r requirements.txt
   ```
   Required libraries include:
   - `streamlit`
   - `lightgbm`
   - `pandas`
   - `joblib`
   - `scikit-learn`
   - `imblearn`

3. **Dataset**:
   - Place the dataset (`Sleepdata.csv`) in the project directory.

### Running the App:
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-repo/sleep-disorder-prediction.git
   cd sleep-disorder-prediction
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open the app in your browser at `http://localhost:8501`.

---

## Authors

- **Ajay Vinayak**: SRMIST, Ramapuram  
- **L Bharath Kumar**: REC  

This project is a collaborative effort showcasing machine learning's potential in healthcare.

---

