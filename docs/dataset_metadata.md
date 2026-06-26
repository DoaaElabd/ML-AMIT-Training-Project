# Dataset Metadata

## Dataset Information

- **Dataset Name:** Credit Approval Dataset
- **Source:** UCI Machine Learning Repository
- **Purpose:** Predict whether a customer's credit card application will be approved.

**Target Variable**

| Column | Description |
|--------|-------------|
| Class | Target variable. <br> **1** = Credit card application approved. <br> **0** = Credit card application rejected. |

---

## Feature Descriptions

| Column | Description | Data Type | Keep? | Notes |
|--------|-------------|-----------|-------|------|
| CustomerID | Unique customer identifier | Integer | ❌ No | Identifier only; removed before training. |
| A1 | Gender / Marital Status | Categorical (encoded) | ✅ Yes | Already numerically encoded. |
| A2 | Age | Numerical | ✅ Yes | Customer age. |
| A3 | Income / Debt | Numerical | ✅ Yes | Financial information. |
| A4 | Housing / Account Type | Categorical (encoded) | ✅ Yes | Already encoded. |
| A5 | Banking Status | Categorical (encoded) | ✅ Yes | Already encoded. |
| A6 | Occupation | Categorical (encoded) | ✅ Yes | Already encoded. |
| A7 | Nationality / Region | Categorical (encoded) | ✅ Yes | Already encoded. |
| A8 | Years Employed | Numerical | ✅ Yes | Employment duration. |
| A9 | Previous Credit History | Binary | ✅ Yes | 1 = Yes, 0 = No. |
| A10 | Employment Status | Binary | ✅ Yes | 1 = Employed, 0 = Not employed. |
| A11 | Credit Score | Numerical | ✅ Yes | Creditworthiness indicator. |
| A12 | Identity Verification | Binary | ✅ Yes | Example: driver's license or phone verification. |
| A13 | Account Type / Preferred Payment Method | Categorical (encoded) | ✅ Yes | Already encoded. |
| A14 | ZIP Code or Financial Value* | Numerical | ⚠️ Review | Verify whether this represents a location code or a financial value. |
| Class | Credit Approval | Binary | Target | Prediction target. |

---

## Data Quality Assessment

The dataset was inspected before model development.

### Findings

- Number of samples: **690**
- Number of features: **15** (excluding the target)
- Missing values: **None**
- Duplicate rows: **None**
- Data types: Numeric (`int64` and `float64`)
- Target distribution:
  - Class 0 (Rejected): **383**
  - Class 1 (Approved): **307**

The dataset is considered clean and suitable for machine learning.

---

## Preprocessing Decisions

- Remove `CustomerID` before training.
- Keep `Class` as the target variable.
- Keep all remaining features unless further analysis indicates otherwise.
- If `A14` is confirmed to be a ZIP code, consider removing it since identifiers generally do not improve model performance.

---

## Notes

The dataset is an anonymized version of the original Credit Approval Dataset from the UCI Machine Learning Repository. Original feature names and many categorical values were intentionally replaced with generic labels (`A1`–`A14`) to protect privacy.