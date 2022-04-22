from sklearn.pipeline import Pipeline, make_pipeline

class model():
    """Perform automatic sales forecast for specified time period using not prepared data.

    Attributes
    ----------
    pipeline_ : Pipeline
        Pipeline created during fitting with steps including
        data preparation->modeling->model evaluation->forecast visualization.
    """
    

    def __init__(self):
        return

    def make_forecast(data, period=30, prediction_level):
    """Make a sales forecast and visualize it.

    Automatically performs the following:
    - prepares data (data_preparation submodule)
    - performs modeling along with feature selection and hyparameter tuning
    - evaluates the accuracy of models and chooses the most effective
    - makes an easy to read visualization of the forecast

    Parameters
    ----------
    data : str
        The full name of the dataset that will be used to predict sales.
        Must be placed in the data folder in CSV format.
        The column with historical sales data must be called 'sales'.

    period : int, default=30
        Time period in days for which sales forecast will be made.
    
    prediction_level : str
        Level (column name) at which sales predictions will be made.
        For example, for each SKU or product category.

    Returns : ndarray
    ----------
        Predicted sales value for each SKU, product category, etc.
        depending on prediction_level set.
    """
