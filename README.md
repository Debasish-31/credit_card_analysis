# Credit Card Default Prediction

## Project Overview
This project is a web application that predicts the likelihood of a credit card default based on various financial and personal factors. It uses a machine learning model to make predictions and presents the results through a user-friendly web interface.

## Features
- Web-based interface for inputting customer data
- Real-time prediction using a pre-trained machine learning model
- Secure handling of sensitive financial information
- Responsive design for use on various devices

## Technology Stack
- Backend: Python, Flask
- Frontend: HTML, CSS
- Machine Learning: scikit-learn
- Data Preprocessing: StandardScaler

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/credit-card-default-prediction.git
    cd credit-card-default-prediction
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the trained model (`clf2.pkl`) and scaler (`train_scaler.pkl`) in the `models/` directory.

2. Run the Flask application:
    ```sh
    python main.py
    ```

3. Open a web browser and navigate to `http://localhost:5000`.

4. Fill in the form with the required information and submit to get the prediction.

## Model Information
The prediction model used in this project is a [type of model, e.g., Random Forest Classifier] trained on historical credit card data. It takes into account factors such as credit limit, payment history, bill amounts, and personal information to predict the likelihood of default.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.
Project Link: [https://github.com/SudeeptaGiri/CreditCard-Defaulter-Analysis.git](https://github.com/SudeeptaGiri/CreditCard-Defaulter-Analysis.git)
