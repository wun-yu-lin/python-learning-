# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:41:57 2021

@author: wunyu
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

excel_file_path = input("請給檔案位置:")
heatmap_data=pd.read_excel(excel_file_path, index_col="Row.names")

species = heatmap_data.iloc[0,0:]
dicts = dict(zip(species.unique(), "rb"))
col_colors = species.map(dicts)
heatmap_data = heatmap_data.drop(index="species")
heatmap_data = heatmap_data.astype(int)
sns.clustermap(heatmap_data,
                row_cluster=True,
                col_cluster=True,
                cmap="coolwarm",
                z_score=0,
                figsize=(30,34),
                col_colors=col_colors
                 )
plt.savefig("heatmap_30_34.png",dpi= 1000)


