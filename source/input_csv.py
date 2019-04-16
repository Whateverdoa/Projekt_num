import pandas as pd
import pandas.util.testing as tm
import numpy as np
np.random.seed(444)

tijd = tm.makeTimeDataFrame(freq="M").head()

adf2 = tm.makeDataFrame().head()

a = tm.all_index_generator()
for num in a:
    print(num)
