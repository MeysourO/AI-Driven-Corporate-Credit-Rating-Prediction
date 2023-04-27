# AI-Driven-Corporate-Credit-Rating-Prediction

# Corporate Rating Analysis

This project aims to build a machine learning model to predict the creditworthiness of companies based on financial ratios. The model is deployed using Streamlit to create a user-friendly interface for users to input company information and get a predicted corporate rating.

## Folders

- **data set**: This folder contains the dataset used to train the machine learning model, as well as the validation set. The training dataset includes labeled financial ratios and corresponding corporate ratings, while the validation set is used to evaluate the performance of the model.

- **notebook file**: This folder contains the Jupyter notebook file where the model is trained and evaluated. It also includes the Streamlit application code for deploying the model as a user interface.

- **pickles file**: This folder contains the pickled files of the trained machine learning model and transformers. These files are used to load the trained model and transformers for making predictions in the Streamlit application.

## Data Collection

The financial data for this project was obtained from the [Financial Modeling Prep API](https://financialmodelingprep.com/developer/docs/). The data was cleaned and preprocessed to remove missing values and outliers.

## Feature Engineering

Several financial ratios were used as features in the machine learning model, including liquidity measurement ratios, profitability indicator ratios, debt ratios, operating performance ratios, and cash flow indicator ratios.

## Model Selection and Training

A random forest classifier was chosen as the machine learning model for this project, and it was trained on the labeled dataset of financial ratios and corresponding corporate ratings. The accuracy of the model was evaluated using metrics such as precision, recall, and F1 score.

## Model Validation

A validation set was used to evaluate the performance of the model and ensure it was not overfitting the training data. The validation set was preprocessed in the same way as the training data and was used to calculate accuracy metrics.

## Streamlit Application

The machine learning model was deployed using Streamlit to create a user-friendly interface for users to input company information and get a predicted corporate rating. The interface includes input fields for company symbol, year, and several financial ratios, as well as a button to submit the inputs and get the predicted rating.

## Getting Started

To use the Streamlit application, you will need to install the necessary dependencies using the following command:

!pip install -r requirements.txt


Once the dependencies are installed, you can run the application using the following command:

streamlit run app.py


## Future Work

In the future, we plan to incorporate additional financial data sources to improve the accuracy of the model and expand the range of companies that can be analyzed. We also plan to add more features to the Streamlit interface to make it even more user-friendly.

## Contributors

Please feel free to contribute to this project by submitting bug reports, feature requests, or pull requests. We appreciate any and all contributions!

If you have any questions or need further assistance, please feel free to reach out to me at meysour.o@gmail.com.



