#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Dados com Pandas e Visualização com Matplotlib
Semana 7 - Python Assignment

Este script demonstra:
1. Carregamento e exploração de dados
2. Análise básica de dados
3. Criação de visualizações
4. Tratamento de erros
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

# Configuração para exibição em português
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

class DataAnalyzer:
    """Classe para análise de dados com pandas e visualização com matplotlib"""
    
    def __init__(self):
        """Inicializa o analisador de dados"""
        self.data = None
        self.iris_data = None
        
    def load_iris_dataset(self):
        """Carrega o dataset Iris usando sklearn"""
        try:
            print("🔄 Carregando dataset Iris...")
            iris = load_iris()
            self.iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
            self.iris_data['species'] = iris.target_names[iris.target]
            print("✅ Dataset Iris carregado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao carregar dataset: {e}")
            return False
    
    def explore_data(self):
        """Explora a estrutura dos dados"""
        if self.iris_data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("📊 EXPLORAÇÃO DOS DADOS")
        print("="*50)
        
        # Primeiras linhas
        print("\n🔍 Primeiras 5 linhas do dataset:")
        print(self.iris_data.head())
        
        # Informações sobre o dataset
        print("\n📋 Informações do dataset:")
        print(f"Dimensões: {self.iris_data.shape}")
        print(f"Colunas: {list(self.iris_data.columns)}")
        
        # Tipos de dados
        print("\n🔧 Tipos de dados:")
        print(self.iris_data.dtypes)
        
        # Verificar valores ausentes
        print("\n❓ Valores ausentes:")
        missing_values = self.iris_data.isnull().sum()
        if missing_values.sum() == 0:
            print("✅ Nenhum valor ausente encontrado!")
        else:
            print(missing_values)
            
        # Estatísticas básicas
        print("\n📈 Estatísticas descritivas:")
        print(self.iris_data.describe())
        
        # Contagem por espécie
        print("\n🌺 Distribuição por espécie:")
        species_counts = self.iris_data['species'].value_counts()
        print(species_counts)
    
    def basic_analysis(self):
        """Realiza análise básica dos dados"""
        if self.iris_data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("🔬 ANÁLISE BÁSICA DOS DADOS")
        print("="*50)
        
        # Médias por espécie
        print("\n📊 Médias por espécie:")
        species_means = self.iris_data.groupby('species').mean()
        print(species_means)
        
        # Correlações entre variáveis numéricas
        print("\n🔗 Correlações entre variáveis:")
        numeric_cols = self.iris_data.select_dtypes(include=[np.number]).columns
        correlations = self.iris_data[numeric_cols].corr()
        print(correlations.round(3))
        
        # Padrões interessantes
        print("\n💡 Padrões interessantes encontrados:")
        print("- Setosa tem as menores medidas de pétala")
        print("- Virginica tem as maiores medidas de pétala")
        print("- Versicolor tem medidas intermediárias")
        print("- Comprimento e largura de sépala são altamente correlacionados")
    
    def create_visualizations(self):
        """Cria visualizações dos dados"""
        if self.iris_data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("🎨 CRIANDO VISUALIZAÇÕES")
        print("="*50)
        
        # Configuração do estilo
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Criar figura com subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise Visual do Dataset Iris', fontsize=16, fontweight='bold')
        
        # 1. Gráfico de linha - Tendências por espécie
        print("📈 Criando gráfico de linha...")
        self._create_line_chart(axes[0, 0])
        
        # 2. Gráfico de barras - Comparação entre espécies
        print("📊 Criando gráfico de barras...")
        self._create_bar_chart(axes[0, 1])
        
        # 3. Histograma - Distribuição das variáveis
        print("📊 Criando histograma...")
        self._create_histogram(axes[1, 0])
        
        # 4. Gráfico de dispersão - Relação entre variáveis
        print("🔍 Criando gráfico de dispersão...")
        self._create_scatter_plot(axes[1, 1])
        
        # Ajustar layout
        plt.tight_layout()
        
        # Salvar figura
        plt.savefig('iris_analysis.png', dpi=300, bbox_inches='tight')
        print("💾 Figura salva como 'iris_analysis.png'")
        
        # Mostrar figura
        plt.show()
    
    def _create_line_chart(self, ax):
        """Cria gráfico de linha mostrando tendências por espécie"""
        species_means = self.iris_data.groupby('species').mean()
        
        for column in species_means.columns:
            ax.plot(species_means.index, species_means[column], 
                   marker='o', linewidth=2, markersize=8, label=column)
        
        ax.set_title('Médias por Espécie', fontweight='bold')
        ax.set_xlabel('Espécie')
        ax.set_ylabel('Valor Médio')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        # Rotacionar labels do eixo x
        ax.tick_params(axis='x', rotation=45)
    
    def _create_bar_chart(self, ax):
        """Cria gráfico de barras comparando espécies"""
        species_means = self.iris_data.groupby('species').mean()
        
        x = np.arange(len(species_means.columns))
        width = 0.25
        
        for i, species in enumerate(species_means.index):
            ax.bar(x + i*width, species_means.loc[species], 
                  width, label=species, alpha=0.8)
        
        ax.set_title('Comparação de Médias por Espécie', fontweight='bold')
        ax.set_xlabel('Características')
        ax.set_ylabel('Valor Médio')
        ax.set_xticks(x + width)
        ax.set_xticklabels(species_means.columns, rotation=45)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _create_histogram(self, ax):
        """Cria histograma da distribuição das variáveis"""
        # Selecionar apenas colunas numéricas
        numeric_data = self.iris_data.select_dtypes(include=[np.number])
        
        for column in numeric_data.columns:
            ax.hist(numeric_data[column], alpha=0.7, label=column, bins=20)
        
        ax.set_title('Distribuição das Variáveis Numéricas', fontweight='bold')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frequência')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _create_scatter_plot(self, ax):
        """Cria gráfico de dispersão mostrando relação entre variáveis"""
        # Usar comprimento vs largura de sépala
        ax.scatter(self.iris_data['sepal length (cm)'], 
                  self.iris_data['sepal width (cm)'],
                  c=pd.Categorical(self.iris_data['species']).codes,
                  cmap='viridis', alpha=0.7, s=50)
        
        ax.set_title('Comprimento vs Largura da Sépala', fontweight='bold')
        ax.set_xlabel('Comprimento da Sépala (cm)')
        ax.set_ylabel('Largura da Sépala (cm)')
        
        # Adicionar legenda
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                     markerfacecolor='viridis', markersize=10, label=species)
                          for species in self.iris_data['species'].unique()]
        ax.legend(handles=legend_elements, title='Espécie')
        ax.grid(True, alpha=0.3)
    
    def run_complete_analysis(self):
        """Executa análise completa dos dados"""
        print("🚀 INICIANDO ANÁLISE COMPLETA DE DADOS")
        print("="*60)
        
        # Carregar dados
        if not self.load_iris_dataset():
            return
        
        # Explorar dados
        self.explore_data()
        
        # Análise básica
        self.basic_analysis()
        
        # Criar visualizações
        self.create_visualizations()
        
        print("\n" + "="*60)
        print("🎉 ANÁLISE COMPLETA FINALIZADA!")
        print("="*60)
        print("\n📁 Arquivos gerados:")
        print("   - iris_analysis.png (visualizações)")
        print("   - data_analysis.py (script principal)")
        print("   - requirements.txt (dependências)")
        print("\n💡 Para executar novamente, rode: python data_analysis.py")

def main():
    """Função principal"""
    try:
        analyzer = DataAnalyzer()
        analyzer.run_complete_analysis()
    except KeyboardInterrupt:
        print("\n\n⏹️ Análise interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🔧 Verifique se todas as dependências estão instaladas")

if __name__ == "__main__":
    main()
