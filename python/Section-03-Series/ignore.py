from unittest.mock import MagicMock

pd = MagicMock()

series_data = {
    0: "Baby Blue",
    "Fender Telecaster": "Baby Blue",
    1: "Sunburst",
    "Gibson Les Paul": "Sunburst",
    2: "Dark Green",
    "ESP Eclipse": "Dark Green"
}

def Series(data):
    return MagicMock()

def sort_values(ascending, inplace):
    return MagicMock()
    
def sort_index(ascending, inplace):
    return MagicMock()
	
def getitem(name):
     return series_data[name]

mock_series = MagicMock()
mock_series.sort_values = MagicMock(spec = sort_values)
mock_series.sort_index = MagicMock(spec = sort_index)
mock_series = MagicMock()
mock_series.__getitem__.side_effect = getitem

pd.Series.mock_return_value = MagicMock(spec = Series)
pd.Series.return_value = mock_series