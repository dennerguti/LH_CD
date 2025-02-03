import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('teste_indicium_precificacao.csv')

print("Análise do impacto do número mínimo de noites no preço:")
preco_por_minimo_noites = df.groupby('minimo_noites')['price'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=preco_por_minimo_noites, x='minimo_noites', y='price')
plt.title('Preço Médio por Número Mínimo de Noites')
plt.xlabel('Número Mínimo de Noites')
plt.ylabel('Preço Médio')
plt.show()


df['disponibilidade_categoria'] = pd.cut(df['disponibilidade_365'], bins=[0, 120, 240, 365], labels=['Baixa', 'Média', 'Alta'])
preco_por_disponibilidade = df.groupby('disponibilidade_categoria')['price'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=preco_por_disponibilidade, x='disponibilidade_categoria', y='price')
plt.title('Preço Médio por Disponibilidade')
plt.xlabel('Categoria de Disponibilidade')
plt.ylabel('Preço Médio')
plt.show()