import warnings
warnings.filterwarnings('ignore')
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

EXCEL_DIR = Path('export_excel')
EXCEL_DIR.mkdir(exist_ok=True)

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10,6)

df = pd.read_csv('dataset-wine.csv')

df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

print(df.isna().sum().sort_values(ascending=False).head(15))

def top_n_by(df, column, n=15):
    return df[column].value_counts().head(n)

##ANÁLISE POR PAÍS##
# País com maior número de vinhos - GERAÇÃO DE GRÁFICO
# Top 15 países com maior quantidade de vinhos (DADOS PARA GRÁFICO)
if 'country' in df.columns:
    top15 = df['country'].value_counts().head(15)
    print('Top 15 países com maior quantidade de vinhos:\n')

    # Converter para DataFrame com o índice como coluna
    top15_df = top15.reset_index()
    top15_df.columns = ['País', 'Quantidade']

    top15_df.to_excel(EXCEL_DIR / '01_top_15_paises.xlsx', index=False)
    print("✓ 01_top_15_paises.xlsx")


# Média de pontos por país (top 15 por número de registros para evitar ruído)
if 'points' in df.columns and 'country' in df.columns:
    country_counts = df['country'].value_counts()
    common_countries = country_counts[country_counts >= 200].index
    mean_points = df[df['country'].isin(common_countries)].groupby('country')['points'].mean().sort_values(
        ascending=False).head(15)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=mean_points.values, y=mean_points.index)
    plt.xlabel('Média de pontos')
    plt.title('Média de pontos por país (países com ≥200 amostras)')

# Média de pontos dos TOP 15 países por número de registros (DADOS PARA GRÁFICO)
if 'points' in df.columns and 'country' in df.columns:
    # 1. Identificar os 15 países com mais registros
    country_counts = df['country'].value_counts()
    top15_countries = country_counts.head(15).index

    # 2. Filtrar o dataframe somente para esses 15 países
    df_top15 = df[df['country'].isin(top15_countries)]

    # 3. Calcular a média de pontos por país (somente entre os Top 15)
    mean_points_top15 = (
        df_top15.groupby('country')['points']
        .mean()
        .sort_values(ascending=False)
    )

    # Exibir resultado
    print("Média de pontos por país (somente TOP 15 por número de registros):\n")
    print(mean_points_top15)

    # EXPORTAR
    mean_points_top15_df = mean_points_top15.reset_index()
    mean_points_top15_df.columns = ['País', 'Pontuação Média']

    mean_points_top15_df.to_excel(EXCEL_DIR / '02_mean_points_top15.xlsx', index=False)
    print("✓ 02_mean_points_top15.xlsx")

##ANÁLISE POR REGIÃO - ORDENADO POR MEDIANA##

if 'region_1' in df.columns and 'points' in df.columns:
    top_regions = df['region_1'].value_counts().dropna().head(12)
    df_filtered = df[df['region_1'].isin(top_regions.index)]
    region_median = df_filtered.groupby('region_1')['points'].median().sort_values(ascending=True)

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='points', y='region_1', data=df_filtered, order=region_median.index)
    plt.title('Distribuição de pontos nas principais regiões')
    plt.show()

if 'region_1' in df.columns and 'points' in df.columns:
    top_regions = df['region_1'].value_counts().dropna().head(12)
    df_filtered = df[df['region_1'].isin(top_regions.index)]
    region_median = df_filtered.groupby('region_1')['points'].median().sort_values(ascending=False)

    top_regions_df = region_median.reset_index()
    top_regions_df.columns = ['region_1', 'mediana_pontos']

    print(top_regions_df)

# Pontuação média por região × variedade (pivot)
if all(c in df.columns for c in ['region_1','variety','points']):
    pivot = pd.pivot_table(df[df['region_1'].notna()], values='points', index='region_1', columns='variety', aggfunc='mean')
# Nota: pivot pode ser grande; exemplo abaixo mostra como pegar top 10 variedades
    print(pivot.iloc[:10, :10])


##VARIEDADES##
#Top 15 - Variedades mais comuns
if 'variety' in df.columns:
    plt.figure(figsize=(12,6))
    top_varieties = df['variety'].value_counts().head(15)
    sns.barplot(x=top_varieties.values, y=top_varieties.index)
    plt.title('Top 15 variedades mais comuns')
    plt.show()

# Criar a série com as 15 variedades mais comuns
top_varieties = df['variety'].value_counts().head(15)

# EXPORTAR
dados_grafico = top_varieties.reset_index()
dados_grafico.columns = ['Variety', 'Quantidade']

