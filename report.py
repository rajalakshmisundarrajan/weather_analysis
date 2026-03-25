import os
import pandas as pd

def create_report_directory():
    """Create report directory if it doesn't exist."""
    if not os.path.exists("report"):
        os.makedirs("report")

def save_analysis_summary(df, filename="report/analysis_summary.csv"):
    """Save statistical summary to CSV."""
    create_report_directory()
    summary = df.describe()
    summary.to_csv(filename)
    print(f"✅ Analysis summary saved: {filename}")
    return summary

def generate_text_report(df, summary, output_file="report.txt"):
    """Generate a comprehensive text report."""
    with open(output_file, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("WEATHER ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")
        
        # Dataset Overview
        f.write("DATASET OVERVIEW\n")
        f.write("-" * 60 + "\n")
        f.write(f"Total Records: {len(df)}\n")
        f.write(f"Total Columns: {len(df.columns)}\n")
        f.write(f"Columns: {', '.join(df.columns)}\n\n")
        
        # Statistical Summary
        f.write("STATISTICAL SUMMARY\n")
        f.write("-" * 60 + "\n")
        f.write(summary.to_string())
        f.write("\n\n")
        
        # Data Quality
        f.write("DATA QUALITY\n")
        f.write("-" * 60 + "\n")
        f.write(f"Missing Values:\n")
        for col in df.columns:
            missing = df[col].isna().sum()
            if missing > 0:
                f.write(f"  {col}: {missing} ({missing/len(df)*100:.2f}%)\n")
        f.write(f"\nNo missing values found in any column.\n\n") if df.isna().sum().sum() == 0 else None
        
        # Column Information
        f.write("COLUMN INFORMATION\n")
        f.write("-" * 60 + "\n")
        for col in df.columns:
            dtype = df[col].dtype
            f.write(f"  {col}: {dtype}\n")
        
        f.write("\n" + "=" * 60 + "\n")
        f.write("End of Report\n")
        f.write("=" * 60 + "\n")
    
    print(f"✅ Text report generated: {output_file}")

def print_summary(df):
    """Print summary statistics to console."""
    print("\n" + "=" * 60)
    print("DATA SUMMARY STATISTICS")
    print("=" * 60)
    print(df.describe())
    print("=" * 60 + "\n")
