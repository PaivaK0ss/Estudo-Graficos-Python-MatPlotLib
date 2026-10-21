import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfDispersao =       pd.read_csv('dados_dispersao.csv', encoding='latin1')   # altura_cm, peso_kg, sexo

fig, ax = plt.subplots(figsize=(10, 6))

for sexo, grupo in dfDispersao.groupby('sexo'):
    ax.scatter(grupo['altura_cm'], grupo['peso_kg'], label=sexo, alpha=0.7)

ax.set_title('Relação entre Altura e Peso por Sexo')
ax.set_xlabel('Altura (cm)')
ax.set_ylabel('Peso (kg)')
ax.legend(title='Sexo')
ax.grid(True, linestyle='--', alpha=0.4)

fig.tight_layout()
plt.show()