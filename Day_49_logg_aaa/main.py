import logging # used to created logs
import os  #help to create new file and floder and acess them

from datetime import datetime # used to get the current date and time

from sklearn.datasets import load_breast_cancer # used to load the breast cancer dataset
from sklearn.linear_model import LogisticRegression # used to create a logistic regression model

from sklearn.model_selection import train_test_split # used to split the dataset into training and testing sets
from sklearn.metrics import accuracy_score # used to calculate the accuracy of the model

# create= a log file to store thr logs

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)


# create a log file with the current date and time
log_file = os.path.join(log_dir, f"mlpipeline_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# configure the logging setting and consule output

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(message)s", # log format to include timestamp, log level, and message
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]       
)

logging.info("Starting the ML pipeline...")

# step:2 Load the dataset

try:
    data = load_breast_cancer()
    X = data.data # features
    y = data.target #target variable
    logging.debug(f"Features Names : {data.feature_names}")
    logging.info(f"Dataset loaded successfully with :{X.shape[0]} ,samples and {X.shape[1]} : features.")

except Exception as e:
    logging.critical(f"Error loading dataset: {e}")


# step:3 Split the dataset into training and testing sets

try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    logging.info(f"Dataset split into training and testing sets with {X_train.shape[0]} training samples and {X_test.shape[0]} testing samples.")
except Exception as e:
    logging.critical(f"Error splitting dataset: {e}")

# step:4 Create and train the logistic regression model

try:
    model = LogisticRegression()
    model.fit(X_train, y_train)
    logging.info("Model trained successfully.")
except Exception as e:
    logging.critical(f"Error training model: {e}")

# step:5 Make predictions on the test set

try:
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"Model accuracy: {accuracy:.4f}")
    logging.info("Predictions made successfully.")

    if accuracy < 0.98:
        logging.warning(f"Model accuracy is below 98%: {accuracy:.4f}")

except Exception as e:
    logging.critical(f"Error making predictions: {e}")