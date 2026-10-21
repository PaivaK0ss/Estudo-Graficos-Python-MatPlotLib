import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfRegressao =       pd.read_csv('dados_regressao.csv', encoding='latin1')   # renda_mensal,gasto_mensal

dfRegressao = dfRegressao.dropna(subset=['renda_mensal', 'gasto_mensal'])

x = dfRegressao['renda_mensal']
y = dfRegressao['gasto_mensal']

coeficientes = np.polyfit(x, y, 1)
reta = np.poly1d(coeficientes)

x_linha = np.linspace(x.min(), x.max(), 100)
y_linha = reta(x_linha)

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x, y, alpha=0.7, label='Dados observados')

ax.plot(x_linha, y_linha, color='red', linestyle='--', label='Regressão linear')

ax.set_title('Regressão Linear: Renda x Gasto Mensal')
ax.set_xlabel('Renda Mensal (R$)')
ax.set_ylabel('Gasto Mensal (R$)')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.4)
fig.tight_layout()
plt.show()