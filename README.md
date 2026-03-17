# 📊 Sales Data Analysis Project

## 📌 Overview

This project focuses on analyzing sales data using **Python**, **Pandas**, and **Matplotlib**. It demonstrates how to perform **time series analysis**, **category-based comparisons**, and generate visual insights from raw data.

The project includes:

* Sales trends over time (monthly & quarterly)
* Category-wise comparison
* Share distribution visualization
* Exporting charts as PNG files
* Generating a brief summary of insights

---

## 🎯 Objectives

* Analyze sales performance over time
* Aggregate data monthly and quarterly
* Compare sales across categories
* Visualize data using different chart types
* Save charts and summarize key findings

---

## 📂 Project Structure

```
├── Sales_data.csv
├── analysis.py
├── line_chart.png
├── bar_chart.png
├── pie_chart.png
└── README.md
```

---

## 📈 Features

### 1. Time Series Analysis

* Plots sales trends over time
* Monthly aggregation using resampling
* (Optional) Quarterly aggregation for broader insights

### 2. Category Analysis

* Bar chart for comparing category sales
* Pie chart to show category share distribution

### 3. Data Visualization

* Line Chart → Sales trend over time
* Bar Chart → Category comparison
* Pie Chart → Percentage share

### 4. Export Outputs

* Charts are saved as:

  * `line_chart.png`
  * `bar_chart.png`
  * `pie_chart.png`

### 5. Summary Generation

* Displays key insights from data such as:

  * Highest selling category
  * Total sales
  * Trends over time

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas 📊
* Matplotlib 📉

---

## ▶️ How to Run the Project

1. Install required libraries:

```bash
pip install pandas matplotlib
```

2. Place your dataset:

* Ensure `Sales_data.csv` is in the same folder

3. Run the script:

```bash
python analysis.py
```

4. Output:

* Charts will be saved as PNG files
* Summary printed in the console

---

## 📊 Dataset Format

Your CSV file should contain:

```
Date,Sales,Category
2024-01-01,200,Electronics
2024-01-05,150,Clothing
2024-02-01,300,Furniture
```

---

## 📌 Chart Explanation

### 📉 Line Chart (Time Series)

* Best for showing trends over time
* X-axis: Date
* Y-axis: Sales
* Helps identify growth or decline patterns

### 📊 Bar Chart (Category Comparison)

* Used to compare sales between categories
* Easy to identify highest and lowest performers

### 🥧 Pie Chart (Share Distribution)

* Shows percentage contribution of each category
* Useful for understanding market share

---

## 🎨 Formatting & Design Choices

* Clear titles for each chart
* Proper axis labeling (Date, Sales, Category)
* Legends where necessary
* Clean layout using `tight_layout()`
* Readable percentage labels in pie chart

---

## 🚀 Future Improvements

* Add interactive dashboards (using Plotly/Power BI)
* Include filtering options
* Automate report generation (PDF/Excel)
* Add yearly trend comparison

---

## 📌 Conclusion

This project provides a simple yet powerful way to analyze sales data and visualize insights. It helps in understanding trends, category performance, and overall business growth.



⭐ If you like this project, don’t forget to star the repository!
