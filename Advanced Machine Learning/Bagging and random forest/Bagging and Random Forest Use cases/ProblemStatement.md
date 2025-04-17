# 🧑‍💼 Case Study: HR Attrition using Ensemble Techniques

## 🧩 Problem Statement

McCurr Consultancy, a global MNC, employs thousands of individuals across the world. The company places a strong emphasis on **hiring top talent** and **retaining them** for as long as possible. Substantial resources are spent on retention efforts such as incentives and employee programs.

The Head of People Operations is seeking to **reduce costs** by **targeting retention efforts only at employees at risk of attrition**. As a newly hired **Data Scientist** in the People Operations Department, your role is to:

- Analyze patterns in the characteristics of employees who leave.
- Build a predictive model to identify employees at risk of attrition.
- Help optimize resource allocation for retention programs.

---

## ❓ Problem Goals

The dataset provided aims to answer the following questions:

1. **What are the key factors** that help in identifying employees likely to attrite?
2. **Can we build a model** to predict attrition effectively?
3. **Which evaluation metrics** are best suited to assess this classification problem?

---

## 📊 Attribute Information

| Feature                    | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| `EmployeeNumber`           | Employee Identifier                                       |
| `Attrition`                | Target variable: Yes/No                                   |
| `Age`                      | Age of the employee                                       |
| `BusinessTravel`           | Travel frequency (e.g., Travel_Rarely, Travel_Frequently) |
| `DailyRate`                | Daily rate (data description not provided)                |
| `Department`               | Department name                                           |
| `DistanceFromHome`         | Distance from home to work (in km)                        |
| `Education`                | Education Level (1-Below College to 5-Doctor)             |
| `EducationField`           | Field of education                                        |
| `EmployeeCount`            | Count of employee records                                 |
| `EnvironmentSatisfaction`  | Satisfaction level (1-Low to 4-Very High)                 |
| `Gender`                   | Male/Female                                               |
| `HourlyRate`               | Hourly rate (data description not provided)               |
| `JobInvolvement`           | Job involvement (1-Low to 4-Very High)                    |
| `JobLevel`                 | Level of job (1 to 5)                                     |
| `JobRole`                  | Role/position of the employee                             |
| `JobSatisfaction`          | Satisfaction level (1-Low to 4-Very High)                 |
| `MaritalStatus`            | Marital status                                            |
| `MonthlyIncome`            | Monthly salary                                            |
| `MonthlyRate`              | Monthly rate (data description not provided)              |
| `NumCompaniesWorked`       | Number of previous companies worked at                    |
| `Over18`                   | Is the employee over 18 years of age?                     |
| `OverTime`                 | Does the employee work overtime?                          |
| `PercentSalaryHike`        | Percent salary hike from last year                        |
| `PerformanceRating`        | Performance rating (1-Low to 4-Outstanding)               |
| `RelationshipSatisfaction` | Satisfaction level (1-Low to 4-Very High)                 |
| `StandardHours`            | Standard working hours                                    |
| `StockOptionLevel`         | Stock options given (level 0 to 3)                        |
| `TotalWorkingYears`        | Total years of work experience                            |
| `TrainingTimesLastYear`    | Number of trainings attended in the last year             |
| `WorkLifeBalance`          | Balance level (1-Low to 4-Outstanding)                    |
| `YearsAtCompany`           | Total years at the company                                |
| `YearsInCurrentRole`       | Years in current role                                     |
| `YearsSinceLastPromotion`  | Years since last promotion                                |
| `YearsWithCurrManager`     | Years with current manager                                |

---

## 🎯 Learning Outcomes

By completing this case study, you will:

- Perform **Exploratory Data Analysis** (EDA)
- **Prepare data** for modeling
- Train and understand data using **ensemble models** (e.g., Random Forest, Bagging)
- Learn how to **evaluate classification models**

---

## 🛠️ Steps & Tasks

1. **Import Libraries** and load the dataset
2. Get an **overview of the data**
3. Perform **data visualization** to uncover patterns
4. Prepare the data (cleaning, encoding, scaling)
5. **Choose a model**, train it, and evaluate results
6. **Document insights** and draw conclusions

---

> 📌 **Note:** Attrition is a **classification problem**. Choose appropriate metrics such as accuracy, precision, recall, and F1-score — especially important due to class imbalance.
