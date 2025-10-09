#!/usr/bin/env python3
"""
Script to normalize PSD values by patient using min-max normalization.

This script reads the detailed_psd_table.csv file and applies min-max normalization
to all PSD frequency band columns on a per-patient basis.
For each patient, normalizes all their recordings (both healthy and impaired)
based on that patient's min/max values across all their recordings.

Output: detailed_psd_normalized_table.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path


def min_max_normalize(series):
    """
    Apply min-max normalization to a pandas Series.
    
    Args:
        series: pandas Series to normalize
        
    Returns:
        pandas Series with values normalized to [0, 1] range
    """
    min_val = series.min()
    max_val = series.max()
    
    # Handle case where all values are the same (avoid division by zero)
    if max_val == min_val:
        return pd.Series([0.5] * len(series), index=series.index)
    
    return (series - min_val) / (max_val - min_val)


def normalize_psd_by_patient(input_file='detailed_psd_table.csv', 
                            output_file='detailed_psd_normalized_table.csv'):
    """
    Normalize PSD values by patient and save to new CSV file.
    
    For each patient, normalizes all their recordings (both healthy and impaired)
    based on that patient's min/max values across all their recordings.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file
    """
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    print(f"Loaded data with {len(df)} rows and {len(df.columns)} columns")
    print(f"Columns: {list(df.columns)}")
    print(f"Unique patients: {df['Patient'].nunique()}")
    
    # Identify PSD columns (all columns that start with 'PSD_')
    psd_columns = [col for col in df.columns if col.startswith('PSD_')]
    print(f"Found {len(psd_columns)} PSD frequency band columns")
    
    # Create a copy for normalization
    df_normalized = df.copy()
    
    # Initialize normalized columns
    for col in psd_columns:
        df_normalized[f'{col} (Normalized)'] = 0.0
    
    # Process each patient individually
    patients = sorted(df['Patient'].unique())
    print(f"\nProcessing {len(patients)} patients individually...")
    
    for patient_id in patients:
        # Get all recordings for this patient (both healthy and impaired)
        patient_mask = df['Patient'] == patient_id
        patient_data = df[patient_mask].copy()
        
        print(f"Patient {patient_id}: {len(patient_data)} recordings")
        
        # Normalize each PSD column for this patient
        for col in psd_columns:
            psd_values = patient_data[col]
            normalized_values = min_max_normalize(psd_values)
            df_normalized.loc[patient_mask, f'{col} (Normalized)'] = normalized_values
    
    # Reorder columns to put normalized columns after original ones
    original_cols = df.columns.tolist()
    
    # Create new column order: original columns + all normalized columns
    normalized_cols = [f'{col} (Normalized)' for col in psd_columns]
    final_cols = original_cols + normalized_cols
    
    df_normalized = df_normalized[final_cols]
    
    # Save to new CSV file
    df_normalized.to_csv(output_file, index=False)
    
    print(f"\nNormalization complete!")
    print(f"Output saved to: {output_file}")
    
    # Print some statistics
    print(f"\nNormalization Statistics:")
    for i, col in enumerate(psd_columns[:3]):  # Show first 3 PSD columns as examples
        print(f"{col}:")
        print(f"  Original range: [{df[col].min():.2e}, {df[col].max():.2e}]")
        print(f"  Normalized range: [{df_normalized[f'{col} (Normalized)'].min():.2f}, {df_normalized[f'{col} (Normalized)'].max():.2f}]")
    
    if len(psd_columns) > 3:
        print(f"... and {len(psd_columns) - 3} more PSD frequency bands")
    
    # Show example of normalization for first patient
    print(f"\nExample normalization for Patient 1:")
    patient1_data = df[df['Patient'] == 1]
    patient1_norm = df_normalized[df_normalized['Patient'] == 1]
    
    for col in psd_columns[:2]:  # Show first 2 PSD columns as examples
        print(f"  {col}:")
        print(f"    Original range: [{patient1_data[col].min():.2e}, {patient1_data[col].max():.2e}]")
        print(f"    Normalized range: [{patient1_norm[f'{col} (Normalized)'].min():.2f}, {patient1_norm[f'{col} (Normalized)'].max():.2f}]")


if __name__ == "__main__":
    # Check if input file exists
    input_file = Path('detailed_psd_table.csv')
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found!")
        print("Please make sure the file exists in the current directory.")
        exit(1)
    
    # Run normalization
    normalize_psd_by_patient()
