# 🌸 Data Analysis with Pandas and Visualization with Matplotlib

**Week 7 - Python Assignment**

This project demonstrates a complete data analysis using the Pandas and Matplotlib libraries in Python, implementing all tasks requested in the assignment.

## 📋 Assignment Objectives

✅ **Load and analyze a dataset** using the pandas library in Python  
✅ **Create simple charts and visualizations** with the matplotlib library  
✅ **Demonstrate exploratory data analysis techniques**  
✅ **Implement error handling** with try-except mechanisms  

## 🚀 Implemented Features

### Task 1: Dataset Loading and Exploration
- ✅ Loading the Iris dataset using sklearn
- ✅ Displaying the first rows with `.head()`
- ✅ Exploring the dataset structure
- ✅ Checking data types and missing values
- ✅ Data cleaning (concept demonstration)

### Task 2: Basic Data Analysis
- ✅ Computing basic statistics with `.describe()`
- ✅ Grouping by species and computing means
- ✅ Correlations analysis among variables
- ✅ Identifying interesting patterns in the data

### Task 3: Data Visualization
- ✅ **Line Chart**: Trends of means by species
- ✅ **Bar Chart**: Comparison between species
- ✅ **Histogram**: Distribution of numeric variables
- ✅ **Scatter Plot**: Relationships between variables

## 📁 Project Structure

```
python-assignment-week7/
├── data_analysis.py          # Main Python script
├── data_analysis.ipynb       # Jupyter Notebook
├── requirements.txt          # Project dependencies
├── README.md                 # This file
└── iris_analysis.png         # Generated visualizations (after running)
```

## 🛠️ Installation and Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Python Script
```bash
python data_analysis.py
```

### 3. Run the Jupyter Notebook
```bash
jupyter notebook data_analysis.ipynb
```

## 📊 Dataset Used

**Iris Dataset** - A classic classification dataset that contains:
- **150 samples** of iris flowers
- **3 species**: setosa, versicolor, virginica
- **4 features**: sepal and petal length and width
- **No missing values** - ideal for demonstration

## 🔍 Key Findings

### Analysis by Species
- **Setosa**: Most distinct species with smaller petals
- **Virginica**: Largest petal measurements
- **Versicolor**: Intermediate measurements

### Important Correlations
- Petal length vs petal width: **0.963** (very high)
- Sepal length vs sepal width: **0.746** (high)
- Moderate correlation between sepal and petal

### Data Distribution
- Balanced dataset (50 samples per species)
- Approximately normal distributions
- Well-separated species

## 🎨 Visualizations Created

### 1. Line Chart
- Shows trends of means by species
- Enables easy comparison of features across species

### 2. Bar Chart
- Compares means across species
- Clear visualization of numerical differences

### 3. Histogram
- Distribution of numeric variables
- Helps understand the shape of the data

### 4. Scatter Plot
- Relationships between different variables
- Shows natural clusters by species

## 💻 Code and Structure

### Main Class: `DataAnalyzer`
```python
class DataAnalyzer:
    def __init__(self)
    def load_iris_dataset(self)
    def explore_data(self)
    def basic_analysis(self)
    def create_visualizations(self)
    def run_complete_analysis(self)
```

### Error Handling
- ✅ Try-except for data loading
- ✅ Validation for loaded data
- ✅ Informative error messages
- ✅ Graceful handling of interruptions

### Chart Customization
- ✅ Titles and axis labels in English
- ✅ Consistent and appealing colors
- ✅ Clear and informative legends
- ✅ Grid and professional formatting

## 🚀 How to Run

### Option 1: Python Script
```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
python data_analysis.py
```

### Option 2: Jupyter Notebook
```bash
# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook

# Open data_analysis.ipynb
```

## 📈 Outputs

After running, the project generates:
- **Complete analysis in the terminal** with statistics and findings
- **Image file** `iris_analysis.png` with all visualizations
- **Detailed report** of identified patterns and correlations

## 🔧 Customization

The code is easily adaptable to other datasets:
- Modify `load_iris_dataset()` to load your own CSV
- Adjust the visualizations to your specific variables
- Customize colors, styles, and formatting

## 📚 Libraries Used

- **pandas**: Data manipulation and analysis
- **matplotlib**: Charts and visualizations
- **seaborn**: Styles and color palettes
- **numpy**: Numerical operations
- **scikit-learn**: Loading the Iris dataset

## 🎯 Conclusion

This project successfully demonstrates:
- ✅ Efficient data loading and exploration
- ✅ Comprehensive statistical analysis
- ✅ Creation of informative and attractive visualizations
- ✅ Well-structured and documented code
- ✅ Robust error handling
- ✅ Implementation of all requested tasks

The Iris dataset is a perfect example to demonstrate exploratory data analysis and visualization techniques, showing how different species can be distinguished based on their morphological features.

---

**👨‍💻 Developed for Week 7 - Python Assignment**  
**📅 Date**: December 2024  
**🔧 Technologies**: Python, Pandas, Matplotlib, Seaborn
