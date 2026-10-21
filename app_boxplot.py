import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfBoxplot =         pd.read_csv('dados_boxplot.csv', encoding='latin1')     # departamento, salario

dfBoxplot = dfBoxplot.dropna(subset=['departamento', 'salario'])

dadosBoxPlot = [
    grupo['salario'].values
    for _, grupo in dfBoxplot.groupby('departamento')
]

departamentos = dfBoxplot.groupby('departamento').groups.keys()

fig, ax = plt.subplots(figsize=(12, 6))
ax.boxplot(dadosBoxPlot, tick_labels=list(departamentos), patch_artist=True, showmeans=True)

ax.set_title('Distribuição dos salários por departamento')
ax.set_xlabel('Departamento')
ax.set_ylabel('Salário (R$)')
plt.xticks(rotation=45, ha='right')
ax.grid(axis='y', linestyle='--', alpha=0.5)
fig.tight_layout()
plt.show()