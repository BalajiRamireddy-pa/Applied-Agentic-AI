# Fixtures : using common data for mulitples

import pytest

import pandas as pd

@pytest.fixture

def sample_data():
    return pd.DataFrame({
        'age': [20, 21, 22, 35],
        'salary': [1000, 2000, 3000, 4000],
        'Buy_insurance': [0,0,1,1]
    })


def test_data_shape(sample_data):
    assert sample_data.shape == (4, 3)


def test_data_target_values(sample_data):
    target = [0, 0, 1, 1]
    assert list(sample_data['Buy_insurance'].tolist()) == target
