import pandas as pd

# Read the sales.csv file
input_file = 'sales.csv'
df = pd.read_csv(input_file)

# Calculate total for each customer
df['Total'] = df['SubTotal'] + df['TaxAmt'] + df['Freight']
result = df.groupby('CustomerID', as_index=False)['Total'].sum()

# Save the result to salesreportFINAL.csv
output_file = 'salesreportFINAL.csv'
result.to_csv(output_file, index=False)

print("File created successfully as salesreportFINAL.csv")
