import glob
import zipfile
import os
import pandas as pd
import pyarrow.parquet as pq
#unzip main folder
with zipfile.ZipFile("202405.zip", "r") as zfile:
    zfile.extractall()
os.remove("202405.zip")
#unzip 31 folders
files = glob.glob("F:/python basic/dataAnalysis/project/202405/2024*.zip")
for file in files:
    extraction_path = f"F:/python basic/dataAnalysis/project/202405/{os.path.splitext(os.path.basename(file))[0]}/"
    with zipfile.ZipFile(file, "r") as zfile2:
        zfile2.extractall(extraction_path)
    os.remove(file)