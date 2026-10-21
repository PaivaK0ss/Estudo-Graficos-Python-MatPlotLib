import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfFrequencia =      pd.read_csv('dados_frequencia.csv', encoding='latin1')  # id_chamado, tipo_atendimento

fig, ax = plt.subplots(figsize=(10, 6))
frequencia = dfFrequencia['tipo_atendimento'].value_counts()
sns.barplot(x=frequencia.index, y=frequencia.values, ax=ax)

for barra in ax.patches:
    altura = barra.get_height()
    ax.annotate(
        f'{int(altura)}', (barra.get_x() + barra.get_width() / 2, altura), ha='center', va='bottom', xytext=(0, 3), textcoords='offset points')

ax.set_title('Frequência por Tipo de Atendimento')
ax.set_xlabel('Tipo de Atendimento')
ax.set_ylabel('Quantidade de Chamados')
plt.xticks(rotation=45, ha='right')
fig.tight_layout()
plt.show()