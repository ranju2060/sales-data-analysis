import pandas as pd
import matplotlib.pyplot as plt 

#Step 1: Load Excel File
data = pd.read_excel("sales_data.xlsx")

print("Original Data:")
print(data)

#Step 2: Create Total Column(Quantity x Price)
data["Total"] = data["Quantity"] * data["Price"]

#Step 3: Category wise sales
category_sales = data.groupby("Category")["Total"].sum()
print("\nCategory Sales:\n", category_sales)

# Step 4: Top customer
top_customer = data.groupby("Customer_Name")["Total"].sum().idxmax()
print("\nTop Customer:", top_customer)

# Step 5: Save new Excel file
data.to_csv("final_report.csv", index=False)

# Step 6: Create chart
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()