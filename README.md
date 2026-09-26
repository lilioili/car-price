# 🚗 Used Car Price Prediction

## 1. Project Overview
This project implements a **Machine Learning regression model** to predict the price of used cars based on key technical and historical attributes. The model is trained on a structured dataset and evaluated using standard regression metrics to assess its predictive performance.

## 2. Project Goal
The main goal of this project is to build a reliable regression model capable of estimating the **price of a used car** based on features such as engine size, technical condition, manufacturing year, mileage, and accident history.

## 3. Dataset
- **File name:** `data.xlsx`
- **Number of records:** 1001
- **Format:** Excel spreadsheet (`.xlsx`)

## 4. Features
The following features are used as input variables for the model:

| Feature           | Description                              |
|--------------------|-------------------------------------------|
| `Engine_Litr`       | Engine displacement (in liters)           |
| `Technical_Score`   | Overall technical condition score         |
| `Year`              | Manufacturing year of the vehicle         |
| `Mileage_km`        | Total mileage driven (in kilometers)      |
| `Accident_Count`    | Number of recorded accidents              |

**Target variable:** Car price

## 5. Machine Learning Approach
This project uses a **supervised regression approach** to model the relationship between the input features and the target price. The `scikit-learn` library is used for data preprocessing, model training, and evaluation.

## 6. Data Split
The dataset was split into training and testing subsets as follows:

- **Training set:** 75%
- **Testing set:** 25%

## 7. Model Evaluation
The model's performance was evaluated using the **Mean Absolute Error (MAE)** metric:

| Metric | Value |
|--------|-------|
| MAE    | 1082  |
| MAE    | 1340  |

> **Note:** Two MAE values are reported above. It is currently unclear whether the second value (1340) corresponds to a different data split (e.g., test set vs. training set), a different model configuration, or another evaluation metric. This should be reviewed and clarified before final reporting, and the label should be corrected accordingly (e.g., to RMSE, MAE on test set, etc.) if needed.

## 8. Technologies Used
- Python
- scikit-learn
- pandas
- NumPy
- (Optional) Matplotlib / Seaborn for visualization

## 9. Project Structure
```
used-car-price-prediction/
│
├── data/
│   └── data.xlsx
│
├── notebooks/
│   └── model_training.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── README.md
└── requirements.txt
```

## 10. How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/used-car-price-prediction.git
   cd used-car-price-prediction
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the dataset (`data.xlsx`) inside the `data/` folder.
4. Run the training script:
   ```bash
   python src/train_model.py
   ```
5. Evaluate the model:
   ```bash
   python src/evaluate_model.py
   ```

## 11. Project Workflow
1. Load and inspect the dataset (`data.xlsx`).
2. Perform data cleaning and preprocessing.
3. Split the data into training (75%) and testing (25%) sets.
4. Train a regression model using `scikit-learn`.
5. Evaluate model performance using MAE.
6. Analyze results and identify areas for improvement.

## 12. Conclusion
The model demonstrates the ability to predict used car prices with a reasonable degree of accuracy, based on the reported MAE score(s). Further validation is recommended to confirm the reliability of the second evaluation metric mentioned above.

## 13. Future Improvements
- Collect a larger and more diverse dataset.
- Perform feature engineering (e.g., brand, fuel type, transmission).
- Experiment with advanced models (Random Forest, XGBoost, Gradient Boosting).
- Apply hyperparameter tuning (GridSearchCV / RandomizedSearchCV).
- Add cross-validation for more robust performance estimation.
- Deploy the model as a web application or API for real-world use.
