import pandas as pd
import random

n_within_condition = 50

## Comment the line below if you want to get a different order than default
random.seed(8710)


id = [i for i in range(1,2*n_within_condition+1,1)]
conditions = ['visible', 'invisible'] * n_within_condition
random.shuffle(conditions)


pd.DataFrame({'id': id,
             'condition': conditions}).to_csv(path_or_buf='conditions.csv', sep = ';', index=False)
