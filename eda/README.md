### **Exploratory Data Analysis (EDA) Guide**

#### **1. Understanding the Data**
- **Questions:**
  - What does the dataset represent? (Domain, context, and purpose)
  - How many rows (observations) and columns (features) are there?
  - What are the data types of each column (numerical, categorical, datetime)?
  - Are there any missing values? How many, and in which columns?
  - What are the unique values and their frequencies in categorical columns?
  - Are there any duplicate rows or records?

#### **2. Data Cleaning**
- **Questions:**
  - Are there any duplicate rows? How should they be handled?
  - Are there outliers or extreme values? How should they be addressed?
  - Are there inconsistent or unexpected data entries (e.g., typos, mixed formats)?
  - Are columns meaningful? (e.g., no strings in numerical columns)
  - Should any columns be combined, split, or dropped?
  - Are there any irrelevant or redundant columns?

#### **3. Univariate Analysis**
- **Numerical Variables:**
  - What is the distribution of the data? (Normal, skewed, uniform)
  - What are the summary statistics? (Mean, median, mode, variance, standard deviation, range)
  - Are there any outliers or extreme values?
  - What are the min and max values?
- **Categorical Variables:**
  - How many unique categories are there?
  - What is the frequency distribution of each category?
  - Are there any imbalanced classes or rare categories?

#### **4. Bivariate Analysis**
- **Numerical vs Numerical:**
  - Is there a correlation between variables? (Use scatter plots, correlation matrix)
  - Are there any linear or non-linear relationships?
- **Numerical vs Categorical:**
  - Does the numerical feature vary across categories? (Use box plots, violin plots)
  - Are there significant differences between groups?
- **Categorical vs Categorical:**
  - What is the distribution of one category across another? (Use contingency tables, bar plots)
  - Are there any associations or dependencies? (Use chi-square tests)

#### **5. Multivariate Analysis**
- **Questions:**
  - How do multiple features interact with each other?
  - Is there any collinearity between features? (Use correlation heatmaps, VIF)
  - Does the target variable correlate with multiple features?
  - Are there any interaction effects between variables?

#### **6. Missing Data**
- **Questions:**
  - How many missing values are there per column?
  - Is the missing data random or systematic?
  - How should missing data be handled? (Imputation, removal, or flagging)
  - Are there patterns in the missing data that could provide insights?

#### **7. Feature Engineering**
- **Questions:**
  - Can new features be created from existing ones? (e.g., age from birthdate, day of the week from datetime)
  - Are there any derived features that could be useful? (e.g., ratios, aggregates)
  - Should any high-cardinality categorical features be grouped or encoded?
  - Can any features be dropped due to redundancy or irrelevance?

#### **8. Data Transformation**
- **Questions:**
  - Should numerical features be normalized or scaled? (e.g., standardization, min-max scaling)
  - Are there features that need transformations? (e.g., log transforms for skewed data)
  - Should categorical features be encoded? (e.g., one-hot encoding, label encoding)
  - Are there any datetime features that need to be broken down? (e.g., year, month, day)

#### **9. Target Variable (Supervised Learning)**
- **Questions:**
  - What is the distribution of the target variable? (Histogram, density plot)
  - Is the target variable imbalanced? (e.g., rare events in classification)
  - How does the target variable correlate with other features?
  - Are there any patterns or trends in the target variable over time (if applicable)?

#### **10. Outlier Detection**
- **Questions:**
  - Which features have outliers? (Use box plots, z-scores, IQR)
  - Are outliers data errors or valid extreme values?
  - Should outliers be removed, transformed, or capped?
  - How do outliers impact the analysis or modeling?

#### **11. Visualization**
- **Questions:**
  - What insights can be drawn from visualizations? (Histograms, scatter plots, pair plots, heatmaps)
  - Are there visual patterns or trends in the data?
  - How can relationships between features be effectively represented?
  - Are there any anomalies or unexpected patterns in the visualizations?

#### **12. Time-Based Analysis (For Time-Series Data)**
- **Questions:**
  - Are there trends, patterns, or seasonality in the data? (Use line plots, decomposition)
  - How does the target variable change over time?
  - Are there any anomalies or shifts in the data? (Use rolling statistics, anomaly detection)
  - Are there lagged relationships or autocorrelations? (Use ACF, PACF plots)

#### **13. Domain-Specific Insights**
- **Questions:**
  - Are there domain-specific features or relationships to explore?
  - Are there known patterns or hypotheses in the domain that can be validated?
  - Are there external factors or datasets that could enhance the analysis?

#### **14. Hypothesis Generation**
- **Questions:**
  - What hypotheses can be formed based on the data?
  - What relationships or patterns might exist that could be tested?
  - What questions can be answered with this data?

#### **15. Data Preparation for Modeling**
- **Questions:**
  - Is the data ready for modeling? (Clean, transformed, and feature-engineered)
  - Are there any additional preprocessing steps needed? (e.g., handling class imbalance)
  - Should the data be split into training, validation, and test sets?

---

### **EDA Workflow Example**
1. **Load the data and inspect the first few rows.**
2. **Check for missing values and decide how to handle them.**
3. **Generate summary statistics and visualize distributions.**
4. **Explore relationships between variables using correlation matrices and scatter plots.**
5. **Identify and handle outliers.**
6. **Perform feature engineering and transformations.**
7. **Formulate hypotheses based on initial findings.**
8. **Prepare the data for further analysis or modeling.**
