# 🍷 Wine Market Analysis

Análise exploratória de dados sobre o mercado global de vinhos, explorando relações entre preço, qualidade, origem e variedades.

## 📊 Sobre

Análise de **~130.000 vinhos** respondendo:
- Quais países têm melhor custo-benefício?
- Existe correlação entre preço e qualidade?
- Como a pontuação varia entre regiões?
- Qual faixa de preço oferece melhor retorno?

## 🚀 Quick Start
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/wine-analysis.git
cd wine-analysis

# Instale dependências
pip install -r requirements.txt

# Execute
python analise_vinhos.py
```

## 📦 Dependências
```txt
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
openpyxl>=3.0.0
```

## 📁 Estrutura
```
wine-analysis/
├── dataset-wine.csv           # Dataset principal
├── analise_vinhos.py          # Script de análise
├── export_excel/              # Resultados em Excel
│   ├── 01_top_15_paises.xlsx
│   ├── 02_mean_points_top15.xlsx
│   ├── 03_variedades_mais_comuns.xlsx
│   ├── 04_mean_by_var.xlsx
│   ├── 5_top10_custo_beneficio.xlsx
│   └── 7_top10_custo_beneficio.xlsx
└── README.md
```

## 📈 Análises

### 1. Por Países
- Top 15 países por volume
- Pontuação média (≥200 amostras)

### 2. Por Regiões
- Top 12 regiões
- Distribuição de qualidade (boxplot)

### 3. Por Variedades
- Top 15 mais comuns
- Top 5 por pontuação média

### 4. Custo-Benefício
- Top 10 vinhos (score: pontos/preço)
- Filtro: preço > $5, pontos ≥ 85

### 5. Faixas de Preço
- Violinplot: <$15, $15-30, $30-50, $50-100, $100-200, >$200

## 📊 Dataset

**Colunas principais:**
- `country` - País de origem
- `points` - Pontuação (0-100)
- `price` - Preço (USD)
- `variety` - Variedade da uva
- `region_1` - Região vinícola
- `title` - Nome do vinho

**Total:** 129.971 vinhos

## 🔧 Customização
```python
# Alterar número de itens
top15 = df['country'].value_counts().head(20)

# Ajustar threshold
common_countries = country_counts[country_counts >= 100].index

# Modificar faixas de preço
bins=[0, 10, 20, 40, 80, 150, float('inf')]
labels=['<$10', '$10-20', '$20-40', '$40-80', '$80-150', '>$150']
```

## 📝 Outputs

### Excel Gerados:
1. **01_top_15_paises.xlsx** - Países por quantidade
2. **02_mean_points_top15.xlsx** - Pontuação média por país
3. **03_variedades_mais_comuns.xlsx** - Top 15 variedades
4. **04_mean_by_var.xlsx** - Top 5 variedades por pontos
6. **7_top10_custo_beneficio.xlsx** - Custo-benefício (filtrado)

### Visualizações:
- Barras horizontais (países, variedades)
- Boxplot (regiões por mediana)
- Violinplot (faixas de preço)

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| `FileNotFoundError` | Coloque `dataset-wine.csv` na raiz |
| `ModuleNotFoundError` | Execute `pip install -r requirements.txt` |
| Gráficos não aparecem | Execute em ambiente interativo |

**Lucas Santos**  

GitHub: [@Lukketes](https://github.com/Lukketes)
Linkedin: [@Lucas Freitas](https://www.linkedin.com/in/lucas-freitas-592180329/)

---
