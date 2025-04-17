# 💼 Case Study: Job Change Prediction using Model Tuning

## 🧩 Problem Statement

An **Ed-Tech company** is looking to hire data scientists from a pool of candidates who have successfully completed certain courses and enrolled in training. The company aims to identify candidates who are **actively looking for a job change** after completing the training, which will help reduce the cost and time required to categorize potential candidates.

They have data related to **demographics**, **education**, and **experience** from candidate sign-ups and enrollments, which needs to be analyzed to determine which candidates are more likely to seek a job change.

---

## 🎯 Problem

The dataset aims to answer the following key questions:

1. **What are the factors** affecting whether a person is looking for a job change?
2. **Does imbalance in the dataset** affect the model's predictions?
3. What are the **key business recommendations** based on data analysis and model predictions?

---

## 📊 Attribute Information

| Feature                  | Description                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------- |
| `enrollee_id`            | Unique ID for the candidate                                                         |
| `city`                   | City code                                                                           |
| `city_development_index` | Development index of the city (scaled)                                              |
| `gender`                 | Gender of the candidate                                                             |
| `relevent_experience`    | Relevant experience of the candidate (in years)                                     |
| `enrolled_university`    | Type of university course enrolled in, if any                                       |
| `education_level`        | Education level of the candidate                                                    |
| `major_discipline`       | Education major discipline of the candidate                                         |
| `experience`             | Total experience in years                                                           |
| `company_size`           | Number of employees in the current employer's company                               |
| `company_type`           | Type of current employer                                                            |
| `lastnewjob`             | Difference in years between previous job and current job                            |
| `training_hours`         | Number of training hours completed                                                  |
| `target`                 | **Target variable**: 0 – Not looking for a job change, 1 – Looking for a job change |

---

## 🧠 Learning Outcomes

- **Exploratory Data Analysis (EDA)** to uncover key patterns in the data.
- **K-fold Cross-validation** to assess model performance and robustness.
- Handling **imbalanced data** to avoid bias in predictions.
- Using **regularization techniques** to reduce model overfitting.

---

## 🛠️ Steps and Tasks

1. **Import Libraries** and Load the Dataset.
2. Perform an **Overview of the Data**.
3. Conduct **Data Visualization** to explore the relationships between variables.
4. **Data Preparation**:
   - Handle missing data and outliers.
   - Encode categorical variables and scale numerical data.
5. **Choose a Model**:
   - Experiment with different algorithms (Logistic Regression, Random Forest, etc.).
6. **Balance the Data**:
   - **Over-sample** or **under-sample** the training set to handle class imbalance.
7. Apply **Regularization** (such as L2 regularization) to reduce overfitting.
8. Draw **Business Insights** from the model to assist the hiring process.

---

## 🚀 Key Recommendations

- **Candidate Segmentation**: Use the model's predictions to identify which candidates may be more inclined to seek job changes.
- **Model Performance**: Evaluate the model’s accuracy, precision, recall, and F1-score using cross-validation.
- **Data Strategy**: Consider the imbalance between job seekers and non-seekers while preparing the dataset.

> 📌 **Note:** Ensure to check for model overfitting and adjust hyperparameters for optimal performance.
