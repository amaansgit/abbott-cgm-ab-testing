# abbott-cgm-ab-testing
End-to-end A/B testing and statistical analysis case study for Abbott's FreeStyle Libre CGM app, leveraging ANOVA, Tukey's HSD, Chi-Square, and Logistic Regression to optimize patient engagement and prescription refill outcomes using a synthetic dataset.

# 📊 Optimizing Patient Engagement & Prescription Refill Using A/B Testing

## End-to-End Statistical Analysis Case Study Inspired by Abbott's FreeStyle Libre CGM Platform

This project demonstrates an end-to-end A/B testing workflow to evaluate the effectiveness of multiple patient engagement campaigns for a Continuous Glucose Monitoring (CGM) mobile application inspired by Abbott's FreeStyle Libre ecosystem.

The objective was to identify which engagement strategy maximizes patient interaction with the mobile application while improving prescription refill rates through statistical hypothesis testing and business analytics.

> **Disclaimer**
>
> This project uses a **synthetically generated dataset** created entirely in Python for educational and portfolio purposes. It does **not** contain any proprietary, confidential, or patient-level data from Abbott or any healthcare organization.

---

# 🚀 Project Objectives

This project aims to answer the following business questions:

- Which campaign generates the highest patient engagement?
- Does campaign strategy influence prescription refill behavior?
- Which engagement strategy should the business deploy to maximize long-term patient adherence?
- Can statistical analysis support business decisions instead of relying on intuition?

---

# 🏥 Business Scenario

A healthcare organization launched four engagement campaigns inside its CGM mobile application.

Patients were randomly assigned to one of four campaigns.

| Campaign | Strategy |
|----------|----------------------------|
| A | Generic Reminder (Control) |
| B | Personalized Health Insights |
| C | Gamification |
| D | Doctor Recommendation |

The analytics team wanted to determine which campaign performed best across multiple patient engagement metrics.

---

# 📁 Repository Structure

```
abbott-cgm-ab-testing/

│

├── Data Generation.py
├── abbott_cgm_ab_testing_dataset.csv
├── AB Testing.py

├── README.md
```

---

# 📈 Dataset

Since real healthcare data cannot be publicly shared, a synthetic dataset was created using Python.

The dataset contains **100,000 simulated patients** with realistic demographic and behavioral characteristics.

## Variables Included

| Variable | Description |
|----------|-------------|
| patient_id | Unique Patient ID |
| age | Patient Age |
| gender | Male / Female |
| diabetes_type | Type 1 / Type 2 |
| state | US State |
| device | Libre 2 / Libre 3 |
| days_since_signup | Days since patient registered |
| campaign_group | A / B / C / D |
| notification_open | Whether patient opened notification |
| weekly_sessions | Weekly app sessions |
| weekly_scan_count | Weekly glucose scans |
| avg_session_time | Average app usage duration |
| retained_30_days | Patient retained after 30 days |
| prescription_refill | Prescription renewed |
| revenue | Revenue generated |

Dataset Size

- 100,000 Patients
- 15 Variables

---

# ⚙️ How the Dataset Was Created

The entire dataset was generated programmatically using **Python**, **NumPy**, and **Pandas** to simulate a realistic healthcare analytics environment.

Rather than randomly generating unrelated values, the dataset was designed to mimic real-world patient behavior by introducing logical relationships between engagement metrics and business outcomes.

The generation process included the following steps:

### Step 1 — Patient Demographics

Random patient profiles were generated including:

- Age
- Gender
- Diabetes Type
- State
- Device Type
- Registration Duration

These variables represent baseline patient characteristics.

---

### Step 2 — Random Campaign Assignment

Patients were randomly assigned into four independent campaign groups:

- Campaign A
- Campaign B
- Campaign C
- Campaign D

Each campaign represented a different patient engagement strategy.

Approximately **25,000 patients** were assigned to each campaign to simulate a randomized A/B test.

---

### Step 3 — Campaign Behaviour

Each campaign was assigned different engagement probabilities.

For example,

Personalized notifications produced higher notification open rates.

Gamification encouraged more weekly sessions and scan counts.

Doctor recommendations generated stronger prescription refill behavior.

---

### Step 4 — Generate Patient Behaviour

Using probability distributions,

the following variables were generated:

- Notification Opens
- Weekly Sessions
- Weekly Scan Count
- Session Duration
- Retention
- Prescription Refill
- Revenue

Each downstream variable was influenced by previous patient behaviour, creating realistic relationships between engagement and business outcomes.

---

### Step 5 — Export Dataset

The final dataset containing **100,000 observations** and **15 variables** was exported as a CSV file using Pandas.

---

# 🧹 Data Validation

Before performing statistical analysis, several quality checks were conducted.

- Verified dataset dimensions
- Checked missing values
- Checked duplicate records
- Validated data types
- Examined summary statistics
- Verified categorical values
- Validated binary variables

---

# 📊 Exploratory Data Analysis

EDA was performed to understand the overall patient population.

Analysis included:

- Campaign Distribution
- Age Distribution
- Gender Distribution
- Diabetes Type Distribution
- Device Distribution
- State Distribution
- Weekly Session Distribution
- Weekly Scan Count Distribution
- Revenue Distribution
- Correlation Analysis

---

# 📐 Statistical Analysis

## Hypothesis 1

### Business Question

Does campaign strategy influence weekly patient engagement?

### Statistical Test

- One-Way ANOVA
- Tukey's HSD Post-Hoc Test

### Result

Campaign C (Gamification) generated the highest weekly app engagement and significantly outperformed all other campaigns.

---

## Hypothesis 2

### Business Question

Does campaign strategy influence prescription refill rates?

### Statistical Test

Chi-Square Test of Independence

### Result

Campaign D (Doctor Recommendation) achieved the highest prescription refill rate, indicating that clinically relevant messaging has a strong influence on patient adherence.

---

## Hypothesis 3

### Business Question

Which engagement factors influence prescription refill behavior?

### Statistical Method

Logistic Regression

### Result

Patient engagement metrics such as weekly sessions, notification interaction, and campaign strategy were identified as key drivers of prescription refill behavior.

---

# 💡 Business Recommendations

Based on the statistical analysis:

- Deploy Gamification campaigns to maximize patient engagement.
- Use Doctor Recommendation campaigns to improve prescription refill rates.
- Replace generic reminders with personalized engagement strategies.
- Combine personalized messaging with clinically relevant recommendations to maximize both engagement and long-term adherence.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Statsmodels
- Jupyter Notebook

---

# 📌 Key Statistical Techniques

- Exploratory Data Analysis (EDA)
- One-Way ANOVA
- Tukey's Honestly Significant Difference (HSD)
- Chi-Square Test of Independence
- Logistic Regression
- Hypothesis Testing

---

# 📚 Key Learnings

Through this project I gained practical experience in:

- Designing synthetic datasets
- Building statistically valid A/B testing experiments
- Performing hypothesis testing
- Translating statistical findings into business recommendations
- Presenting analytical insights for healthcare business stakeholders

---

# 👤 Author

**Amaan Alam**

Senior Data Analyst

NSUT Graduate | Data Analytics | Python | SQL | Power BI | Statistics
