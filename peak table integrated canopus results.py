import pandas as pd
Peak_table_path = input("請給MS1 peak table.xlsx的檔案位置:")
CANOPUS_results_path = input("請給CANOPUS results.xlsx的檔案位置:")
Peak_table = pd.read_excel(Peak_table_path)
CANOPUS_results = pd.read_excel(CANOPUS_results_path)
print(Peak_table_path)
print(CANOPUS_results_path)

id_peaktable = Peak_table["SIRIUS_ID"]
id_canopus =  CANOPUS_results["ID"]
Peak_table_index = list(Peak_table.index)
CANOPUS_results_index = list(CANOPUS_results.index)
Peaktable_canopus = pd.DataFrame()
list_x = list(Peak_table.iloc[0:1])+list(CANOPUS_results.iloc[0:1])
Peaktable_canopus = Peaktable_canopus.append([list_x])
for x in Peak_table_index:
    list_x = list(Peak_table.iloc[x])
    for y in CANOPUS_results_index:
        if id_canopus[y] == id_peaktable[x]:
            list_x = list_x + list(CANOPUS_results.iloc[y])
            break
    Peaktable_canopus = Peaktable_canopus.append([list_x])

with pd.ExcelWriter('Peaktable_canopus_result.xlsx') as writer:  
            Peaktable_canopus.to_excel(writer, sheet_name='Peaktable_canopus_result')