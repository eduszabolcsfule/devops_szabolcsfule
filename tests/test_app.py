import pytest
import pandas as pd
from io import StringIO
from app.main import load_data

@pytest.fixture
def sample_csv():
    csv_data = "Tevékenység,Órák száma\nAlvás,12\nEvés,4\nJáték,2\n"
    return StringIO(csv_data) 

def test_load_data(sample_csv):
    # test load data
    df = load_data(sample_csv)
    
    # is pandas dataframe
    assert isinstance(df, pd.DataFrame), "A visszaadott objektumnak pandas DataFrame-nek kell lennie"
    
    # dataframe is not empty
    assert not df.empty, "A beolvasott DataFrame üres"
