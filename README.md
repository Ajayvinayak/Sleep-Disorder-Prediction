Sleep Disorder Prediction
This project utilizes machine learning to predict sleep disorders such as insomnia or sleep apnea based on user inputs such as gender, age, occupation, sleep duration, quality of sleep, physical activity, and stress levels. The model is designed to assist in identifying potential sleep health issues.

Table of Contents
Project Overview
Dataset
Model
Installation
Usage
Results
Contributing
License
Project Overview
This project predicts potential sleep disorders by analyzing factors like age, sleep duration, quality of sleep, and more. The trained LightGBM model achieves an accuracy of 90.67%. It can be used to assist healthcare professionals and individuals in identifying sleep disorders and improving sleep health.

Dataset
The dataset used includes the following features:

Gender
Age
Occupation
Sleep Duration
Quality of Sleep
Physical Activity Level
Stress Level
BMI Category
Blood Pressure (Systolic/Diastolic)
Heart Rate
Daily Steps
The target variable is Sleep Disorder, which includes labels such as 'Insomnia', 'Sleep Apnea', and 'None'.

Model
A LightGBM classifier was used for predicting sleep disorders, with the following configuration:

n_estimators: 500
learning_rate: 0.05
max_depth: 10
Cross-validation and hyperparameter tuning were applied to improve performance, resulting in an accuracy of 90.67%.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Ajayvinayak/sleep-disorder-prediction.git
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure you have the dataset file Sleepdata.csv in the project directory.

Usage
To train the model:

python
Copy code
python train_model.py
To predict sleep disorders for a new user: Use the prediction function by providing the necessary input values:

python
Copy code
result = predict_sleep_disorder(Gender='Male', Age=25, Occupation='Software Engineer', 
                                Sleep_Duration=7, Quality_of_Sleep=6, Physical_Activity_Level=40, 
                                Stress_Level=5, BMI_Category='Normal', 
                                Systolic=120, Diastolic=80, Heart_Rate=75, Daily_Steps=8000)
print(f"Predicted Sleep Disorder: {result}")
Results
The model achieves an accuracy of 90.67%. Cross-validation results indicate strong generalization performance, making it suitable for predictive applications in sleep health.

Contributing
Feel free to submit issues or pull requests. Contributions are welcome to improve the model performance or expand functionality.

License
This project is licensed under the MIT License.



