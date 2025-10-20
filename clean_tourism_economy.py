import pandas as pd
import numpy as np

def clean_tourism_economy_data():
    """
    Clean world_tourism_economy_data.csv to have only average values across years for each country.
    """
    
    # Read the original data
    print("Reading original tourism economy data...")
    df = pd.read_csv('data/world_tourism_economy_data.csv')
    
    print(f"Original data shape: {df.shape}")
    print(f"Years range: {df['year'].min()} - {df['year'].max()}")
    print(f"Number of unique countries: {df['country'].nunique()}")
    
    # Define numeric columns to average (excluding country, country_code, year)
    numeric_columns = [
        'tourism_receipts', 'tourism_arrivals', 'tourism_exports', 
        'tourism_departures', 'tourism_expenditures', 'gdp', 
        'inflation', 'unemployment'
    ]
    
    # Group by country and country_code, then calculate mean for numeric columns
    print("Calculating averages across years for each country...")
    
    # Create aggregation dictionary
    agg_dict = {}
    for col in numeric_columns:
        if col in df.columns:
            agg_dict[col] = 'mean'
    
    # Group and aggregate
    df_avg = df.groupby(['country', 'country_code']).agg(agg_dict).reset_index()
    
    # Round numeric values to reasonable decimal places
    for col in numeric_columns:
        if col in df_avg.columns:
            if col in ['tourism_receipts', 'tourism_arrivals', 'tourism_exports', 
                      'tourism_departures', 'tourism_expenditures', 'gdp']:
                # Round large monetary/count values to whole numbers
                df_avg[col] = df_avg[col].round(0)
            else:
                # Round percentages to 2 decimal places
                df_avg[col] = df_avg[col].round(2)
    
    print(f"Cleaned data shape: {df_avg.shape}")
    print("Sample of cleaned data:")
    print(df_avg.head())
    
    # Save the cleaned data
    output_file = 'data/world_tourism_economy_data_averaged.csv'
    df_avg.to_csv(output_file, index=False)
    print(f"\nCleaned data saved to: {output_file}")
    
    # Show some statistics
    print("\nData Summary:")
    print(f"Countries with complete data: {df_avg.dropna().shape[0]}")
    print(f"Countries with any missing values: {df_avg.isnull().any(axis=1).sum()}")
    
    return df_avg

if __name__ == "__main__":
    cleaned_data = clean_tourism_economy_data()
