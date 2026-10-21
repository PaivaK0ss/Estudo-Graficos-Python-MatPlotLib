import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfPizza =           pd.read_csv('dados_pizza.csv', encoding='latin1')       # canal_venda, faturamento

dadosPizza = dfPizza.groupby('canal_venda')['faturamento'].sum()
fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    dadosPizza.values,
    labels=dadosPizza.index,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.7
)

ax.set_title('Participação no Faturamento por Canal de Venda')
ax.axis('equal')
plt.show()