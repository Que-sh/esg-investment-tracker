import pyodbc
import numpy as np
import matplotlib.pyplot as plt

     # Database connection
conn_str = (
         "DRIVER={ODBC Driver 17 for SQL Server};"
         "SERVER=SHRADDHA\\SQLEXPRESS;"  # Updated server name
         "DATABASE=ESGInvestmentDB;"
         "Trusted_Connection=yes;"
     )

try:
         # Connect to database
         conn = pyodbc.connect(conn_str)
         cursor = conn.cursor()

         # Execute stored procedures
         cursor.execute("EXEC sp_GetWeightedESGScore")
         weighted_esg_row = cursor.fetchone()
         weighted_esg = weighted_esg_row[0] if weighted_esg_row else None
         print(f"Weighted ESG Score: {weighted_esg}")

         cursor.execute("EXEC sp_GetTotalReturns")
         total_return_row = cursor.fetchone()
         total_return = total_return_row[0] if total_return_row else None
         print(f"Total Return: {total_return}")

         cursor.execute("EXEC sp_GetInvestmentSummary")
         rows = cursor.fetchall()
         print(f"Number of rows retrieved: {len(rows)}")
         for row in rows:
             print(f"Row: {row.bond_id}, {row.name}, ESG: {row.esg_score}, Return: {row.annual_return}, Amount: {row.investment_amount}")

         # Extract data for visualization
         if not rows:
             raise ValueError("No data retrieved from the database. Check the Investments table or stored procedure.")

         bond_ids = [row.bond_id for row in rows]
         esg_scores = [row.esg_score for row in rows]
         returns = [row.annual_return for row in rows]
         amounts = [row.investment_amount for row in rows]

         # Create scatter plot
         plt.figure(figsize=(10, 6))
         scatter = plt.scatter(esg_scores, returns, s=[float(a)/100 for a in amounts], alpha=0.6, c='green')
         for i, bond_id in enumerate(bond_ids):
             plt.annotate(bond_id, (esg_scores[i], returns[i]), fontsize=8)

         plt.title(f'ESG Score vs. Annual Return\nWeighted ESG: {weighted_esg:.2f} | Total Return: ${total_return:.2f}')
         plt.xlabel('ESG Score')
         plt.ylabel('Annual Return (%)')
         plt.grid(True)

         # Save plot
         plt.savefig('esg_vs_returns.png', dpi=300, bbox_inches='tight')
         plt.close()

         print("Visualization generated: esg_vs_returns.png")

except Exception as e:
         print(f"An error occurred: {e}")

finally:
         # Clean up
         if 'cursor' in locals():
             cursor.close()
         if 'conn' in locals():
             conn.close()