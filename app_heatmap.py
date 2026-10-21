import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfHeatmap =         pd.read_csv('dados_heatmap.csv', encoding='latin1')     # dia_semana, horario, movimento_clientes

dadosHeatMap = dfHeatmap.pivot_table(index='dia_semana', columns='horario', values='movimento_clientes', aggfunc='mean')
ordem_dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

dadosHeatMap = dadosHeatMap.reindex(
    [dia for dia in ordem_dias if dia in dadosHeatMap.index]
)

fig, ax = plt.subplots(figsize=(12, 6))

sns.heatmap(
    dadosHeatMap,
    annot=True,
    fmt='.0f',
    cmap='coolwarm',
    linewidths=0.5,
    ax=ax
)
ax.set_title('Mapa de Calor do Movimento de Clientes')
ax.set_xlabel('Horário')
ax.set_ylabel('Dia da Semana')
fig.tight_layout()
plt.show()