import numpy as np
import pandas as pd

numbers = np.random.randint(1, 100, 10)

series = pd.Series(numbers)

print("Pandas Series:")
print(series)
