import os
import pandas as pd
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data.csv')
df = pd.read_csv(file_path)
print(df.iloc[9, :])