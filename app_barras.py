import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfBarras =          pd.read_csv('dados_barras.csv', encoding='latin1')      # categoria, regiao, vendas_medias

dadosBarras = dfBarras.pivot_table( index='categoria', columns='regiao', values='vendas_medias', aggfunc='sum', fill_value=0)

x = np.arange(len(dadosBarras.index))
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

regioes = ['Norte', 'Leste', 'Sul', 'Oeste']
for i, regiao in enumerate(regioes):
    if regiao in dadosBarras.columns:
        deslocamento = (i - (len(regioes) - 1) / 2) * width
        barras = ax.bar(x + deslocamento, dadosBarras[regiao], width, label=regiao )
        ax.bar_label(barras, padding=3)

ax.set_ylim(top=dadosBarras.max().max() * 1.15)
ax.set_title('Vendas por categoria ao redor das regiões')
ax.set_xlabel('Categoria')
ax.set_ylabel('Vendas Médias (R$)')
ax.set_xticks(x)
ax.set_xticklabels(dadosBarras.index, rotation=45, ha='right')
ax.legend()
fig.tight_layout()
plt.show()