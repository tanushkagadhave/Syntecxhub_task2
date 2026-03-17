import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load dataset safely
    df = pd.read_csv("Sales_data.csv", encoding='latin1')

    # Check required columns
    required_columns = ['Date', 'Sales', 'Category']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove invalid dates
    df = df.dropna(subset=['Date'])

    # Ensure Sales is numeric
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df = df.dropna(subset=['Sales'])

    # -------- Monthly Sales Trend --------
    monthly_sales = df.resample('ME', on='Date')['Sales'].sum()

    plt.figure()
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("line_chart.png")
    plt.close()

    # -------- Sales by Category --------
    category_sales = df.groupby('Category')['Sales'].sum()

    plt.figure()
    category_sales.plot(kind='bar')
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("bar_chart.png")
    plt.close()

    # -------- Category Share --------
    plt.figure()
    category_sales.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Category Share")
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("pie_chart.png")
    plt.close()

    print("All charts saved successfully!")

except FileNotFoundError:
    print("Error: Sales_data.csv file not found!")

except Exception as e:
    print("Error:", e)