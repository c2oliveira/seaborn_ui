import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Criando um DataFrame fictício com dados de vendas
dados = {
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
    "Vendas": [2000, 2500, 1800, 2200, 3000, 5000, 4000],
    "Clientes": [150, 180, 130, 160, 210, 300, 270],
    "Lucro": [400, 500, 360, 440, 600, 1000, 800]
}

df = pd.DataFrame(dados)

# Configurando estilo do Seaborn
sns.set_style("whitegrid")

# Gráfico de barras - Total de vendas por dia
plt.figure(figsize=(10, 5))
sns.barplot(x="Dia", y="Vendas", data=df, palette="Blues")
plt.title("Total de Vendas por Dia")
plt.xlabel("Dia da Semana")
plt.ylabel("Vendas em R$")
plt.xticks(rotation=45)
plt.show()

# Gráfico de dispersão - Relacionando número de clientes e total de vendas
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Clientes", y="Vendas", data=df, color="red")
plt.title("Relação entre Número de Clientes e Total de Vendas")
plt.xlabel("Número de Clientes")
plt.ylabel("Total de Vendas em R$")
plt.show()

# Heatmap - Correlação entre vendas, número de clientes e lucro
plt.figure(figsize=(6, 4))
sns.heatmap(df[["Vendas", "Clientes", "Lucro"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlação entre Variáveis")
plt.show()

# Explicação dos gráficos:
# 1. O gráfico de barras mostra o total de vendas por dia, permitindo identificar quais dias tiveram melhores resultados.
# 2. O gráfico de dispersão evidencia a relação entre o número de clientes e o total de vendas, ajudando a entender se mais clientes resultam em maior faturamento.
# 3. O heatmap exibe a correlação entre as variáveis, permitindo visualizar como vendas, clientes e lucro estão relacionados.
