
# Adidas Sales Performance Analysis & Interactive Dashboard

## Overview

This project provides a comprehensive analysis of Adidas sales data, aiming to extract key insights into sales performance across different dimensions such as retailers, product categories, regions, and time. It showcases a typical data analysis workflow, including data loading, cleaning, aggregation, and visualization using Python's Pandas, Matplotlib, and Plotly libraries. Furthermore, an interactive dashboard built with **Streamlit** (`app.py`) is included for dynamic exploration of the findings, allowing users to interact with visualisations and filter data in real-time. The core data processing and static visualisations are documented within a **Jupyter Notebook** (`main.ipynb`).

## Key Questions / Objectives

* Analyze total sales performance by different retailers, visualising the contribution of each.
* Understand sales trends over time by tracking monthly sales figures.
* Examine the distribution of total sales and units sold across various states, using dual-axis charts for comparative insights.
* Explore sales breakdown hierarchically by region and city using interactive treemaps, allowing drill-down into geographical sales performance.
* Identify top-performing product categories and their impact on overall sales.
* Provide a user-friendly interactive dashboard to facilitate easy data exploration and insight discovery.

## Project Structure

| File Name            | Description                                                                                                                                                                                                   |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `main.ipynb`       | The primary Jupyter Notebook containing the step-by-step data loading, cleaning, aggregation, and initial visualisation using Pandas and Plotly. This is where the in-depth analytical process is documented. |
| `app.py`           | A Python script for the interactive Streamlit web application. This script reads the Adidas sales data and generates the dynamic dashboard visualisations.                                                    |
| `data/Adidas.xlsx` | The raw sales data in Excel format, which serves as the input for both the Jupyter Notebook and the Streamlit application.                                                                                    |
| `README.md`        | This README file provides an overview, setup instructions, and details about the project.                                                                                                                   |
| `images/logo.jpeg` | An image file specifically used within the Streamlit application (`app.py`) for branding or visual elements.                                                                                                |

## Technologies / Libraries Used

* Python 3.x
* **Pandas:** For efficient data loading, manipulation, and advanced analytical operations on tabular data.
* **NumPy:** For fundamental numerical computing (often used implicitly by Pandas).
* **Matplotlib:** For foundational plotting capabilities, though more complex interactive plots are handled by Plotly.
* **Plotly Express & Plotly Graph Objects:** Utilised extensively for creating rich, interactive, and visually appealing data visualisations such as bar charts, line charts, dual-axis charts, and treemaps.
* **Streamlit:** The framework used to transform the data analysis and visualisations into an interactive web application, making the insights accessible and explorable.
* **Openpyxl:** To enable Pandas to read and process `.xlsx` Excel files.

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone [https://github.com/juto-shogan/adidas-Analysis.git](https://github.com/juto-shogan/adidas-Analysis.git)
   cd adidas-Analysis
   ```
2. **Create a Virtual Environment (Recommended)**

   ```bash
   python -m venv venv
   # On Windows:
   # .\venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```
3. **Install Dependencies**

   Create a `requirements.txt` file in your project root with the following contents:

   ```
   pandas
   matplotlib
   plotly
   streamlit
   openpyxl
   ```

   Then install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Analysis & Dashboard

1. **Activate your virtual environment** (if created):

   * On Windows: `.\venv\Scripts\activate`
   * On macOS/Linux: `source venv/bin/activate`
2. **Explore the Jupyter Notebook (`main.ipynb`):**
   To delve into the detailed analysis process, data transformations, and the generation of individual plots:

   ```bash
   jupyter notebook main.ipynb
   ```

   This command will open the Jupyter Notebook in your default web browser, where you can execute cells sequentially to review and reproduce the data analysis steps.
3. **Run the Interactive Dashboard (`app.py`):**
   To launch the interactive Streamlit dashboard and explore the sales insights dynamically:

   ```bash
   streamlit run app.py
   ```

   This command will open the interactive dashboard in your default web browser, typically at `http://localhost:8501`.

## Findings / Insights

* **Retailer Performance:** The analysis identifies top-performing retailers by total sales, providing a precise understanding of which sales channels are most effective.
* **Temporal Sales Trends:** Monthly sales trends are visualised, revealing seasonal patterns, growth, or decline periods in Adidas sales over time.
* **Geographical Sales Distribution:** A combined visualisation of total sales and units sold by state allows for a nuanced comparison, highlighting areas with high revenue generation versus high product movement.
* **Regional and City-Level Sales Breakdown:** Interactive treemaps offer a hierarchical view of sales performance across different regions and cities, enabling drill-down into specific geographical areas for detailed insights.
* **[Add any other specific insights you gained, e.g., "Discovered a significant increase in online sales during specific promotional periods," "Identified a particular product line contributing disproportionately to profits." ]**

## Author

Somto Mbonu

Data Analyst
GitHub Profile: [juto-shogan](https://github.com/juto-shogan)
