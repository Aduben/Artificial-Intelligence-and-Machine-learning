# 💳 Case Study: German Credit Analysis

## 📚 Context

When a bank receives a loan application, it has to decide whether to approve or reject the application based on the applicant’s profile. There are two types of risks associated with this decision:

1. **Good credit risk**: If the applicant is likely to repay the loan, rejecting the loan results in a loss of business to the bank.
2. **Bad credit risk**: If the applicant is unlikely to repay the loan, approving the loan results in a financial loss to the bank.

To minimize these risks, **HRE Bank** wants to automate the loan approval process using a predictive model. The goal is to predict whether a customer is at risk of defaulting on the loan based on their demographic and socio-economic profile.

As a **Data Scientist** at HRE Bank, you have been tasked with building a predictive model to assess the risk of loan default.

---

## 🎯 Problem

The dataset aims to answer the following key questions:

1. **What are the key features** that lead to a person defaulting on a loan?
2. Can we build a model to **predict** whether a customer will default or not?

---

## 📊 Attribute Information

| Feature            | Description                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `Age`              | Age of the applicant (Numeric)                                                                                                           |
| `Sex`              | Gender of the applicant (Categories: male, female)                                                                                       |
| `Job`              | Job type (Categories: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled)                       |
| `Housing`          | Type of housing (Categories: own, rent, or free)                                                                                         |
| `Saving accounts`  | Saving account status (Categories: little, moderate, quite rich, rich)                                                                   |
| `Checking account` | Checking account status (Categories: little, moderate, rich)                                                                             |
| `Credit amount`    | Credit amount in Deutsche Marks (DM)                                                                                                     |
| `Duration`         | Duration for which the credit is given (in months)                                                                                       |
| `Purpose`          | Purpose of the loan (Categories: car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others) |
| `Risk`             | Target variable (0 - Not at risk, 1 - At risk/defaulter)                                                                                 |

---

## 🧠 Learning Outcomes

- **Exploratory Data Analysis (EDA)** to understand the structure and relationships in the data.
- **Pipelines** to streamline data preprocessing and model training.
- **Hyperparameter tuning** to optimize model performance.

---

## 🛠️ Steps and Tasks

1. **Import Libraries** and Load the Dataset.
2. Perform an **Overview of the Data**.
3. Conduct **Data Visualization** to identify key patterns and relationships.
4. **Data Preparation**:
   - Handle missing values, encode categorical variables, and scale numerical features.
5. **Choose a Model**:
   - Select and train classification models (e.g., Logistic Regression, Decision Trees, Random Forest).
6. **Tune the Model**:
   - Use techniques like **Grid Search** or **Randomized Search** for hyperparameter tuning.
7. Draw **Conclusions** from the model and provide actionable business insights.

---

## 🚀 Key Recommendations

- **Risk Assessment**: Use the model to predict which applicants are at risk of default, enabling the bank to make more informed lending decisions.
- **Feature Importance**: Identify which features (e.g., age, credit amount, duration) have the highest impact on default risk.
- **Model Performance**: Evaluate the model's accuracy, precision, recall, and F1-score to ensure it meets the business requirements.

> 📌 **Note**: Model validation, cross-validation, and hyperparameter tuning are crucial steps to improve the model’s predictive power.
