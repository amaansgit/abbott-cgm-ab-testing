# Statistical Testing Cheat Sheet for A/B Testing

## Overview

After completing Data Validation, Exploratory Data Analysis (EDA), and verifying that the experiment groups are balanced (Baseline Validation), the next step is **Hypothesis Testing**.

The objective of hypothesis testing is to determine whether the observed differences between groups are statistically significant or simply due to random chance.

---

# Step 1: Formulate the Hypothesis

Every statistical test begins with two hypotheses.

## Null Hypothesis (H₀)

The null hypothesis assumes **no difference** or **no relationship** exists.

Example:

> Campaign type has no effect on weekly app engagement.

---

## Alternative Hypothesis (H₁)

The alternative hypothesis assumes that a significant difference or relationship exists.

Example:

> Campaign type influences weekly app engagement.

---

# Step 2: Identify Your Variables

Before selecting a statistical test, identify:

### Independent Variable (Predictor)

The variable being changed or compared.

Examples:

- Campaign Group
- Gender
- Device Type
- Diabetes Type

Usually **categorical**.

---

### Dependent Variable (Outcome)

The variable being measured.

Examples:

- Weekly Sessions
- Revenue
- Scan Count
- Prescription Refill
- Retention

Can be either **continuous** or **categorical**.

---

# Step 3: Choose the Correct Statistical Test

The choice depends on:

1. Type of dependent variable
2. Number of groups being compared
3. Business question

---

# Decision Tree

```
                    What is your outcome?

                  Numerical (Continuous)
                          │
             ┌────────────┴────────────┐
             │                         │
       Compare 2 Groups         Compare 3+ Groups
             │                         │
        Independent t-Test        One-Way ANOVA
                                        │
                                        ▼
                              Significant?
                                        │
                               Yes → Tukey HSD
```

```
                  Categorical (Yes/No)

                         │
                         ▼

               Relationship Between Categories?

                         │

                   Chi-Square Test
```

```
             Predict a Binary Outcome?

             (Yes / No)

                    │

                    ▼

          Logistic Regression
```

---

# 1. Independent t-Test

## When to Use

- Compare **two independent groups**
- Dependent variable is numerical

Examples

- Campaign A vs Campaign B
- Male vs Female Revenue
- Libre 2 vs Libre 3 Sessions

### Example

Question:

Does Campaign B produce higher weekly sessions than Campaign A?

Test:

Independent t-Test

---

# 2. One-Way ANOVA

## When to Use

- Compare **three or more independent groups**
- Dependent variable is numerical

Examples

- Weekly Sessions across Campaign A, B, C and D
- Revenue across four marketing strategies

### Example

Question:

Does campaign strategy affect weekly app sessions?

Test:

One-Way ANOVA

### Why Not Multiple t-Tests?

Running multiple t-tests increases the probability of false positives (Type I Error).

ANOVA compares all groups simultaneously while controlling this error.

---

# 3. Tukey's HSD

## When to Use

Only after ANOVA shows a statistically significant result.

ANOVA answers:

> Is there any difference?

Tukey answers:

> Which groups are different?

Example:

ANOVA says:

Campaigns differ.

Tukey tells us:

- A vs B
- A vs C
- A vs D
- B vs C
- B vs D
- C vs D

---

# 4. Chi-Square Test

## When to Use

Use when **both variables are categorical**.

Examples

Campaign Group

↓

Prescription Refill

Campaign Group

↓

Retention

Gender

↓

Purchase

### Example

Question:

Does campaign type influence prescription refill?

Outcome:

Yes / No

Test:

Chi-Square Test of Independence

---

# 5. Logistic Regression

## When to Use

Use when predicting a **binary outcome**.

Examples

Will the patient refill?

Will the customer churn?

Will the user click?

Dependent Variable

Yes / No

Independent Variables

Can be numerical or categorical.

Example

Predicting prescription refill using:

- Campaign Group
- Weekly Sessions
- Notification Open
- Weekly Scan Count
- Age

---

# Statistical Test Summary

| Business Question | Outcome Type | Groups | Statistical Test |
|------------------|--------------|--------|------------------|
| Compare two average values | Numerical | 2 | Independent t-Test |
| Compare three or more averages | Numerical | 3+ | One-Way ANOVA |
| Identify which groups differ | Numerical | 3+ | Tukey HSD |
| Relationship between two categorical variables | Categorical | Any | Chi-Square Test |
| Predict a Yes/No outcome | Binary | Multiple predictors | Logistic Regression |

---

# Application in This Project

| Hypothesis | Statistical Test |
|------------|------------------|
| Does campaign type affect weekly app engagement? | One-Way ANOVA |
| Which campaign performs significantly better? | Tukey's HSD |
| Does campaign type influence prescription refill rates? | Chi-Square Test |
| Which factors influence prescription refill behavior? | Logistic Regression |

---

# Key Takeaways

- **t-Test** → Compare the means of **2 groups**.
- **ANOVA** → Compare the means of **3 or more groups**.
- **Tukey's HSD** → Identify which specific groups differ after a significant ANOVA.
- **Chi-Square Test** → Determine whether two categorical variables are associated.
- **Logistic Regression** → Predict the probability of a binary outcome using multiple predictors.

Choosing the appropriate statistical test ensures that conclusions are statistically valid, minimizes false discoveries, and enables data-driven business decisions.
