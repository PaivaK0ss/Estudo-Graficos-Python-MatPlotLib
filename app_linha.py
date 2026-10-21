import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfLinhas =          pd.read_csv('dados_linhas.csv', encoding='latin1')      # data, vendas, loja

dfLinhas['data'] = pd.to_datetime(dfLinhas['data'])

dadosLinhas = dfLinhas.groupby(['data', 'loja'])['vendas'].sum().reset_index()

dadosLinhas = dadosLinhas.sort_values('data')

fig, ax = plt.subplots(figsize=(12, 6))

for loja, grupo in dadosLinhas.groupby('loja'):
    ax.plot(grupo['data'], grupo['vendas'], marker='o', label=loja)

ax.set_title('Evolução das Vendas por Loja')
ax.set_xlabel('Data')
ax.set_ylabel('Vendas (R$)')
ax.legend(title='Loja')
ax.grid(True, linestyle='--', alpha=0.4)

plt.xticks(rotation=45)
fig.tight_layout()
plt.show()