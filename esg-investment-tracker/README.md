ESG Investment Tracker
 A dashboard to track and analyze ESG-linked investments using MSSQL, Python, and HTML. This project fetches data from an MSSQL database, generates a scatter plot of ESG scores vs. annual returns, and displays the results in a stylish offline dashboard.

 ## Project Structure
 ```
 esg-investment-tracker/
 ├── sql/
 │   ├── create_database.sql        # SQL script to create the database and table
 │   └── stored_procedures.sql      # SQL script to create stored procedures
 ├── src/
 │   └── esg_tracker.py             # Python script to generate the scatter plot
 ├── dashboard/
 │   ├── index.html                # Stylish dashboard HTML page
 │   └── esg_vs_returns.png        # Generated scatter plot image
 └── README.md                     # Project documentation
 ```

 ## Prerequisites
 - **SQL Server**: Microsoft SQL Server (e.g., Express Edition) with SQL Server Management Studio (SSMS).
 - **Python**: Python 3.6+ with the following packages:
   - `pyodbc` (for MSSQL connection)
   - `numpy` (for calculations)
   - `matplotlib` (for plotting)
 - **ODBC Driver**: ODBC Driver 17 for SQL Server (or compatible version).

 ## Setup Instructions
 1. **Set Up the Database**:
    - Open SSMS and connect to your SQL Server instance (e.g., `SHRADDHA\SQLEXPRESS`).
    - Run `sql/create_database.sql` to create the `ESGInvestmentDB` database and `Investments` table with sample data.
    - Run `sql/stored_procedures.sql` to create the stored procedures (`sp_GetWeightedESGScore`, `sp_GetTotalReturns`, `sp_GetInvestmentSummary`).

 2. **Install Python Dependencies**:
    - Navigate to the project folder in a terminal:
      ```bash
      cd path/to/esg-investment-tracker
      ```
    - (Optional) Create a virtual environment:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - Install required packages:
      ```bash
      pip install pyodbc numpy matplotlib
      ```

 3. **Update the Python Script**:
    - Open `src/esg_tracker.py` and update the `conn_str` with your SQL Server instance name:
      ```python
      conn_str = (
          "DRIVER={ODBC Driver 17 for SQL Server};"
          "SERVER=SHRADDHA\\SQLEXPRESS;"  # Replace with your server name
          "DATABASE=ESGInvestmentDB;"
          "Trusted_Connection=yes;"
      )
      ```

 4. **Run the Python Script**:
    - Execute the script to generate the scatter plot:
      ```bash
      python src/esg_tracker.py
      ```
    - This generates `dashboard/esg_vs_returns.png`.

 5. **View the Dashboard**:
    - Open `dashboard/index.html` in a web browser to view the offline dashboard.
    - The dashboard displays the weighted ESG score, total annual return, and a scatter plot of ESG scores vs. returns.

 ## Usage
 - Modify the `Investments` table in `ESGInvestmentDB` to add your own data.
 - Re-run `esg_tracker.py` to update the visualization.
 - Refresh `index.html` in your browser to see the updated dashboard.

 ## Output
 - **Weighted ESG Score**: 85.62 (based on sample data).
 - **Total Annual Return**: $565.50 (based on sample data).
 - **Scatter Plot**: Visualizes ESG scores vs. annual returns, with point sizes proportional to investment amounts.

 ## Future Improvements
 - Add interactive features to the dashboard (e.g., using JavaScript).
 - Implement real-time data updates from an API.
 - Expand the database to include more ESG metrics.

 ## License
 MIT License - feel free to use and modify this project.

