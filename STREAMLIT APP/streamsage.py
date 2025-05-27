
import streamlit as st
import pandas as pd
import numpy as np
import catboost

# ------------------------
# Set Page Config FIRST
# ------------------------
st.set_page_config(
    page_title="IT'S PREDICTION TIME!",
    page_icon="🌙",
    layout="wide"
)

st.markdown("""
    <style>
    /* ----- Base Styling ----- */
    .stApp, .block-container {
        background-color: #121212;
        color: #e0e0e0;
    }

    /* ----- Headings & Text ----- */
    h1, h2, h3, h4, h5, h6, .stMarkdown, .css-10trblm, .css-1v0mbdj {
        color: #ffffff;
    }

    /* ----- Colored Notes & CSV Section Fix ----- */
    .stAlert, .css-1cpxqw2 {
        background-color: #1f1f2e;
        border-left: 5px solid #ffaa00;
        color: #f5f5f5;
    }

    .stMarkdown div[style*="background-color: rgb(38, 39, 48)"] {
        background-color: #1e1e2f !important;
        color: #e0e0e0 !important;
    }

    /* Make file uploader match theme */
    .stFileUploader, .stFileUploader > div {
        background-color: #1e1e2f;
        color: #f5f5f5;
    }

    /* ----- Button Styling ----- */
    .stButton > button {
        background-color: #2a2a3f;
        color: white;
        border: 1px solid #444466;
        border-radius: 8px;
    }

    .stButton > button:hover {
        background-color: #444466;
        color: white;
    }
     /* ----- Sidebar ----- */
    [data-testid="stSidebar"] {
        background-color: #1e1e2f;
        color: #e0e0e0;
    
    }

    [data-testid="stSidebar"] .css-1d391kg {
        color: #e0e0e0 !important;
    }

    /* ----- Tabs and Navigation Buttons ----- */
    .element-container button {
        background-color: #2b2b3c;
        color: #ffffff;
    }

    .element-container button:hover {
        background-color: #444466;
    }

    /* ----- Improve Table and Upload Display ----- */
    .stDataFrame, .stTable, .css-1n76uvr {
        background-color: #1a1a2f;
        color: #ffffff;
    }

    /* ----- Fix for "Home" White Background ----- */
    .css-1dp5vir {
        background-color: #121212 !important;
    }

    </style>
""", unsafe_allow_html=True)

# ------------------------
# 🎓 Load Trained Model
# ------------------------
model = catboost.CatBoostClassifier()
model.load_model('catboost_churn_model_final.cbm')

