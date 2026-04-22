import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_excel("sales_data.xlsx")

print("Original Data:")
print(data)

data["Total"] = data["Quantity"] * data["Price"]

category_sales = data.groupby("Category")["Total"].sum()
print("\nCategory Sales:\n", category_sales)

top_customer = data.groupby("Customer_Name")["Total"].sum().idxmax()
print("\nTop Customer:", top_customer)

data.to_csv("final_report.csv", index=False)

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()
