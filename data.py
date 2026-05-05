import pandas as pd
import numpy as np
import shutil as sh
import od
def = pd.read_csv("Illinois_real_estate_ultimate.csv")
print(df.info())
print(df.head())

os.rename("Illinois_real_estate_ultimate.csv", "real_estate_data.csv")
sh.copy("real_estate_data.csv", "backup_real_estate_data.csv")
sh.move("real_estate_data.csv", "moved_real_estate_data.csv")

