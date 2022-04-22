from unittest.mock import MagicMock

def sort_values(by, ascending):
    return MagicMock()
    
df = MagicMock()
df.sort_values = MagicMock(spec = sort_values)