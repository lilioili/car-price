# Drug Dose Prediction Using Machine Learning

## Project Overview

The goal of this project is to predict the **prescribed drug dose for patients** using patient-related clinical features and a **Regression** model from the `scikit-learn` library.

The model learns the relationship between patient characteristics and the prescribed dose, then predicts the appropriate dose for new patient data.

## Dataset

The dataset is stored in the following file:

```text
data.xlsx
```

The dataset contains **80,000 records** with the following input features:

| Feature | Description |
|---|---|
| Age | Patient's age |
| Weight | Patient's weight |
| Height | Patient's height |
| Tumor Size | Size of the tumor |
| Completed Sessions | Number of completed treatment sessions |

The target variable is the **prescribed drug dose**.

## Train/Test Split

The dataset was divided into training and testing sets:

| Dataset | Percentage | Number of Samples |
|---|---:|---:|
| Training Data | 80% | 64,000 |
| Test Data | 20% | 16,000 |
| Total | 100% | 80,000 |

## Model

- **Problem Type:** Regression
- **Library:** `scikit-learn`
- **Target:** Prescribed drug dose

## Model Evaluation

The model was evaluated using **MAE**, **MSE**, and **RMSE**.

| Metric | Formula | Result |
|---|---|---:|
| MAE | $MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|$ | 20 |
| MSE | $MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$ | 32 |
| RMSE | $RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2} = \sqrt{MSE}$ | 1.34 |

### Metric Definitions

- **MAE (Mean Absolute Error):** Average absolute difference between the actual and predicted drug doses.
- **MSE (Mean Squared Error):** Average squared difference between the actual and predicted drug doses.
- **RMSE (Root Mean Squared Error):** Square root of MSE and represents the prediction error in the same unit as the target variable.

In the formulas:

- $y_i$ = actual drug dose
- $\hat{y}_i$ = predicted drug dose
- $n$ = number of test samples

## Software Output

The trained model was connected to a software interface for predicting the prescribed drug dose.

![Software Output](a.png)

## Project Files

```text
project/
├── data.xlsx
├── output.png
└── README.md
```

## Technologies Used

- Python
- pandas
- scikit-learn
- Microsoft Excel dataset (`.xlsx`)

