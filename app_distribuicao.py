import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfDistribuicao =    pd.read_csv('dados_distribuicao.csv', encoding='latin1')# cliente_id, idade

fig, ax = plt.subplots(figsize=(10, 6))

sns.histplot(data=dfDistribuicao, x='idade', bins=15, kde=True, ax=ax)

for barra in ax.patches:
    altura = barra.get_height()
    if altura > 0:
        ax.annotate(f'{int(altura)}', (barra.get_x() + barra.get_width() / 2, altura), ha='center', va='bottom', xytext=(0, 3), textcoords='offset points')

ax.set_title('Distribuição das Idades dos Clientes')
ax.set_xlabel('Idade (anos)')
ax.set_ylabel('Quantidade de clientes')
fig.tight_layout()
plt.show()