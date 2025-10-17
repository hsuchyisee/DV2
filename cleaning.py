import pandas as pd

def clean_world_tourism_data():
    """
    Clean world_tourism_economy_data.csv to only contain actual countries,
    using countries_cleaned.csv as the reference for valid country codes.
    """
    
    # Read the tourism economy data
    tourism_data = pd.read_csv('data/world_tourism_economy_data.csv')
    print(f"Original tourism data shape: {tourism_data.shape}")
    print(f"Unique entities in original data: {tourism_data['country'].nunique()}")
    
    # Read the countries reference data to get valid country codes
    countries_ref = pd.read_csv('data/countries_cleaned.csv')
    
    # Extract unique country codes from the reference data
    # Use the 'Alpha-3 code' column which matches the 'country_code' in tourism data
    valid_country_codes = set(countries_ref['Alpha-3 code'].dropna().unique())
    print(f"Valid country codes from reference: {len(valid_country_codes)}")
    
    # Filter tourism data to only include valid country codes
    tourism_countries_only = tourism_data[
        tourism_data['country_code'].isin(valid_country_codes)
    ].copy()
    
    print(f"Filtered tourism data shape: {tourism_countries_only.shape}")
    print(f"Unique countries in filtered data: {tourism_countries_only['country'].nunique()}")
    
    # Show some examples of what was filtered out
    filtered_out = tourism_data[~tourism_data['country_code'].isin(valid_country_codes)]
    print(f"\nExamples of entities filtered out (non-countries):")
    print(filtered_out['country'].unique()[:10])
    
    # Save the cleaned data
    output_file = 'data/world_tourism_economy_data_countries_only.csv'
    tourism_countries_only.to_csv(output_file, index=False)
    print(f"\nCleaned data saved to: {output_file}")
    
    return tourism_countries_only

if __name__ == "__main__":
    cleaned_data = clean_world_tourism_data()
