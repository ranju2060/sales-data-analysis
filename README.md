# sales-data-analysis
Sales data analysis using Excel and Python, with SQL-based aggregation concepts

Sales Data Analysis Project

Overview
This project analyzes a sales dataset (`sales_data.xlsx`) to extract meaningful insights such as total sales by category and customer performance. The analysis is performed using Excel and Python (Pandas).

Dataset
The dataset contains the following columns:

- Customer_Name  
- Product  
- Category  
- Quantity  
- Price  
- Total  

Data Cleaning
- Removed duplicate and unnecessary columns  
- Fixed inconsistent data structure  
- Verified totals using Excel formulas  
- Ensured proper formatting of numeric values  

Analysis Performed

1. Category-wise Sales
- Electronics: 220,000  
- Fashion: 11,000  

2. Customer-wise Sales
- Ranju: 80,000  
- Sita: 62,000  
- Ram: 80,000  
- Amit: 6,000  
- Rita: 3,000  

Data Visualization
Created charts using Excel:

- Bar chart for category-wise sales  
- Bar chart for customer-wise sales  

(Screenshots are included in the repository)

Python Analysis
Used Pandas for data analysis:

```python
import pandas as pd

df = pd.read_excel("sales_data.xlsx")

category_sales = df.groupby("Category")["Total"].sum()
customer_sales = df.groupby("Customer_Name")["Total"].sum()

print(category_sales)
print(customer_sales)
```

SQL (Conceptual Understanding)
SQL was studied and understood for data aggregation and analysis purposes.

Example query:

```sql
SELECT Category, SUM(Total) AS Total_Sales
FROM sales_data
GROUP BY Category;
```

Key Insights
- Electronics category generated the highest revenue  
- Fashion category had significantly lower sales  
- Top customers: Ranju and Ram  
- Sales are concentrated in a few high-value transactions  

Tools Used
- Excel (Pivot Tables, Charts)  
- Python (Pandas, Matplotlib)  
- SQL (Conceptual knowledge for data analysis)  

Repository Contents
- `sales_data.xlsx` (dataset)  
- Screenshots of charts  
- Python analysis file (.py)  
- README.md  

Conclusion
This project demonstrates a basic data analysis workflow including data cleaning, aggregation, visualization, and insight generation using real-world tools.
