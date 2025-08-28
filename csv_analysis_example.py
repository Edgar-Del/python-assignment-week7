#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo Adicional: Análise de Dataset CSV
Demonstra como adaptar o código para trabalhar com arquivos CSV

Este script mostra:
1. Como carregar um arquivo CSV
2. Tratamento de erros para arquivos não encontrados
3. Análise de dados com valores ausentes
4. Limpeza de dados
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

class CSVDataAnalyzer:
    """Classe para análise de dados CSV com tratamento de erros"""
    
    def __init__(self, csv_path):
        """Inicializa o analisador com caminho do arquivo CSV"""
        self.csv_path = csv_path
        self.data = None
        self.original_shape = None
        
    def load_csv_data(self):
        """Carrega dados de um arquivo CSV com tratamento de erros"""
        try:
            print(f"🔄 Carregando arquivo CSV: {self.csv_path}")
            
            # Verificar se o arquivo existe
            if not os.path.exists(self.csv_path):
                raise FileNotFoundError(f"Arquivo não encontrado: {self.csv_path}")
            
            # Carregar dados
            self.data = pd.read_csv(self.csv_path)
            self.original_shape = self.data.shape
            
            print(f"✅ CSV carregado com sucesso!")
            print(f"📊 Dimensões originais: {self.original_shape}")
            return True
            
        except FileNotFoundError as e:
            print(f"❌ Erro: {e}")
            print("💡 Verifique se o caminho do arquivo está correto")
            return False
            
        except pd.errors.EmptyDataError:
            print("❌ Erro: Arquivo CSV está vazio")
            return False
            
        except pd.errors.ParserError as e:
            print(f"❌ Erro de parsing: {e}")
            print("💡 Verifique se o arquivo é um CSV válido")
            return False
            
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return False
    
    def explore_data(self):
        """Explora a estrutura dos dados CSV"""
        if self.data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("📊 EXPLORAÇÃO DOS DADOS CSV")
        print("="*50)
        
        # Primeiras linhas
        print("\n🔍 Primeiras 5 linhas do dataset:")
        print(self.data.head())
        
        # Informações sobre o dataset
        print("\n📋 Informações do dataset:")
        print(f"Dimensões: {self.data.shape}")
        print(f"Colunas: {list(self.data.columns)}")
        
        # Tipos de dados
        print("\n🔧 Tipos de dados:")
        print(self.data.dtypes)
        
        # Verificar valores ausentes
        print("\n❓ Valores ausentes:")
        missing_values = self.data.isnull().sum()
        total_missing = missing_values.sum()
        
        if total_missing == 0:
            print("✅ Nenhum valor ausente encontrado!")
        else:
            print(f"⚠️ Total de valores ausentes: {total_missing}")
            print(missing_values)
            
            # Porcentagem de valores ausentes
            missing_percentage = (total_missing / (self.data.shape[0] * self.data.shape[1])) * 100
            print(f"📊 Porcentagem de valores ausentes: {missing_percentage:.2f}%")
    
    def clean_data(self):
        """Limpa os dados removendo ou preenchendo valores ausentes"""
        if self.data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("🧹 LIMPEZA DOS DADOS")
        print("="*50)
        
        # Verificar valores ausentes novamente
        missing_values = self.data.isnull().sum()
        total_missing = missing_values.sum()
        
        if total_missing == 0:
            print("✅ Dados já estão limpos!")
            return
        
        print(f"🔄 Iniciando limpeza de {total_missing} valores ausentes...")
        
        # Estratégia de limpeza
        print("\n📋 Estratégia de limpeza:")
        print("1. Para colunas numéricas: preencher com média")
        print("2. Para colunas categóricas: preencher com moda")
        print("3. Para colunas com muitos valores ausentes: remover linhas")
        
        # Aplicar limpeza
        data_cleaned = self.data.copy()
        
        for column in data_cleaned.columns:
            if data_cleaned[column].isnull().sum() > 0:
                if data_cleaned[column].dtype in ['int64', 'float64']:
                    # Coluna numérica - preencher com média
                    mean_value = data_cleaned[column].mean()
                    data_cleaned[column].fillna(mean_value, inplace=True)
                    print(f"📊 Coluna '{column}': preenchida com média ({mean_value:.2f})")
                else:
                    # Coluna categórica - preencher com moda
                    mode_value = data_cleaned[column].mode()[0]
                    data_cleaned[column].fillna(mode_value, inplace=True)
                    print(f"📊 Coluna '{column}': preenchida com moda ('{mode_value}')")
        
        # Verificar se ainda há valores ausentes
        remaining_missing = data_cleaned.isnull().sum().sum()
        if remaining_missing == 0:
            print("✅ Limpeza concluída com sucesso!")
            self.data = data_cleaned
        else:
            print(f"⚠️ Ainda restam {remaining_missing} valores ausentes")
    
    def basic_analysis(self):
        """Realiza análise básica dos dados limpos"""
        if self.data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("🔬 ANÁLISE BÁSICA DOS DADOS")
        print("="*50)
        
        # Estatísticas básicas
        print("\n📈 Estatísticas descritivas:")
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            print(self.data[numeric_cols].describe())
        else:
            print("⚠️ Nenhuma coluna numérica encontrada para análise estatística")
        
        # Análise de colunas categóricas
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        
        if len(categorical_cols) > 0:
            print(f"\n📊 Colunas categóricas encontradas: {list(categorical_cols)}")
            
            for col in categorical_cols:
                print(f"\n🌺 Distribuição da coluna '{col}':")
                value_counts = self.data[col].value_counts()
                print(value_counts.head(10))  # Mostrar top 10
                
                if len(value_counts) > 10:
                    print(f"... e mais {len(value_counts) - 10} valores únicos")
    
    def create_simple_visualizations(self):
        """Cria visualizações simples dos dados"""
        if self.data is None:
            print("❌ Nenhum dataset carregado!")
            return
            
        print("\n" + "="*50)
        print("🎨 CRIANDO VISUALIZAÇÕES SIMPLES")
        print("="*50)
        
        # Configuração do estilo
        plt.style.use('default')
        
        # Criar figura com subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Análise Visual do Dataset CSV', fontsize=16, fontweight='bold')
        
        # 1. Histograma de colunas numéricas
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("📊 Criando histograma...")
            self._create_histogram(axes[0, 0], numeric_cols[0])
        else:
            axes[0, 0].text(0.5, 0.5, 'Nenhuma coluna numérica', 
                           ha='center', va='center', transform=axes[0, 0].transAxes)
            axes[0, 0].set_title('Histograma')
        
        # 2. Gráfico de barras para colunas categóricas
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            print("📊 Criando gráfico de barras...")
            self._create_bar_chart(axes[0, 1], categorical_cols[0])
        else:
            axes[0, 1].text(0.5, 0.5, 'Nenhuma coluna categórica', 
                           ha='center', va='center', transform=axes[0, 1].transAxes)
            axes[0, 1].set_title('Gráfico de Barras')
        
        # 3. Box plot para colunas numéricas
        if len(numeric_cols) > 1:
            print("📊 Criando box plot...")
            self._create_box_plot(axes[1, 0], numeric_cols[:3])  # Primeiras 3 colunas
        else:
            axes[1, 0].text(0.5, 0.5, 'Poucas colunas numéricas para box plot', 
                           ha='center', va='center', transform=axes[1, 0].transAxes)
            axes[1, 0].set_title('Box Plot')
        
        # 4. Matriz de correlação
        if len(numeric_cols) > 1:
            print("🔗 Criando matriz de correlação...")
            self._create_correlation_matrix(axes[1, 1], numeric_cols)
        else:
            axes[1, 1].text(0.5, 0.5, 'Poucas colunas numéricas para correlação', 
                           ha='center', va='center', transform=axes[1, 1].transAxes)
            axes[1, 1].set_title('Matriz de Correlação')
        
        # Ajustar layout
        plt.tight_layout()
        
        # Salvar figura
        plt.savefig('csv_analysis.png', dpi=300, bbox_inches='tight')
        print("💾 Figura salva como 'csv_analysis.png'")
        
        # Mostrar figura
        plt.show()
    
    def _create_histogram(self, ax, column):
        """Cria histograma para uma coluna numérica"""
        ax.hist(self.data[column].dropna(), bins=20, alpha=0.7, edgecolor='black')
        ax.set_title(f'Distribuição de {column}', fontweight='bold')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frequência')
        ax.grid(True, alpha=0.3)
    
    def _create_bar_chart(self, ax, column):
        """Cria gráfico de barras para uma coluna categórica"""
        value_counts = self.data[column].value_counts().head(10)  # Top 10
        value_counts.plot(kind='bar', ax=ax, color='skyblue', alpha=0.8)
        ax.set_title(f'Top 10 Valores - {column}', fontweight='bold')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frequência')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3)
    
    def _create_box_plot(self, ax, columns):
        """Cria box plot para múltiplas colunas numéricas"""
        data_to_plot = [self.data[col].dropna() for col in columns]
        ax.boxplot(data_to_plot, labels=columns)
        ax.set_title('Box Plot - Distribuição por Coluna', fontweight='bold')
        ax.set_ylabel('Valor')
        ax.grid(True, alpha=0.3)
    
    def _create_correlation_matrix(self, ax, columns):
        """Cria matriz de correlação"""
        correlation_matrix = self.data[columns].corr()
        im = ax.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
        
        # Adicionar valores de correlação
        for i in range(len(columns)):
            for j in range(len(columns)):
                text = ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                              ha="center", va="center", color="black", fontweight='bold')
        
        ax.set_title('Matriz de Correlação', fontweight='bold')
        ax.set_xticks(range(len(columns)))
        ax.set_yticks(range(len(columns)))
        ax.set_xticklabels(columns, rotation=45)
        ax.set_yticklabels(columns)
        
        # Adicionar barra de cores
        plt.colorbar(im, ax=ax)
    
    def run_analysis(self):
        """Executa análise completa dos dados CSV"""
        print("🚀 INICIANDO ANÁLISE DE DADOS CSV")
        print("="*60)
        
        # Carregar dados
        if not self.load_csv_data():
            return
        
        # Explorar dados
        self.explore_data()
        
        # Limpar dados se necessário
        if self.data.isnull().sum().sum() > 0:
            self.clean_data()
        
        # Análise básica
        self.basic_analysis()
        
        # Criar visualizações
        self.create_simple_visualizations()
        
        print("\n" + "="*60)
        print("🎉 ANÁLISE CSV COMPLETA FINALIZADA!")
        print("="*60)
        print(f"\n📊 Resumo:")
        print(f"   - Dimensões originais: {self.original_shape}")
        print(f"   - Dimensões finais: {self.data.shape}")
        print(f"   - Colunas numéricas: {len(self.data.select_dtypes(include=[np.number]).columns)}")
        print(f"   - Colunas categóricas: {len(self.data.select_dtypes(include=['object']).columns)}")
        print(f"\n📁 Arquivos gerados:")
        print(f"   - csv_analysis.png (visualizações)")

