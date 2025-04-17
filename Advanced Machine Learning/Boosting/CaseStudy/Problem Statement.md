# 🍷 Case Study: Wine Quality Prediction

## 🧩 Problem Statement

Wine is a beverage made from fermented grapes or fruit juices, containing a relatively low amount of alcohol. It's the **second most popular alcoholic drink globally** after beer and one of the most consumed beverages.

Traditionally, wine quality is assessed through **taste and vintage**, which is a **time-consuming, expensive**, and subjective process. In reality, wine quality is also influenced by **physiochemical attributes** such as acidity, sugar content, and alcohol levels.

**Moonshine**, a premium red wine company, wants to **improve production efficiency** and **reduce the cost** of expert-driven wine testing. As a **Data Scientist** at Moonshine, your role is to develop a **predictive model** that can help **identify premium-quality wines** based on available data.

---

## 🎯 Objective

The dataset is designed to answer the following questions:

1. What are the different factors that help in identifying **premium, high-quality wine**?
2. Can we build a model to **predict wine quality** reliably?
3. What should be the **evaluation metric** of choice?

---

## 📊 Attribute Information

| Feature                | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| `fixed acidity`        | Sourness and resistance to microbial infection (g/dm³ tartaric acid) |
| `volatile acidity`     | Acetic acid content; high levels produce a vinegar taste (g/dm³)     |
| `citric acid`          | Adds freshness and flavor (g/dm³)                                    |
| `residual sugar`       | Remaining sugar after fermentation (g/dm³)                           |
| `chlorides`            | Salt content (g/dm³)                                                 |
| `free sulfur dioxide`  | Free sulfite content (g/dm³)                                         |
| `total sulfur dioxide` | Total sulfite (free + bound) in g/dm³                                |
| `density`              | Density in g/cm³                                                     |
| `pH`                   | Acidity/basicity on a scale from 0 to 14                             |
| `sulphates`            | Potassium sulfate content (g/dm³)                                    |
| `alcohol`              | Alcohol content in %                                                 |
| `quality`              | Wine quality score (integer from 3 to 8)                             |

---

## 🧠 Learning Outcomes

- Perform **Exploratory Data Analysis (EDA)**
- Prepare the dataset for machine learning
- Train and interpret **ensemble models** (e.g., Random Forest, Gradient Boosting)
- Evaluate classification or regression model performance using appropriate metrics

---

## 🛠️ Steps & Tasks

1. **Import Libraries** and load the dataset
2. Conduct a basic **overview and inspection** of the data
3. Perform **data visualization** to understand distributions and correlations
4. Prepare data:
   - Handle missing values
   - Encode categorical variables (if any)
   - Scale numerical features
5. **Choose a model**, train it, and evaluate performance using metrics such as:
   - **Accuracy**, **F1-score**, **Precision/Recall** (for classification)
   - **R²**, **RMSE**, **MAE** (for regression)
6. Draw insights and present a **conclusion**

---

> 🧪 **Tip:** Wine quality prediction can be treated as either a **classification** (e.g., classify into low, medium, high) or **regression** (predict actual score) problem depending on your goal.
