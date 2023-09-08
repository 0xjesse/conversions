import pandas as pd

def convert_spreadsheet(input_file, output_file, column_mapping):
    # Read the input spreadsheet
    df = pd.read_excel(input_file)

    # Create a new DataFrame for the output spreadsheet
    output_df = pd.DataFrame()

    # Iterate over the column mapping
    for output_column, input_column in column_mapping.items():
        # Copy the data from the input column to the output column
        output_df[output_column] = df[input_column]

    # Write the output DataFrame to the output spreadsheet
    output_df.to_excel(output_file, index=False)

# Example usage
input_file = 'input.xlsx'
output_file = 'output.xlsx'
column_mapping = {
    'First Name': 'Name',
    'Last Name': 'Surname',
    'Email': 'Email Address'
}

convert_spreadsheet(input_file, output_file, column_mapping)