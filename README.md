# 🌸 Análise de Dados com Pandas e Visualização com Matplotlib

**Semana 7 - Python Assignment**

Este projeto demonstra uma análise completa de dados usando as bibliotecas Pandas e Matplotlib em Python, implementando todas as tarefas solicitadas na atribuição.

## 📋 Objetivos da Atribuição

✅ **Carregar e analisar um dataset** usando a biblioteca pandas em Python  
✅ **Criar gráficos e visualizações simples** com a biblioteca matplotlib  
✅ **Demonstrar técnicas de análise exploratória de dados**  
✅ **Implementar tratamento de erros** com mecanismos try-except  

## 🚀 Funcionalidades Implementadas

### Tarefa 1: Carregamento e Exploração do Dataset
- ✅ Carregamento do dataset Iris usando sklearn
- ✅ Exibição das primeiras linhas com `.head()`
- ✅ Exploração da estrutura dos dados
- ✅ Verificação de tipos de dados e valores ausentes
- ✅ Limpeza de dados (demonstração conceitual)

### Tarefa 2: Análise Básica dos Dados
- ✅ Cálculo de estatísticas básicas com `.describe()`
- ✅ Agrupamento por espécie e cálculo de médias
- ✅ Análise de correlações entre variáveis
- ✅ Identificação de padrões interessantes nos dados

### Tarefa 3: Visualização dos Dados
- ✅ **Gráfico de Linha**: Tendências das médias por espécie
- ✅ **Gráfico de Barras**: Comparação entre espécies
- ✅ **Histograma**: Distribuição das variáveis numéricas
- ✅ **Gráfico de Dispersão**: Relações entre variáveis

## 📁 Estrutura do Projeto

```
python-assignment-week7/
├── data_analysis.py          # Script Python principal
├── data_analysis.ipynb       # Notebook Jupyter
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
└── iris_analysis.png        # Visualizações geradas (após execução)
```

## 🛠️ Instalação e Configuração

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o Script Python
```bash
python data_analysis.py
```

### 3. Executar o Notebook Jupyter
```bash
jupyter notebook data_analysis.ipynb
```

## 📊 Dataset Utilizado

**Dataset Iris** - Um clássico dataset de classificação que contém:
- **150 amostras** de flores iris
- **3 espécies**: setosa, versicolor, virginica
- **4 características**: comprimento e largura de sépala e pétala
- **Sem valores ausentes** - ideal para demonstração

## 🔍 Principais Descobertas

### Análise por Espécie
- **Setosa**: Espécie mais distinta, com pétalas menores
- **Virginica**: Maiores medidas de pétala
- **Versicolor**: Medidas intermediárias

### Correlações Importantes
- Comprimento e largura de pétala: **0.963** (muito alta)
- Comprimento e largura de sépala: **0.746** (alta)
- Correlação moderada entre sépala e pétala

### Distribuição dos Dados
- Dataset balanceado (50 amostras por espécie)
- Distribuições aproximadamente normais
- Espécies bem separáveis

## 🎨 Visualizações Criadas

### 1. Gráfico de Linha
- Mostra tendências das médias por espécie
- Permite comparar facilmente as características entre espécies

### 2. Gráfico de Barras
- Compara médias entre espécies
- Visualização clara das diferenças numéricas

### 3. Histograma
- Distribuição das variáveis numéricas
- Ajuda a entender a forma dos dados

### 4. Gráfico de Dispersão
- Relações entre diferentes variáveis
- Mostra clusters naturais por espécie

## 💻 Código e Estrutura

### Classe Principal: `DataAnalyzer`
```python
class DataAnalyzer:
    def __init__(self)
    def load_iris_dataset(self)
    def explore_data(self)
    def basic_analysis(self)
    def create_visualizations(self)
    def run_complete_analysis(self)
```

### Tratamento de Erros
- ✅ Try-except para carregamento de dados
- ✅ Verificação de dados válidos
- ✅ Mensagens de erro informativas
- ✅ Graceful handling de interrupções

### Customização de Gráficos
- ✅ Títulos e labels em português
- ✅ Cores atrativas e consistentes
- ✅ Legendas claras e informativas
- ✅ Grid e formatação profissional

## 🚀 Como Executar

### Opção 1: Script Python
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar análise
python data_analysis.py
```

### Opção 2: Notebook Jupyter
```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar Jupyter
jupyter notebook

# Abrir data_analysis.ipynb
```

## 📈 Saídas Geradas

Após a execução, o projeto gera:
- **Análise completa no terminal** com estatísticas e descobertas
- **Arquivo de imagem** `iris_analysis.png` com todas as visualizações
- **Relatório detalhado** de padrões e correlações encontradas

## 🔧 Personalização

O código é facilmente adaptável para outros datasets:
- Modifique `load_iris_dataset()` para carregar seu próprio CSV
- Ajuste as visualizações para suas variáveis específicas
- Personalize cores, estilos e formatação

## 📚 Bibliotecas Utilizadas

- **pandas**: Manipulação e análise de dados
- **matplotlib**: Criação de gráficos e visualizações
- **seaborn**: Estilos e paletas de cores
- **numpy**: Operações numéricas
- **scikit-learn**: Carregamento do dataset Iris

## 🎯 Conclusão

Este projeto demonstra com sucesso:
- ✅ Carregamento e exploração eficiente de dados
- ✅ Análise estatística abrangente
- ✅ Criação de visualizações informativas e atrativas
- ✅ Código bem estruturado e documentado
- ✅ Tratamento robusto de erros
- ✅ Implementação de todas as tarefas solicitadas

O dataset Iris serve como exemplo perfeito para demonstrar técnicas de análise exploratória de dados e visualização, mostrando como diferentes espécies podem ser distinguidas com base em suas características morfológicas.

---

**👨‍💻 Desenvolvido para a Semana 7 - Python Assignment**  
**📅 Data**: Dezembro 2024  
**🔧 Tecnologias**: Python, Pandas, Matplotlib, Seaborn
