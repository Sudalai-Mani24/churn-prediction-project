🔮 STREAMSAGE — Churn Prediction for Streaming Platforms
📌 Overview

STREAMSAGE is a machine learning-powered web application that predicts customer churn for small-to-mid-sized streaming platforms. Built using Streamlit and CatBoost, it allows users to upload customer data and instantly receive churn predictions along with personalized retention strategies.

🎯 Objective

Predict customers likely to churn

Support data-driven retention strategies

Provide a simple interface for non-technical users

⚙️ Tech Stack

Frontend: Streamlit

Backend: Python

ML Model: CatBoostClassifier

Libraries: pandas, numpy, scikit-learn, imbalanced-learn

🚀 Key Features

📂 Upload CSV file for prediction

🧠 Automatic feature engineering (fills missing engineered features)

🔍 Churn prediction using optimized threshold (0.3)

💡 Personalized retention recommendations

📊 Interactive data preview

📥 Download predictions as CSV

🎨 Clean dark-themed UI

📊 Model Performance

Accuracy: ~85%

Precision: ~46%

Recall: ~77%

F1 Score: ~58%

ROC-AUC: ~82%

Threshold = 0.3 chosen to prioritize high recall and minimize missed churners.

📁 Required Input Columns
gender
age
no_of_days_subscribed
weekly_mins_watched
minimum_daily_mins
maximum_daily_mins
weekly_max_night_mins
videos_watched
maximum_days_inactive
customer_support_calls
multi_screen
mail_subscribed

⚠️ Engineered features will be automatically calculated if missing or empty.

🧠 Feature Engineering

The following features are dynamically generated:

subscription_tenure → normalized subscription duration

engagement_score → user activity level (Min-Max scaling)

consistency_score → usage consistency

night_owl_score → late-night viewing behavior

churn_risk_score → combines support calls & low engagement

multi_screen_score → multi-device usage

email_marketing_score → email subscription indicator

🤖 Model Details

Algorithm: CatBoostClassifier

Handles categorical features efficiently

Performs well on small datasets (~2500 records)

Threshold tuning used for business-driven optimization

🔄 Workflow

Upload CSV file

Data preprocessing & encoding

Feature engineering (auto-fill missing values)

Churn probability prediction

Apply threshold (0.3)

Generate retention recommendations

Display & download results

💡 Business Impact

Helps identify high-risk customers early

Enables targeted retention strategies

Useful for startups without data science teams

⚠️ Limitations

Trained on small dataset

Rule-based recommendations

Not deployed on cloud (local Streamlit app)

🔮 Future Scope

Integrate real-time streaming data

Deploy as cloud API

Improve recommendation engine using AI

Add advanced models (BERT / deep learning)

▶️ How to Run
pip install -r requirements.txt
streamlit run app.py
📌 Project Type

Machine Learning + Data Analytics

Intermediate-level Python project

Academic + Portfolio Project🔮 STREAMSAGE — Churn Prediction for Streaming Platforms
📌 Overview

STREAMSAGE is a machine learning-powered web application that predicts customer churn for small-to-mid-sized streaming platforms. Built using Streamlit and CatBoost, it allows users to upload customer data and instantly receive churn predictions along with personalized retention strategies.

🎯 Objective

Predict customers likely to churn

Support data-driven retention strategies

Provide a simple interface for non-technical users

⚙️ Tech Stack

Frontend: Streamlit

Backend: Python

ML Model: CatBoostClassifier

Libraries: pandas, numpy, scikit-learn, imbalanced-learn

🚀 Key Features

📂 Upload CSV file for prediction

🧠 Automatic feature engineering (fills missing engineered features)

🔍 Churn prediction using optimized threshold (0.3)

💡 Personalized retention recommendations

📊 Interactive data preview

📥 Download predictions as CSV

🎨 Clean dark-themed UI

📊 Model Performance

Accuracy: ~85%

Precision: ~46%

Recall: ~77%

F1 Score: ~58%

ROC-AUC: ~82%

Threshold = 0.3 chosen to prioritize high recall and minimize missed churners.

📁 Required Input Columns
gender
age
no_of_days_subscribed
weekly_mins_watched
minimum_daily_mins
maximum_daily_mins
weekly_max_night_mins
videos_watched
maximum_days_inactive
customer_support_calls
multi_screen
mail_subscribed

⚠️ Engineered features will be automatically calculated if missing or empty.

🧠 Feature Engineering

The following features are dynamically generated:

subscription_tenure → normalized subscription duration

engagement_score → user activity level (Min-Max scaling)

consistency_score → usage consistency

night_owl_score → late-night viewing behavior

churn_risk_score → combines support calls & low engagement

multi_screen_score → multi-device usage

email_marketing_score → email subscription indicator

🤖 Model Details

Algorithm: CatBoostClassifier

Handles categorical features efficiently

Performs well on small datasets (~2500 records)

Threshold tuning used for business-driven optimization

🔄 Workflow

Upload CSV file

Data preprocessing & encoding

Feature engineering (auto-fill missing values)

Churn probability prediction

Apply threshold (0.3)

Generate retention recommendations

Display & download results

💡 Business Impact

Helps identify high-risk customers early

Enables targeted retention strategies

Useful for startups without data science teams

⚠️ Limitations

Trained on small dataset

Rule-based recommendations

Not deployed on cloud (local Streamlit app)

🔮 Future Scope

Integrate real-time streaming data

Deploy as cloud API

Improve recommendation engine using AI

Add advanced models (BERT / deep learning)

▶️ How to Run
pip install -r requirements.txt
streamlit run app.py
📌 Project Type

Machine Learning + Data Analytics

Intermediate-level Python project

Academic + Portfolio Project
