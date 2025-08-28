#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Additional Example: CSV Dataset Analysis
Demonstrates how to adapt the code to work with CSV files

This script shows:
1. How to load a CSV file
2. Error handling for files not found
3. Data analysis with missing values
4. Data cleaning
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

class CSVDataAnalyzer:
    """Class for CSV data analysis with error handling"""
    
    def __init__(self, csv_path):
        """Initialize the analyzer with the CSV file path"""
        self.csv_path = csv_path
        self.data = None
        self.original_shape = None
        
    def load_csv_data(self):
        """Load data from a CSV file with error handling"""
        try:
            print(f"🔄 Loading CSV file: {self.csv_path}")
            
            # Check if file exists
            if not os.path.exists(self.csv_path):
                raise FileNotFoundError(f"File not found: {self.csv_path}")
            
            # Load data
            self.data = pd.read_csv(self.csv_path)
            self.original_shape = self.data.shape
            
            print(f"✅ CSV loaded successfully!")
            print(f"📊 Original shape: {self.original_shape}")
            return True
            
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            print("💡 Check if the file path is correct")
            return False
            
        except pd.errors.EmptyDataError:
            print("❌ Error: CSV file is empty")
            return False
            
        except pd.errors.ParserError as e:
            print(f"❌ Parsing error: {e}")
            print("💡 Check if the file is a valid CSV")
            return False
            
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False
    
    def explore_data(self):
        """Explore the CSV data structure"""
        if self.data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("📊 CSV DATA EXPLORATION")
        print("="*50)
        
        # First rows
        print("\n🔍 First 5 rows of the dataset:")
        print(self.data.head())
        
        # Dataset info
        print("\n📋 Dataset info:")
        print(f"Shape: {self.data.shape}")
        print(f"Columns: {list(self.data.columns)}")
        
        # Data types
        print("\n🔧 Data types:")
        print(self.data.dtypes)
        
        # Missing values
        print("\n❓ Missing values:")
        missing_values = self.data.isnull().sum()
        total_missing = missing_values.sum()
        
        if total_missing == 0:
            print("✅ No missing values found!")
        else:
            print(f"⚠️ Total missing values: {total_missing}")
            print(missing_values)
            
            # Percentage of missing values
            missing_percentage = (total_missing / (self.data.shape[0] * self.data.shape[1])) * 100
            print(f"📊 Percentage of missing values: {missing_percentage:.2f}%")
    
    def clean_data(self):
        """Clean data by removing or filling missing values"""
        if self.data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("🧹 DATA CLEANING")
        print("="*50)
        
        # Check missing values again
        missing_values = self.data.isnull().sum()
        total_missing = missing_values.sum()
        
        if total_missing == 0:
            print("✅ Data is already clean!")
            return
        
        print(f"🔄 Starting cleaning of {total_missing} missing values...")
        
        # Cleaning strategy
        print("\n📋 Cleaning strategy:")
        print("1. Numeric columns: fill with mean")
        print("2. Categorical columns: fill with mode")
        print("3. Columns with too many missing values: drop rows")
        
        # Apply cleaning
        data_cleaned = self.data.copy()
        
        for column in data_cleaned.columns:
            if data_cleaned[column].isnull().sum() > 0:
                if data_cleaned[column].dtype in ['int64', 'float64']:
                    # Numeric column - fill with mean
                    mean_value = data_cleaned[column].mean()
                    data_cleaned[column].fillna(mean_value, inplace=True)
                    print(f"📊 Column '{column}': filled with mean ({mean_value:.2f})")
                else:
                    # Categorical column - fill with mode
                    mode_value = data_cleaned[column].mode()[0]
                    data_cleaned[column].fillna(mode_value, inplace=True)
                    print(f"📊 Column '{column}': filled with mode ('{mode_value}')")
        
        # Check if there are still missing values
        remaining_missing = data_cleaned.isnull().sum().sum()
        if remaining_missing == 0:
            print("✅ Cleaning completed successfully!")
            self.data = data_cleaned
        else:
            print(f"⚠️ There are still {remaining_missing} missing values")
    
    def basic_analysis(self):
        """Perform basic analysis of the cleaned data"""
        if self.data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("🔬 BASIC DATA ANALYSIS")
        print("="*50)
        
        # Basic statistics
        print("\n📈 Descriptive statistics:")
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            print(self.data[numeric_cols].describe())
        else:
            print("⚠️ No numeric columns found for statistical analysis")
        
        # Categorical columns analysis
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        
        if len(categorical_cols) > 0:
            print(f"\n📊 Categorical columns found: {list(categorical_cols)}")
            
            for col in categorical_cols:
                print(f"\n🌺 Distribution of column '{col}':")
                value_counts = self.data[col].value_counts()
                print(value_counts.head(10))  # Show top 10
                
                if len(value_counts) > 10:
                    print(f"... and {len(value_counts) - 10} more unique values")
    
    def create_simple_visualizations(self):
        """Create simple data visualizations"""
        if self.data is None:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("🎨 CREATING SIMPLE VISUALIZATIONS")
        print("="*50)
        
        # Style configuration
        plt.style.use('default')
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Visual Analysis of the CSV Dataset', fontsize=16, fontweight='bold')
        
        # 1. Histogram for numeric columns
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("📊 Creating histogram...")
            self._create_histogram(axes[0, 0], numeric_cols[0])
        else:
            axes[0, 0].text(0.5, 0.5, 'No numeric columns', 
                           ha='center', va='center', transform=axes[0, 0].transAxes)
            axes[0, 0].set_title('Histogram')
        
        # 2. Bar chart for categorical columns
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            print("📊 Creating bar chart...")
            self._create_bar_chart(axes[0, 1], categorical_cols[0])
        else:
            axes[0, 1].text(0.5, 0.5, 'No categorical columns', 
                           ha='center', va='center', transform=axes[0, 1].transAxes)
            axes[0, 1].set_title('Bar Chart')
        
        # 3. Box plot for numeric columns
        if len(numeric_cols) > 1:
            print("📊 Creating box plot...")
            self._create_box_plot(axes[1, 0], numeric_cols[:3])  # Primeiras 3 colunas
        else:
            axes[1, 0].text(0.5, 0.5, 'Not enough numeric columns for box plot', 
                           ha='center', va='center', transform=axes[1, 0].transAxes)
            axes[1, 0].set_title('Box Plot')
        
        # 4. Correlation matrix
        if len(numeric_cols) > 1:
            print("🔗 Creating correlation matrix...")
            self._create_correlation_matrix(axes[1, 1], numeric_cols)
        else:
            axes[1, 1].text(0.5, 0.5, 'Not enough numeric columns for correlation', 
                           ha='center', va='center', transform=axes[1, 1].transAxes)
            axes[1, 1].set_title('Correlation Matrix')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        plt.savefig('csv_analysis.png', dpi=300, bbox_inches='tight')
        print("💾 Figure saved as 'csv_analysis.png'")
        
        # Show figure
        plt.show()
    
    def _create_histogram(self, ax, column):
        """Create histogram for a numeric column"""
        ax.hist(self.data[column].dropna(), bins=20, alpha=0.7, edgecolor='black')
        ax.set_title(f'Distribution of {column}', fontweight='bold')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.grid(True, alpha=0.3)
    
    def _create_bar_chart(self, ax, column):
        """Create bar chart for a categorical column"""
        value_counts = self.data[column].value_counts().head(10)  # Top 10
        value_counts.plot(kind='bar', ax=ax, color='skyblue', alpha=0.8)
        ax.set_title(f'Top 10 Values - {column}', fontweight='bold')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3)
    
    def _create_box_plot(self, ax, columns):
        """Create box plot for multiple numeric columns"""
        data_to_plot = [self.data[col].dropna() for col in columns]
        ax.boxplot(data_to_plot, labels=columns)
        ax.set_title('Box Plot - Distribution per Column', fontweight='bold')
        ax.set_ylabel('Value')
        ax.grid(True, alpha=0.3)
    
    def _create_correlation_matrix(self, ax, columns):
        """Create correlation matrix"""
        correlation_matrix = self.data[columns].corr()
        im = ax.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
        
        # Add correlation values
        for i in range(len(columns)):
            for j in range(len(columns)):
                text = ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                              ha="center", va="center", color="black", fontweight='bold')
        
        ax.set_title('Correlation Matrix', fontweight='bold')
        ax.set_xticks(range(len(columns)))
        ax.set_yticks(range(len(columns)))
        ax.set_xticklabels(columns, rotation=45)
        ax.set_yticklabels(columns)
        
        # Add colorbar
        plt.colorbar(im, ax=ax)
    
    def run_analysis(self):
        """Run complete CSV data analysis"""
        print("🚀 STARTING CSV DATA ANALYSIS")
        print("="*60)
        
        # Load data
        if not self.load_csv_data():
            return
        
        # Explore data
        self.explore_data()
        
        # Clean data if needed
        if self.data.isnull().sum().sum() > 0:
            self.clean_data()
        
        # Basic analysis
        self.basic_analysis()
        
        # Create visualizations
        self.create_simple_visualizations()
        
        print("\n" + "="*60)
        print("🎉 COMPLETE CSV ANALYSIS FINISHED!")
        print("="*60)
        print(f"\n📊 Summary:")
        print(f"   - Original shape: {self.original_shape}")
        print(f"   - Final shape: {self.data.shape}")
        print(f"   - Numeric columns: {len(self.data.select_dtypes(include=[np.number]).columns)}")
        print(f"   - Categorical columns: {len(self.data.select_dtypes(include=['object']).columns)}")
        print(f"\n📁 Generated files:")
        print(f"   - csv_analysis.png (visualizations)")

