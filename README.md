# 🍷 Análise Exploratória do Mercado de Vinhos

Projeto de análise de dados focado no mercado global de vinhos, explorando relações entre preço, qualidade, origem geográfica, variedades de uva e características regionais. Utilizando técnicas de visualização de dados e análise estatística para extrair insights sobre custo-benefício, padrões de qualidade e oportunidades de mercado.

## 📊 Sobre o Projeto

Este projeto analisa um dataset com **~130.000 vinhos** de diversas origens, pontuações e faixas de preço, respondendo perguntas como:

- Quais países produzem os vinhos com melhor relação qualidade-preço?
- Existe correlação entre preço e pontuação?
- Quais variedades de uva oferecem melhor custo-benefício?
- Como a qualidade varia entre regiões vinícolas?
- Qual faixa de preço oferece o melhor retorno em qualidade?

## 🎯 Funcionalidades

### Análises Implementadas:

1. **Análise por Países**
   - Top países por volume de produção
   - Média de pontuação por país
   - Variação de preços por origem

2. **Análise de Preço vs Qualidade**
   - Correlação entre preço e pontos
   - Top vinhos com melhor custo-benefício
   - Distribuição de preços e outliers

3. **Análise por Variedades**
   - Top 15 variedades mais comuns
   - Pontuação média por variedade
   - Diferenças estatísticas entre castas (ANOVA)

4. **Análise Regional**
   - Top regiões por pontuação
   - Distribuição de qualidade por região (boxplot ordenado por mediana)
   - Variabilidade regional

5. **Análise de Valor**
   - Matriz de valor (scatter plot: preço vs pontos por variedade)
   - Top 10 vinhos com melhor custo-benefício
   - Distribuição de qualidade por faixa de preço (violinplot)

6. **Análise Temporal**
   - Tendências de pontuação ao longo dos anos
   - Evolução de preços

## 📁 Estrutura do Projeto
```
wine-analysis/
│
├── dataset-wine.csv              # Dataset principal (~130k vinhos)
├── analise_vinhos.py             # Script principal de análise
│
├── export/                       # Gráficos PNG gerados
│   ├── dash_01_paises.png
│   ├── dash_02_preco_pontos.png
│   ├── distribuicao_regioes_top3_disparidade.png
│   ├── matriz_valor_variedades.png
│   ├── top10_custo_beneficio.png
│   └── faixas_preco_qualidade_violino.png
│
├── export_excel/                 # Dados exportados em Excel
│   ├── 01_top_paises_quantidade.xlsx
│   ├── 04_correlacao_preco_pontos.xlsx
│   ├── 21_regioes_disparidade.xlsx
│   ├── 23_matriz_valor_variedades.xlsx
│   ├── 24_top10_custo_beneficio.xlsx
│   └── 25_faixas_preco_qualidade.xlsx
│
└── README.md                     # Este arquivo
```

## 🛠️ Tecnologias e Dependências

### Requisitos do Sistema
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Bibliotecas Necessárias
```python
pandas>=1.3.0          # Manipulação e análise de dados
numpy>=1.21.0          # Computação numérica
matplotlib>=3.4.0      # Visualização de dados (gráficos)
seaborn>=0.11.0        # Visualização estatística avançada
scipy>=1.7.0           # Testes estatísticos (ANOVA)
openpyxl>=3.0.0        # Leitura/escrita de arquivos Excel
pathlib                # Manipulação de caminhos (built-in)
```

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/wine-analysis.git
cd wine-analysis
```

### 2. Crie um ambiente virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

**OU instale manualmente:**
```bash
pip install pandas numpy matplotlib seaborn scipy openpyxl
```

### 4. Execute o script
```bash
python analise_vinhos.py
```

### 5. Resultados

Após a execução, você encontrará:
- **Gráficos PNG** na pasta `/export/`
- **Dados em Excel** na pasta `/export_excel/`
- **Resumo estatístico** no terminal

## 📋 requirements.txt

Crie um arquivo `requirements.txt` com:
```txt
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
openpyxl>=3.0.0
```

## 📊 Dataset

### Fonte dos Dados
Dataset de vinhos contendo avaliações de críticos especializados.

### Estrutura do Dataset (14 colunas):

| Coluna | Tipo | Descrição | Valores Não-Nulos |
|--------|------|-----------|-------------------|
| `country` | object | País de origem | 129.908 |
| `points` | int64 | Pontuação (0-100) | 129.971 |
| `price` | float64 | Preço em USD | 120.975 |
| `variety` | object | Variedade da uva | 129.970 |
| `region_1` | object | Região vinícola | 108.724 |
| `title` | object | Nome do vinho | 129.971 |
| `description` | object | Descrição do crítico | 129.971 |
| `designation` | object | Vinhedo/denominação | 92.506 |
| `province` | object | Província/estado | 129.908 |
| `taster_name` | object | Nome do degustador | 103.727 |
| `winery` | object | Nome da vinícola | 129.971 |

**Total:** 129.971 vinhos

## 🎨 Principais Visualizações

### 1. Dashboard de Países
Análise consolidada mostrando:
- Quantidade de vinhos por país
- Pontuação média por país
- Relação preço vs qualidade
- Variação de preços

### 2. Matriz de Valor (Scatter Plot)
Visualização interativa de variedades:
- Eixo X: Preço médio
- Eixo Y: Pontuação média
- Tamanho das bolhas: Quantidade de vinhos
- Identifica quadrantes: Alto Valor, Premium, Econômico, Baixo Valor

### 3. Distribuição Regional (Boxplot)
Mostra variabilidade de qualidade nas principais regiões vinícolas, ordenado por mediana.

### 4. Faixas de Preço (Violinplot)
Revela como qualidade se distribui em 6 faixas de preço:
- <$15, $15-30, $30-50, $50-100, $100-200, >$200

### 5. Top 10 Custo-Benefício
Lista vinhos com maior score (pontos/preço), filtrados por:
- Preço > $5
- Pontos ≥ 85

### ✅ Descobertas Chave:

1. **Correlação Preço-Qualidade:** Existe correlação positiva, mas com retornos decrescentes após $50-100
2. **Melhor Custo-Benefício:** Vinhos de $6-8 pontuando 87-90 oferecem máximo retorno
3. **Diversidade Geográfica:** Custo-benefício excepcional não se limita a regiões específicas
4. **Variedades Populares:** Pinot Noir e Chardonnay dominam em volume, mas não necessariamente em qualidade/preço
5. **Sweet Spot:** Faixa $30-50 oferece melhor equilíbrio entre qualidade consistente e preço razoável

## 👤 Autor

**Lucas Santos Freitas**
- GitHub: [[@Lukketes](github.com/Lukketes)
- LinkedIn: [Lucas Freitas](https://linkedin.com/in/lucas-freitas-592180329/)

🍷 **Happy Wine Analysis!**
