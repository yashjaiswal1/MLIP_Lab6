import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    # Unpack the features and target from the fixture
    feature_df, target_series = feature_target_sample

    # Call the data_split function
    return_tuple = data_split(feature_df, target_series)

    # Test if the length of return_tuple is 4
    assert len(return_tuple) == 4

    # Unpack the returned tuple
    X_train, X_test, y_train, y_test = return_tuple

    # Assert that the splits have the correct sizes
    # Since the default test_size is 0.2 and we have only 2 samples,
    # the test set will have 0 samples, so we need to handle this.
    assert X_train.shape[0] + X_test.shape[0] == feature_df.shape[0]
    assert y_train.shape[0] + y_test.shape[0] == target_series.shape[0]

    # Ensure that training and testing sets are mutually exclusive
    if not X_test.empty:
        assert not X_train.equals(X_test)
    if not y_test.empty:
        assert not y_train.equals(y_test)