def main():
    """Main function with usage example"""
    print("📁 CSV DATA ANALYSIS EXAMPLE")
    print("="*50)
    
    # Example 1: Try to load a file that does not exist
    print("\n🔍 Example 1: File not found")
    analyzer1 = CSVDataAnalyzer("non_existent_file.csv")
    analyzer1.run_analysis()
    
    # Example 2: Create a sample dataset and save as CSV
    print("\n\n🔍 Example 2: Creating sample dataset")
    
    # Create sample data
    np.random.seed(42)
    n_samples = 100
    
    example_data = pd.DataFrame({
        'age': np.random.randint(18, 80, n_samples),
        'height': np.random.normal(170, 10, n_samples),
        'weight': np.random.normal(70, 15, n_samples),
        'city': np.random.choice(['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'], n_samples),
        'profession': np.random.choice(['Engineer', 'Doctor', 'Teacher', 'Lawyer', 'Designer'], n_samples)
    })
    
    # Add some missing values
    example_data.loc[np.random.choice(n_samples, 10), 'age'] = np.nan
    example_data.loc[np.random.choice(n_samples, 15), 'height'] = np.nan
    example_data.loc[np.random.choice(n_samples, 8), 'city'] = np.nan
    
    # Save as CSV
    csv_filename = "sample_data.csv"
    example_data.to_csv(csv_filename, index=False)
    print(f"✅ Sample dataset saved as '{csv_filename}'")
    
    # Analyze the created dataset
    print(f"\n🔍 Analyzing '{csv_filename}'...")
    analyzer2 = CSVDataAnalyzer(csv_filename)
    analyzer2.run_analysis()
    
    # Clean up temporary file
    if os.path.exists(csv_filename):
        os.remove(csv_filename)
        print(f"\n🧹 Temporary file '{csv_filename}' removed")

if __name__ == "__main__":
    main()
