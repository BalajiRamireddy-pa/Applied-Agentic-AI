# integration testing + functional testing

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import numpy as np


def pipeline(X_train, y_train, X_test):
    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    return model, scaler


# Integration + functional test
def test_pipeline():
    # Sample training data
    X_train = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])

    # 4 labels for 4 training samples
    y_train = np.array([0, 1, 0, 1])

    # Sample test data
    X_test = np.array([
        [25, 2500],
        [30, 3500]
    ])

    # Run the pipeline
    model, scaler = pipeline(X_train, y_train, X_test)

    # Make predictions
    pred = model.predict(scaler.transform(X_test))

    # Check that predictions were generated
    assert len(pred) == len(X_test), "Number of predictions does not match test data"

    # Check if the model is fitted
    assert hasattr(model, "coef_"), "Model is not fitted"

    # Check if the scaler is fitted
    assert hasattr(scaler, "mean_"), "Scaler is not fitted"