def main():
    """Função principal com exemplo de uso"""
    print("📁 EXEMPLO DE ANÁLISE DE DADOS CSV")
    print("="*50)
    
    # Exemplo 1: Tentar carregar um arquivo que não existe
    print("\n🔍 Exemplo 1: Arquivo não encontrado")
    analyzer1 = CSVDataAnalyzer("arquivo_inexistente.csv")
    analyzer1.run_analysis()
    
    # Exemplo 2: Criar um dataset de exemplo e salvar como CSV
    print("\n\n🔍 Exemplo 2: Criando dataset de exemplo")
    
    # Criar dados de exemplo
    np.random.seed(42)
    n_samples = 100
    
    example_data = pd.DataFrame({
        'idade': np.random.randint(18, 80, n_samples),
        'altura': np.random.normal(170, 10, n_samples),
        'peso': np.random.normal(70, 15, n_samples),
        'cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'], n_samples),
        'profissao': np.random.choice(['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Designer'], n_samples)
    })
    
    # Adicionar alguns valores ausentes
    example_data.loc[np.random.choice(n_samples, 10), 'idade'] = np.nan
    example_data.loc[np.random.choice(n_samples, 15), 'altura'] = np.nan
    example_data.loc[np.random.choice(n_samples, 8), 'cidade'] = np.nan
    
    # Salvar como CSV
    csv_filename = "exemplo_dados.csv"
    example_data.to_csv(csv_filename, index=False)
    print(f"✅ Dataset de exemplo salvo como '{csv_filename}'")
    
    # Analisar o dataset criado
    print(f"\n🔍 Analisando '{csv_filename}'...")
    analyzer2 = CSVDataAnalyzer(csv_filename)
    analyzer2.run_analysis()
    
    # Limpar arquivo temporário
    if os.path.exists(csv_filename):
        os.remove(csv_filename)
        print(f"\n🧹 Arquivo temporário '{csv_filename}' removido")

if __name__ == "__main__":
    main()
