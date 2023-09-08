## mapping data for google sheets

import pandas as pd
from google.colab import files


def convert_csv(input_file, output_file, column_mapping):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Create a new DataFrame for the output CSV file
    output_df = pd.DataFrame()

    # Iterate over the column mapping
    for output_column, input_column in column_mapping.items():
        # Copy the data from the input column to the output column
        output_df[output_column] = df[input_column]

    # Save the output DataFrame as a CSV file within Google Colab
    output_df.to_csv(output_file, index=False)

# Example usage
input_file = 'OLD_Crm' #can replace with path to file
output_file = 'new_CRM'
column_mapping = {
    'Lead - Title': 'Project Name',
    'Lead - Contact person': 'Contact Name',
    'Person - Email': 'Contact Email'
}

convert_csv(input_file, output_file, column_mapping)

# Download the output CSV file from Google Colab
files.download(output_file)