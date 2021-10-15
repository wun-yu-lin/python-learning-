import pandas as pd
import numba as nb
Peak_table_path = input("請給MS1 peak table.xlsx的檔案位置:")
SIRIUS_results_path = input("請給SIRIUS results.xlsx的檔案位置:")
mz_tol = input("請給mz tolerance參數 ex:20 (ppm):")
mz_tol = float(mz_tol)
rt_tol = input("請給rt tolerance，單位為 秒:")
rt_tol = int(rt_tol)
Peak_table = pd.read_excel(Peak_table_path)
SIRIUS_results = pd.read_excel(SIRIUS_results_path)
print(Peak_table_path)
print(SIRIUS_results_path)

mz_peaktable = Peak_table["mzmed"]
rt_peaktable = Peak_table["rtmed"]
mz_sirius =  SIRIUS_results["ionMass"]
rt_sirius = SIRIUS_results["retentionTimeInSeconds"]
Peak_table_index = list(Peak_table.index)
SIRIUS_results_index = list(SIRIUS_results.index)

for x in Peak_table_index:
    