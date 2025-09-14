import pandas as pd
import os

file_path = r'c:\Users\neeha\Downloads\TDS training file.xlsx'

if os.path.exists(file_path):
    try:
        df = pd.read_excel(file_path, header=None)
        
        print("Full Excel Content:")
        print("="*80)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        
        print(df.to_string())
        
        print("\n\nAnalyzing TDS Solution Structure:")
        print("="*80)
        
        for i, row in df.iterrows():
            if pd.notna(row[0]) and pd.notna(row[1]):
                print(f"{row[0]}: {row[1]}")
            
    except Exception as e:
        print(f"Error reading Excel file: {e}")
else:
    print(f"File not found: {file_path}")