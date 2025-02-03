import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('teste_indicium_precificacao.csv')

# 1.
print("Análise de 'minimo_noites':")
print(f"Mínimo de noites exigidas: {df['minimo_noites'].min()}")
print(f"Máximo de noites exigidas: {df['minimo_noites'].max()}")
print(f"Média de noites exigidas: {df['minimo_noites'].mean():.2f}")
print("\n")

anuncios_extremos = df[df['minimo_noites'] > 30]
print(f"Número de anúncios com exigências extremas (>30 noites): {len(anuncios_extremos)}")
print("\n")


plt.figure(figsize=(8, 5))
sns.histplot(df['minimo_noites'], bins=30, kde=True)
plt.title('Distribuição de Mínimo de Noites Exigidas')
plt.xlabel('Mínimo de Noites')
plt.ylabel('Frequência')
plt.show()

# 2. 
print("Análise de 'numero_de_reviews':")
anuncios_poucas_reviews = df[df['numero_de_reviews'] < 5]
print(f"Número de anúncios com poucas reviews (<5): {len(anuncios_poucas_reviews)}")
print("\n")

plt.figure(figsize=(8, 5))
sns.histplot(df['numero_de_reviews'], bins=30, kde=True)
plt.title('Distribuição do Número de Reviews')
plt.xlabel('Número de Reviews')
plt.ylabel('Frequência')
plt.show()


# 3.
print("Análise de 'calculado_host_listings_count':")
hosts_multiplas_propriedades = df[df['calculado_host_listings_count'] > 3]
print(f"Número de anúncios de hosts com múltiplas propriedades: {len(hosts_multiplas_propriedades)}")
print("\n")

plt.figure(figsize=(8, 5))
sns.histplot(df['calculado_host_listings_count'], bins=30, kde=True)
plt.title('Distribuição de Anúncios por Host')
plt.xlabel('Número de Anúncios por Host')
plt.ylabel('Frequência')
plt.show()

# 54.
print("Análise de 'disponibilidade_365':")
print(f"Disponibilidade média dos anúncios: {df['disponibilidade_365'].mean():.2f} dias")
print("\n")

plt.figure(figsize=(8, 5))
sns.histplot(df['disponibilidade_365'], bins=30, kde=True)
plt.title('Distribuição de Disponibilidade no Ano')
plt.xlabel('Dias Disponíveis no Ano')
plt.ylabel('Frequência')
plt.show()