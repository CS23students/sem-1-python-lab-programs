# numpy and pandas

# import numpy and pandas

# numpy
import pandas as pd
import numpy as np
M1 = np.array([[1, 1, 1], [1, 1, 1], [1, -14, 21]])
M2 = np.array([[1, -1, 1], [1, 1, 1], [1, 4, 21]])
M3 = M1 + M2

print("Numpy: \n", M3)


# pandas
data = {"Name:": ["Tom", "Nick", "John", "krish"], "Age": [20, 21, 22, 24]}
df = pd.DataFrame(data)
print("Pandas: \n", df)
