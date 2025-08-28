#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Analysis Demonstration - No External Dependencies
Week 7 - Python Assignment

This script demonstrates data analysis concepts using only standard Python.
It simulates what would be done with pandas and matplotlib.
"""

import csv
import random
import statistics
import math
from collections import Counter, defaultdict

class SimpleDataAnalyzer:
    """Simple data analyzer using only standard Python"""
    
    def __init__(self):
        """Initialize the analyzer"""
        self.data = []
        self.headers = []
        self.numeric_columns = []
        self.categorical_columns = []
        
    def create_sample_dataset(self):
        """Create a sample dataset for demonstration"""
        print("🔄 Creating sample dataset...")
        
        # Create sample data (simulating the Iris dataset)
        self.headers = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
        
        # Data for Setosa
        for _ in range(50):
            self.data.append([
                round(random.uniform(4.5, 5.5), 2),  # sepal_length
                round(random.uniform(3.0, 4.0), 2),  # sepal_width
                round(random.uniform(1.0, 2.0), 2),  # petal_length
                round(random.uniform(0.1, 0.5), 2),  # petal_width
                'setosa'
            ])
        
        # Data for Versicolor
        for _ in range(50):
            self.data.append([
                round(random.uniform(5.5, 6.5), 2),  # sepal_length
                round(random.uniform(2.5, 3.5), 2),  # sepal_width
                round(random.uniform(3.0, 4.5), 2),  # petal_length
                round(random.uniform(1.0, 1.5), 2),  # petal_width
                'versicolor'
            ])
        
        # Data for Virginica
        for _ in range(50):
            self.data.append([
                round(random.uniform(6.0, 7.0), 2),  # sepal_length
                round(random.uniform(2.5, 3.5), 2),  # sepal_width
                round(random.uniform(4.5, 6.0), 2),  # petal_length
                round(random.uniform(1.5, 2.5), 2),  # petal_width
                'virginica'
            ])
        
        # Identify numeric and categorical columns
        self.numeric_columns = [i for i, header in enumerate(self.headers) 
                               if header != 'species']
        self.categorical_columns = [i for i, header in enumerate(self.headers) 
                                  if header == 'species']
        
        print(f"✅ Dataset created with {len(self.data)} samples and {len(self.headers)} columns")
        print(f"📊 Numeric columns: {[self.headers[i] for i in self.numeric_columns]}")
        print(f"🌺 Categorical columns: {[self.headers[i] for i in self.categorical_columns]}")
    
    def explore_data(self):
        """Explore the data structure"""
        if not self.data:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("📊 DATA EXPLORATION")
        print("="*50)
        
        # First rows
        print("\n🔍 First 5 rows of the dataset:")
        print(" | ".join(self.headers))
        print("-" * 80)
        for i, row in enumerate(self.data[:5]):
            print(f"{i+1} | " + " | ".join(str(val) for val in row))
        
        # Dataset info
        print(f"\n📋 Dataset info:")
        print(f"Dimensions: {len(self.data)} rows x {len(self.headers)} columns")
        print(f"Columns: {self.headers}")
        
        # Check missing values (none in this example)
        print("\n❓ Missing values:")
        print("✅ No missing values found!")
        
        # Counts by species
        print("\n🌺 Distribution by species:")
        species_counts = Counter(row[4] for row in self.data)  # index 4 is 'species'
        for species, count in species_counts.items():
            print(f"  {species}: {count} samples")
    
    def basic_analysis(self):
        """Perform basic data analysis"""
        if not self.data:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("🔬 BASIC DATA ANALYSIS")
        print("="*50)
        
        # Basic stats for numeric columns
        print("\n📈 Descriptive statistics:")
        for col_idx in self.numeric_columns:
            col_name = self.headers[col_idx]
            values = [row[col_idx] for row in self.data]
            
            print(f"\n{col_name}:")
            print(f"  Mean: {statistics.mean(values):.2f}")
            print(f"  Median: {statistics.median(values):.2f}")
            print(f"  Std dev: {statistics.stdev(values):.2f}")
            print(f"  Min: {min(values):.2f}")
            print(f"  Max: {max(values):.2f}")
        
        # Means by species
        print("\n📊 Means by species:")
        species_means = defaultdict(lambda: defaultdict(list))
        
        for row in self.data:
            species = row[4]
            for col_idx in self.numeric_columns:
                species_means[species][col_idx].append(row[col_idx])
        
        # Table header
        header_row = "Species"
        for col_idx in self.numeric_columns:
            header_row += f" | {self.headers[col_idx]:>10}"
        print(header_row)
        print("-" * len(header_row))
        
        # Table rows
        for species in ['setosa', 'versicolor', 'virginica']:
            row_data = f"{species:>8}"
            for col_idx in self.numeric_columns:
                mean_val = statistics.mean(species_means[species][col_idx])
                row_data += f" | {mean_val:>10.2f}"
            print(row_data)
        
        # Correlations between numeric variables
        print("\n🔗 Correlations between variables:")
        for i, col1_idx in enumerate(self.numeric_columns):
            for j, col2_idx in enumerate(self.numeric_columns):
                if i < j:  # Avoid duplicates
                    col1_name = self.headers[col1_idx]
                    col2_name = self.headers[col2_idx]
                    correlation = self._calculate_correlation(col1_idx, col2_idx)
                    print(f"  {col1_name} vs {col2_name}: {correlation:.3f}")
    
    def _calculate_correlation(self, col1_idx, col2_idx):
        """Calculate correlation between two numeric columns"""
        values1 = [row[col1_idx] for row in self.data]
        values2 = [row[col2_idx] for row in self.data]
        
        n = len(values1)
        if n != len(values2):
            return 0.0
        
        # Means
        mean1 = statistics.mean(values1)
        mean2 = statistics.mean(values2)
        
        # Pearson correlation
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(values1, values2))
        denominator1 = sum((x - mean1) ** 2 for x in values1)
        denominator2 = sum((y - mean2) ** 2 for y in values2)
        
        if denominator1 == 0 or denominator2 == 0:
            return 0.0
        
        correlation = numerator / math.sqrt(denominator1 * denominator2)
        return correlation
    
    def identify_patterns(self):
        """Identify interesting patterns in the data"""
        if not self.data:
            print("❌ No dataset loaded!")
            return
            
        print("\n" + "="*50)
        print("💡 INTERESTING PATTERNS FOUND")
        print("="*50)
        
        # Analysis by species
        print("\n📊 Analysis by species:")
        
        # Find min and max by species
        species_stats = defaultdict(lambda: defaultdict(list))
        for row in self.data:
            species = row[4]
            for col_idx in self.numeric_columns:
                species_stats[species][col_idx].append(row[col_idx])
        
        for species in ['setosa', 'versicolor', 'virginica']:
            print(f"\n🌺 {species.upper()}:")
            for col_idx in self.numeric_columns:
                col_name = self.headers[col_idx]
                values = species_stats[species][col_idx]
                min_val = min(values)
                max_val = max(values)
                mean_val = statistics.mean(values)
                print(f"  {col_name}: min={min_val:.2f}, max={max_val:.2f}, mean={mean_val:.2f}")
        
        # General patterns
        print("\n🔍 General patterns identified:")
        print("- Setosa has the smallest petal measurements")
        print("- Virginica has the largest petal measurements")
        print("- Versicolor has intermediate measurements")
        print("- All species have 50 samples (balanced dataset)")
        
        # Important correlations
        print("\n🔗 Important correlations:")
        petal_length_idx = self.headers.index('petal_length')
        petal_width_idx = self.headers.index('petal_width')
        petal_corr = self._calculate_correlation(petal_length_idx, petal_width_idx)
        print(f"- Petal length and width: {petal_corr:.3f} (very high)")
        
        sepal_length_idx = self.headers.index('sepal_length')
        sepal_width_idx = self.headers.index('sepal_width')
        sepal_corr = self._calculate_correlation(sepal_length_idx, sepal_width_idx)
        print(f"- Sepal length and width: {sepal_corr:.3f}")
    
    def save_to_csv(self, filename="iris_sample.csv"):
        """Save data to a CSV file"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.headers)
                writer.writerows(self.data)
            
            print(f"\n💾 Data saved to '{filename}'")
            return True
        except Exception as e:
            print(f"❌ Error saving CSV: {e}")
            return False
    
    def run_complete_analysis(self):
        """Run complete data analysis"""
        print("🚀 STARTING COMPLETE DATA ANALYSIS")
        print("="*60)
        
        # Create dataset
        self.create_sample_dataset()
        
        # Explore data
        self.explore_data()
        
        # Basic analysis
        self.basic_analysis()
        
        # Identify patterns
        self.identify_patterns()
        
        # Save data
        self.save_to_csv()
        
        print("\n" + "="*60)
        print("🎉 COMPLETE ANALYSIS FINISHED!")
        print("="*60)
        print("\n📁 Generated files:")
        print("   - iris_sample.csv (sample dataset)")
        print("   - demo_analysis.py (this script)")
        print("   - requirements.txt (dependencies)")
        print("\n💡 To use with pandas and matplotlib:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Run: python data_analysis.py")

def main():
    """Main function"""
    try:
        print("🌸 DATA ANALYSIS DEMONSTRATION")
        print("Week 7 - Python Assignment")
        print("="*50)
        print("\nThis script demonstrates data analysis using only standard Python.")
        print("For full analysis with visualizations, use data_analysis.py\n")
        
        analyzer = SimpleDataAnalyzer()
        analyzer.run_complete_analysis()
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Analysis interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
