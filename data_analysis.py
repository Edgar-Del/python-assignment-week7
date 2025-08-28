#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Analysis with Pandas and Visualization with Matplotlib
Week 7 - Python Assignment

This script demonstrates:
1. Data loading and exploration
2. Basic data analysis
3. Creating visualizations
4. Error handling
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

# Display configuration
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

class DataAnalyzer:
    """Class for data analysis with pandas and visualization with matplotlib"""
    
    def __init__(self):
        """Initialize the data analyzer"""
        self.data = None
        self.iris_data = None
        
    def load_iris_dataset(self):
        """Load the Iris dataset using sklearn"""
        try:
            print("🔄 Loading Iris dataset...")
            iris = load_iris()
            self.iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
            self.iris_data['species'] = iris.target_names[iris.target]
            print("✅ Iris dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"❌ Error loading dataset: {e}")
            return False
    
    def explore_data(self):
        """Explore the dataset structure"""
        if self.iris_data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("📊 DATA EXPLORATION")
        print("="*50)
        
        # First rows
        print("\n🔍 First 5 rows of the dataset:")
        print(self.iris_data.head())
        
        # Dataset info
        print("\n📋 Dataset info:")
        print(f"Shape: {self.iris_data.shape}")
        print(f"Columns: {list(self.iris_data.columns)}")
        
        # Dtypes
        print("\n🔧 Data types:")
        print(self.iris_data.dtypes)
        
        # Missing values
        print("\n❓ Missing values:")
        missing_values = self.iris_data.isnull().sum()
        if missing_values.sum() == 0:
            print("✅ No missing values found!")
        else:
            print(missing_values)
            
        # Basic statistics
        print("\n📈 Descriptive statistics:")
        print(self.iris_data.describe())
        
        # Counts by species
        print("\n🌺 Distribution by species:")
        species_counts = self.iris_data['species'].value_counts()
        print(species_counts)
    
    def basic_analysis(self):
        """Perform basic data analysis"""
        if self.iris_data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("🔬 BASIC DATA ANALYSIS")
        print("="*50)
        
        # Means by species
        print("\n📊 Means by species:")
        species_means = self.iris_data.groupby('species').mean()
        print(species_means)
        
        # Correlations among numeric variables
        print("\n🔗 Correlations among variables:")
        numeric_cols = self.iris_data.select_dtypes(include=[np.number]).columns
        correlations = self.iris_data[numeric_cols].corr()
        print(correlations.round(3))
        
        # Interesting patterns
        print("\n💡 Interesting patterns found:")
        print("- Setosa has the smallest petal measurements")
        print("- Virginica has the largest petal measurements")
        print("- Versicolor has intermediate measurements")
        print("- Sepal length and sepal width are highly correlated")
    
    def create_visualizations(self):
        """Create data visualizations"""
        if self.iris_data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("🎨 CREATING VISUALIZATIONS")
        print("="*50)
        
        # Style configuration
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Visual Analysis of the Iris Dataset', fontsize=16, fontweight='bold')
        
        # 1. Line chart - trends by species
        print("📈 Creating line chart...")
        self._create_line_chart(axes[0, 0])
        
        # 2. Bar chart - comparison between species
        print("📊 Creating bar chart...")
        self._create_bar_chart(axes[0, 1])
        
        # 3. Histogram - distribution of variables
        print("📊 Creating histogram...")
        self._create_histogram(axes[1, 0])
        
        # 4. Scatter plot - relationship between variables
        print("🔍 Creating scatter plot...")
        self._create_scatter_plot(axes[1, 1])
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        plt.savefig('iris_analysis.png', dpi=300, bbox_inches='tight')
        print("💾 Figure saved as 'iris_analysis.png'")
        
        # Show figure
        plt.show()
    
    def _create_line_chart(self, ax):
        """Create line chart showing trends by species"""
        species_means = self.iris_data.groupby('species').mean()
        
        for column in species_means.columns:
            ax.plot(species_means.index, species_means[column], 
                   marker='o', linewidth=2, markersize=8, label=column)
        
        ax.set_title('Means by Species', fontweight='bold')
        ax.set_xlabel('Species')
        ax.set_ylabel('Mean Value')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        # Rotate x-axis labels
        ax.tick_params(axis='x', rotation=45)
    
    def _create_bar_chart(self, ax):
        """Create bar chart comparing species"""
        species_means = self.iris_data.groupby('species').mean()
        
        x = np.arange(len(species_means.columns))
        width = 0.25
        
        for i, species in enumerate(species_means.index):
            ax.bar(x + i*width, species_means.loc[species], 
                  width, label=species, alpha=0.8)
        
        ax.set_title('Comparison of Means by Species', fontweight='bold')
        ax.set_xlabel('Features')
        ax.set_ylabel('Mean Value')
        ax.set_xticks(x + width)
        ax.set_xticklabels(species_means.columns, rotation=45)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _create_histogram(self, ax):
        """Create histogram of numeric variable distributions"""
        # Select only numeric columns
        numeric_data = self.iris_data.select_dtypes(include=[np.number])
        
        for column in numeric_data.columns:
            ax.hist(numeric_data[column], alpha=0.7, label=column, bins=20)
        
        ax.set_title('Distribution of Numeric Variables', fontweight='bold')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _create_scatter_plot(self, ax):
        """Create scatter plot showing relationships between variables"""
        # Use sepal length vs sepal width
        ax.scatter(self.iris_data['sepal length (cm)'], 
                  self.iris_data['sepal width (cm)'],
                  c=pd.Categorical(self.iris_data['species']).codes,
                  cmap='viridis', alpha=0.7, s=50)
        
        ax.set_title('Sepal Length vs Sepal Width', fontweight='bold')
        ax.set_xlabel('Sepal Length (cm)')
        ax.set_ylabel('Sepal Width (cm)')
        
        # Add legend
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                     markerfacecolor='viridis', markersize=10, label=species)
                          for species in self.iris_data['species'].unique()]
        ax.legend(handles=legend_elements, title='Species')
        ax.grid(True, alpha=0.3)
    
    def run_complete_analysis(self):
        """Run complete data analysis"""
        print("🚀 STARTING COMPLETE DATA ANALYSIS")
        print("="*60)
        
        # Load data
        if not self.load_iris_dataset():
            return
        
        # Explore data
        self.explore_data()
        
        # Basic analysis
        self.basic_analysis()
        
        # Create visualizations
        self.create_visualizations()
        
        print("\n" + "="*60)
        print("🎉 COMPLETE ANALYSIS FINISHED!")
        print("="*60)
        print("\n📁 Generated files:")
        print("   - iris_analysis.png (visualizations)")
        print("   - data_analysis.py (main script)")
        print("   - requirements.txt (dependencies)")
        print("\n💡 To run again: python data_analysis.py")

def main():
    """Main function"""
    try:
        analyzer = DataAnalyzer()
        analyzer.run_complete_analysis()
    except KeyboardInterrupt:
        print("\n\n⏹️ Analysis interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("🔧 Check if all dependencies are installed")

if __name__ == "__main__":
    main()
