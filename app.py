import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfBarras =          pd.read_csv('dados_barras.csv', encoding='latin1')      # categoria, regiao, vendas_medias
dfBoxplot =         pd.read_csv('dados_boxplot.csv', encoding='latin1')     # departamento, salario
dfDispersao =       pd.read_csv('dados_dispersao.csv', encoding='latin1')   # altura_cm, peso_kg, sexo
dfDistribuicao =    pd.read_csv('dados_distribuicao.csv', encoding='latin1')# cliente_id, idade
dfFrequencia =      pd.read_csv('dados_frequencia.csv', encoding='latin1')  # id_chamado, tipo_atendimento
dfHeatmap =         pd.read_csv('dados_heatmap.csv', encoding='latin1')     # dia_semana, horario, movimento_clientes
dfLinhas =          pd.read_csv('dados_linhas.csv', encoding='latin1')      # data, vendas, loja
dfPizza =           pd.read_csv('dados_pizza.csv', encoding='latin1')       # canal_venda, faturamento
dfRegressao =       pd.read_csv('dados_regressao.csv', encoding='latin1')   # renda_mensal,gasto_mensal


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