dados_grafico.to_excel(EXCEL_DIR / '03_variedades_mais_comuns.xlsx', index=False)
print("✓ 03_variedades_mais_comuns.xlsx")

# Pontuação média por variedade (exemplo para top 5)
if 'points' in df.columns and 'variety' in df.columns:
    mean_by_var = df.groupby('variety')['points'].mean().sort_values(ascending=False).head(5)
    plt.figure(figsize=(12,6))
    sns.barplot(x=mean_by_var.values, y=mean_by_var.index)
    plt.title('Média de pontos por variedade (top 5 por média)')

    # EXPORTAR
    mean_by_var_df = mean_by_var.reset_index()
    mean_by_var_df.columns = ['Variety', 'Quantidade']

    mean_by_var_df.to_excel(EXCEL_DIR / '04_mean_by_var.xlsx', index=False)
    print("✓ 04_mean_by_var.xlsx")

##TOP 10 CUSTO-BENEFÍCIO##

if 'price' in df.columns and 'points' in df.columns:
    df_cb = df.dropna(subset=['price', 'points']).copy()
    df_cb['custo_beneficio'] = df_cb['points'] / df_cb['price']
    plt.show()

# EXPORTAR EXCEL
if 'price' in df.columns and 'points' in df.columns:
    df_cb = df.dropna(subset=['price', 'points']).copy()
    df_cb['custo_beneficio'] = df_cb['points'] / df_cb['price']
    top10_cb = df_cb.nlargest(10, 'custo_beneficio')

    dados_grafico = top10_cb[['title', 'country', 'variety', 'price', 'points', 'custo_beneficio']].copy()
    dados_grafico.columns = ['Vinho', 'País', 'Variedade', 'Preço (USD)', 'Pontos', 'Score CB']
    dados_grafico = dados_grafico.round(2).reset_index(drop=True)

    dados_grafico.to_excel(EXCEL_DIR / '5_top10_custo_beneficio.xlsx', index=False)
    print("✓ 5_top10_custo_beneficio.xlsx")



##FAIXAS DE PREÇO VS QUALIDADE

if 'price' in df.columns and 'points' in df.columns:
    # Criar faixas de preço
    df_faixas = df.dropna(subset=['price', 'points']).copy()
    df_faixas['faixa_preco'] = pd.cut(df_faixas['price'],
                                      bins=[0, 15, 30, 50, 100, 200, float('inf')],
                                      labels=['<$15', '$15-30', '$30-50',
                                              '$50-100', '$100-200', '>$200'])

    plt.figure(figsize=(12, 6))
    sns.violinplot(x='faixa_preco', y='points', data=df_faixas,
                   palette='viridis', inner='quartile')
    plt.xlabel('Faixa de Preço', fontsize=12, fontweight='bold')
    plt.ylabel('Pontuação', fontsize=12, fontweight='bold')
    plt.title('Distribuição de Pontuação por Faixa de Preço 🎻', fontsize=15, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

##TOP 10 CUSTO-BENEFÍCIO##

if 'price' in df.columns and 'points' in df.columns and 'title' in df.columns:
    # Filtrar: preço > $5 E pontos >= 85
    df_cb = df.dropna(subset=['price', 'points', 'title']).copy()
    df_cb = df_cb[(df_cb['price'] > 5) & (df_cb['points'] >= 85)]
    df_cb['custo_beneficio'] = df_cb['points'] / df_cb['price']

    # Top 10
    top10_cb = df_cb.nlargest(10, 'custo_beneficio')

    plt.figure(figsize=(12, 6))
    sns.barplot(x='custo_beneficio', y='title', data=top10_cb.head(10), palette='RdYlGn')
    plt.xlabel('Score Custo-Benefício')
    plt.title('Top 10 Vinhos: Melhor Custo-Benefício')
    plt.tight_layout()
    plt.show()

# EXPORTAR EXCEL
if 'price' in df.columns and 'points' in df.columns and 'title' in df.columns:
    df_cb = df.dropna(subset=['price', 'points', 'title']).copy()
    df_cb = df_cb[(df_cb['price'] > 5) & (df_cb['points'] >= 85)]
    df_cb['custo_beneficio'] = df_cb['points'] / df_cb['price']

    top10_cb = df_cb.nlargest(10, 'custo_beneficio')

    dados_grafico = top10_cb[['title', 'custo_beneficio']].reset_index(
        drop=True)
    dados_grafico.columns = ['Vinho', 'Score CB']
    dados_grafico = dados_grafico.round(2)

    dados_grafico.to_excel(EXCEL_DIR / '7_top10_custo_beneficio.xlsx', index=False)
    print("✓ 7_top10_custo_beneficio.xlsx")
