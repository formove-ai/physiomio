#!/usr/bin/env python3
"""
Script to normalize SNR Mean and SNR Std Dev values by patient using min-max normalization.

This script reads the detailed_snrs_table.csv file and applies min-max normalization
to the SNR Mean (dB) and SNR Std Dev (dB) columns on a per-patient basis.
The normalized values will be in the range [0, 1].

Output: detailed_snrs_normalized_table.csv
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


def normalize_snrs_by_patient(input_file='detailed_snrs_table.csv', 
                             output_file='detailed_snrs_normalized_table.csv'):
    """
    Normalize SNR values by patient and save to new CSV file.
    
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
    
    # Create a copy for normalization
    df_normalized = df.copy()
    
    # Initialize normalized columns
    snr_mean_col = 'SNR Mean (dB)'
    snr_std_col = 'SNR Std Dev (dB)'
    
    df_normalized[f'{snr_mean_col} (Normalized)'] = 0.0
    df_normalized[f'{snr_std_col} (Normalized)'] = 0.0
    
    # Process each patient individually
    patients = sorted(df['Patient'].unique())
    print(f"\nProcessing {len(patients)} patients individually...")
    
    for patient_id in patients:
        # Get all recordings for this patient (both healthy and impaired)
        patient_mask = df['Patient'] == patient_id
        patient_data = df[patient_mask].copy()
        
        print(f"Patient {patient_id}: {len(patient_data)} recordings")
        
        # Normalize SNR Mean for this patient
        snr_mean_values = patient_data[snr_mean_col]
        normalized_mean = min_max_normalize(snr_mean_values)
        df_normalized.loc[patient_mask, f'{snr_mean_col} (Normalized)'] = normalized_mean
        
        # Normalize SNR Std Dev for this patient
        snr_std_values = patient_data[snr_std_col]
        normalized_std = min_max_normalize(snr_std_values)
        df_normalized.loc[patient_mask, f'{snr_std_col} (Normalized)'] = normalized_std
    
    # Reorder columns to put normalized columns after original ones
    original_cols = df.columns.tolist()
    new_cols = [f'{snr_mean_col} (Normalized)', f'{snr_std_col} (Normalized)']
    
    # Insert normalized columns after the original SNR columns
    snr_mean_idx = original_cols.index(snr_mean_col)
    snr_std_idx = original_cols.index(snr_std_col)
    
    final_cols = original_cols.copy()
    final_cols.insert(snr_mean_idx + 1, f'{snr_mean_col} (Normalized)')
    final_cols.insert(snr_std_idx + 2, f'{snr_std_col} (Normalized)')
    
    df_normalized = df_normalized[final_cols]
    
    # Save to new CSV file
    df_normalized.to_csv(output_file, index=False)
    
    print(f"\nNormalization complete!")
    print(f"Output saved to: {output_file}")
    
    # Print some statistics
    print(f"\nNormalization Statistics:")
    print(f"Original SNR Mean range: [{df[snr_mean_col].min():.2f}, {df[snr_mean_col].max():.2f}]")
    print(f"Original SNR Std Dev range: [{df[snr_std_col].min():.2f}, {df[snr_std_col].max():.2f}]")
    
    print(f"\nNormalized SNR Mean range: [{df_normalized[f'{snr_mean_col} (Normalized)'].min():.2f}, {df_normalized[f'{snr_mean_col} (Normalized)'].max():.2f}]")
    print(f"Normalized SNR Std Dev range: [{df_normalized[f'{snr_std_col} (Normalized)'].min():.2f}, {df_normalized[f'{snr_std_col} (Normalized)'].max():.2f}]")
    
    # Show example of normalization for first few patients
    print(f"\nExample normalization for first 3 patients:")
    for patient_id in sorted(df['Patient'].unique())[:3]:
        patient_data = df[df['Patient'] == patient_id]
        patient_norm = df_normalized[df_normalized['Patient'] == patient_id]
        
        print(f"\nPatient {patient_id}:")
        print(f"  Original SNR Mean range: [{patient_data[snr_mean_col].min():.2f}, {patient_data[snr_mean_col].max():.2f}]")
        print(f"  Normalized SNR Mean range: [{patient_norm[f'{snr_mean_col} (Normalized)'].min():.2f}, {patient_norm[f'{snr_mean_col} (Normalized)'].max():.2f}]")
        print(f"  Original SNR Std Dev range: [{patient_data[snr_std_col].min():.2f}, {patient_data[snr_std_col].max():.2f}]")
        print(f"  Normalized SNR Std Dev range: [{patient_norm[f'{snr_std_col} (Normalized)'].min():.2f}, {patient_norm[f'{snr_std_col} (Normalized)'].max():.2f}]")


if __name__ == "__main__":
    # Check if input file exists
    input_file = Path('detailed_snrs_table.csv')
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found!")
        print("Please make sure the file exists in the current directory.")
        exit(1)
    
    # Run normalization
    normalize_snrs_by_patient()