# ------------------------
# Header
# ------------------------
st.markdown("<h1 style='text-align: center;'>🔮 STREAMSAGE — <em>A Practical Solution for Churn Prediction</em></h1>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------
# Navigation State
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = "HOME"

# ------------------------
# Toolbar Navigation
# ------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 HOME", key="home", help="Go to homepage", use_container_width=True):
        st.session_state.page = "HOME"
with col2:
    if st.button("❓ WHY YOU ARE HERE?", key="why", use_container_width=True):
        st.session_state.page = "WHY YOU ARE HERE?"
with col3:
    if st.button("🧠 ABOUT MODEL DESIGN", key="about", use_container_width=True):
        st.session_state.page = "ABOUT MODEL DESIGN"
with col4:
    if st.button("🔮 CHURN PREDICTION", key="predict", use_container_width=True):
        st.session_state.page = "CHURN PREDICTION"

st.markdown("---")

# ------------------------
# 📚 Sidebar
# ------------------------
with st.sidebar:
    st.header("ℹ️ Model Info")
    with st.expander("See details"):
        st.write("""
        - **Model: CatBoostClassifier**
        - **Preprocessing: SMOTE, Label Encoding**
        - **Threshold: 0.3**
        - **Metrics: Accuracy, Precision, Recall, F1, ROC-AUC**
        """)
    st.header("🎯 Why CatBoost?")
    with st.expander("Read More"):
        st.write("""
        - **CatBoost is best for small datasets with categorical data.**
        - **Built-in handling of categorical features, less tuning.**
        - **Ordered boosting = better generalization with fewer samples.**
        """)
    st.caption("Built for Academic Project 📚")

# ------------------------
# 🏠 Home Page
# ------------------------
if st.session_state.page == "HOME":
    st.subheader("ALL YOU NEED TO KNOW ABOUT STREAMSAGE!")
    st.markdown("""
    This app helps **small-to-mid-sized streaming platforms** predict customer churn using Machine Learning.

    ### 🌟 Built for the Underdogs
    **STREAMSAGE** empowers platforms where every subscriber matters.

    ### ⚡ No Data Scientist? No Problem!
    Just **upload your CSV**, and get churn predictions. CatBoost handles the hard part.

    ### 🔍 Custom Threshold & Smart Strategy
    - Predict using threshold of `0.3`
    - Auto-suggest retention actions based on churn risk.

    🎁 **Now includes retention recommendation engine!**
    """)

# ------------------------
# ❓ Problem Statement Page
# ------------------------
if st.session_state.page == "WHY YOU ARE HERE?":
    st.subheader("❓ PROBLEM STATEMENT")
    st.markdown("""
    - Customer churn drains profits.
    - Most streaming startups can't afford big ML teams.
    
    ### ✔️ OUR SOLUTION
    - Churn prediction tailored for smaller datasets (~2500 users).
    - Works out of the box — **high recall, balanced precision**.
    - Uses **CatBoost**, ideal for categorical features.
    """)

# ------------------------
# 🧠 Model Design Page
# ------------------------
if st.session_state.page == "ABOUT MODEL DESIGN":
    st.subheader("📊 MODEL PERFORMANCE")
    st.markdown("""
    - **Accuracy:** ~85%
    - **Precision:** ~46%
    - **Recall:** ~77%
    - **F1 Score:** ~58%
    - **ROC-AUC:** ~82%
    """)
    st.subheader("Why This Model?")
    st.markdown("""
    - Designed for low-sample data
    - Zero preprocessing needed
    - Smartly handles categorical values
    - Fast prediction + interpretable
    """)

# ------------------------
# 🔮 Prediction Page
# ------------------------
if st.session_state.page == "CHURN PREDICTION":
    st.title("IT'S PREDICTION TIME!")
    st.write("Upload a CSV file containing customer details to predict churn risk.")

st.markdown("""
<div style='background-color:#1e1e2f; padding: 10px; border-left: 4px solid #ffaa00; color: #f5f5f5;'>
    <strong>📢 Required CSV Columns:</strong><br>
    <ul style='margin: 0; padding-left: 20px;'>
        <li>gender</li>
        <li>age</li>
        <li>no_of_days_subscribed</li>
        <li>weekly_mins_watched</li>
        <li>minimum_daily_mins</li>
        <li>maximum_daily_mins</li>
        <li>weekly_max_night_mins</li>
        <li>videos_watched</li>
        <li>maximum_days_inactive</li>
        <li>customer_support_calls</li>
    </ul>
    <strong>Note:</strong> MAKE SURE THE COLUMNS BELOW ARE UPLOADED WITH EMPTY ROWS BEFORE UPLOADING YOUR <strong>CSV FILE</strong>. 
    THESE COLUMNS ARE EXTRACTED DURING A FEATURE ENGINEERING STEP BEFORE TRAINING THE MODEL TO IMPROVE MODEL PERFORMANCE.
    <ul style='margin: 0; padding-left: 20px;'>
        <li>multi_screen_score</li>
        <li>email_marketing_score</li>
        <li>subscription_tenure</li>
        <li>engagement_score</li>
        <li>consistency_score</li>
        <li>night_owl_score</li>
        <li>churn_risk_score</li>
    </ul>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style='color: green; font-weight: bold;'>
    Upload your input CSV file
</div>
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📢", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        # ----------------- Preview Uploaded Data -----------------
        st.subheader("📄 Data Preview")
        st.dataframe(data.head())

        # ----------------- Basic Preprocessing -----------------
        data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})
        data['multi_screen'] = data['multi_screen'].map({'No': 0, 'Yes': 1})
        data['mail_subscribed'] = data['mail_subscribed'].map({'No': 0, 'Yes': 1})
        data = data.drop(columns=[col for col in ['year', 'customer_id'] if col in data.columns])

        # ----------------- Feature Engineering with Fill Logic -----------------

        # Subscription Tenure (Scaled 0-1)
        sub_tenure = data['no_of_days_subscribed'] / data['no_of_days_subscribed'].max()
        if 'subscription_tenure' in data.columns:
            data['subscription_tenure'].fillna(sub_tenure, inplace=True)
        else:
            data['subscription_tenure'] = sub_tenure

        # Engagement Score (Scaled 0-1)
        eng_score = (data['weekly_mins_watched'] - data['weekly_mins_watched'].min()) / (
            data['weekly_mins_watched'].max() - data['weekly_mins_watched'].min())
        if 'engagement_score' in data.columns:
            data['engagement_score'].fillna(eng_score, inplace=True)
        else:
            data['engagement_score'] = eng_score

        # Consistency Score
        consistency = 1 - (data['maximum_daily_mins'] - data['minimum_daily_mins']) / data['maximum_daily_mins']
        if 'consistency_score' in data.columns:
            data['consistency_score'].fillna(consistency, inplace=True)
        else:
            data['consistency_score'] = consistency

        # Night Owl Score
        night_owl = data['weekly_max_night_mins'] / data['weekly_mins_watched']
        if 'night_owl_score' in data.columns:
            data['night_owl_score'].fillna(night_owl, inplace=True)
        else:
            data['night_owl_score'] = night_owl

        # Churn Risk Score
        weight_1, weight_2 = 0.5, 0.5
        churn_risk = data['customer_support_calls'] * weight_1 + (1 - eng_score) * weight_2
        if 'churn_risk_score' in data.columns:
            data['churn_risk_score'].fillna(churn_risk, inplace=True)
        else:
            data['churn_risk_score'] = churn_risk

        # Multi-Screen Score
        if 'multi_screen_score' in data.columns:
            data['multi_screen_score'].fillna(data['multi_screen'], inplace=True)
        else:
            data['multi_screen_score'] = data['multi_screen']

        # Email Marketing Score
        if 'email_marketing_score' in data.columns:
            data['email_marketing_score'].fillna(data['mail_subscribed'], inplace=True)
        else:
            data['email_marketing_score'] = data['mail_subscribed']

        st.success("✅ Missing feature values filled successfully.")

        # ----------------- Optional: Preview Updated Data -----------------
        st.subheader("📊 Updated Data After Feature Engineering")
        st.dataframe(data.head())


        if st.button("🔮 Predict Churn"):
                probs = model.predict_proba(data)[:, 1]
                preds = (probs >= 0.3).astype(int)
                data['Churn Probability'] = probs
                data['Churn Prediction (0=No, 1=Yes)'] = preds

                def recommend_strategy(row):
                    if row['churn_risk_score'] > 0.6:
                        return "💸 Offer discount coupon + track next week usage."
                    elif row['maximum_days_inactive'] > 7:
                        return "🎁 Offer discount to re-engage."
                    elif row['engagement_score'] < 0.4:
                        return "📩 Recommend content based on watch history."
                    elif row['consistency_score'] < 0.5:
                        return "🔁 Trigger weekly engagement reminders."
                    elif row['customer_support_calls'] > 3:
                        return "📞 Assign to senior support staff."
                    elif row['email_marketing_score'] == 1:
                        return "💌 Improve personalized email marketing."
                    else:
                        return "✔️ Low Risk – Keep Engaged."

                data['Retention Recommendation'] = data.apply(recommend_strategy, axis=1)

                st.success("✔️ Prediction Done")
                st.subheader("📊 Results")
                st.dataframe(data)

                st.download_button(
                    label="📥 Download CSV",
                    data=data.to_csv(index=False).encode('utf-8'),
                    file_name='churn_predictions.csv',
                    mime='text/csv'
                )
    except Exception as e:
            st.error(f"❌ Error processing file: {e}")

# ------------------------
# 📌 Footer
# ------------------------
st.markdown("---")
st.caption("© 2025 Streaming Churn Project | Built for Academic Use 📚")
