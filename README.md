# Fashion E-Commerce Product Success Prediction

## Overview

This repository contains the code and analysis for predicting the success of fashion e-commerce products. The analysis involves exploratory data analysis (EDA), model development using Random Forest and Artificial Neural Network (ANN), and model selection.

## Files

1. `eda.ipynb`: Jupyter Notebook containing Exploratory Data Analysis (EDA) of the historical dataset, including visualizations and insights derived from the data.

2. `model_randomforest.py`: Python script implementing the Random Forest model for predicting product success. The script follows an object-oriented approach with functions for loading data, preprocessing, training, testing, and prediction.

3. `model_ann.py`: Python script implementing the Artificial Neural Network (ANN) model for predicting product success. Similar to the Random Forest model, it follows an object-oriented approach with functions for data loading, preprocessing, training, testing, and prediction.

4. `model_selection.ipynb`: Jupyter Notebook containing the model selection pipeline, including training and evaluation of Random Forest and ANN models, hyperparameter tuning, and selection of the final model.

5. `historic.csv`: CSV file containing historical data of past fashion e-commerce products, including attributes like category, main promotion, color, stars, and success indicator.

6. `prediction_input.csv`: CSV file containing potential products for the upcoming year and their attributes (no success indicator).

7. `README.md`: This file, providing an overview of the repository and its contents, along with instructions for running the analysis.

## Approach

1. **Exploratory Data Analysis (EDA)**: Conducted initial data exploration to understand the characteristics of the historical dataset, identify patterns, and gain insights into factors influencing product success.

2. **Model Development**: Developed two models for predicting product success: Random Forest and Artificial Neural Network (ANN). Implemented the models in separate Python scripts (`model_randomforest.py` and `model_ann.py`) following an object-oriented approach.

3. **Model Selection**: Compared the performance of the Random Forest and ANN models using a model selection pipeline (`model_selection.ipynb`). Evaluated the models using appropriate metrics, performed hyperparameter tuning, and selected the best-performing model for predicting product success.

## How to Use

1. Clone the repository to your local machine:

git clone <(https://github.com/mayyurs/dsw_ML_test)>

2. Navigate to the cloned directory:
   
4. Install the required dependencies:

4. Run the Jupyter Notebooks (`eda.ipynb` and `model_selection.ipynb`) to perform exploratory data analysis and model selection, respectively.

5. Execute the Python scripts (`model_randomforest.py` and `model_ann.py`) to train, test, and predict using the Random Forest and ANN models.

## Dependencies

- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

## Author

[Mayur Shinde](github.com/mayyurs)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





