import pandas as pd
from visualizations import generate_all_visualizations
from report import save_analysis_summary, generate_text_report, print_summary

def load_data(path):
    """Load CSV data into a pandas DataFrame."""
    try:
        df = pd.read_csv(path)
        if df.empty:
            raise ValueError("Dataset is empty")
        print(f"✅ Data loaded: {len(df)} rows, {len(df.columns)} columns")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def clean_data(df):
    """Clean and preprocess the data."""
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Remove rows with missing values
    df = df.dropna()
    print(f"✅ Data cleaned: {len(df)} rows remaining after removing NaN values")
    
    # Convert date columns
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            print(f"✅ Converted '{col}' to datetime format")
    
    return df

def analyze_data(df):
    """Generate statistical analysis."""
    summary = df.describe()
    print("✅ Data analysis completed")
    return summary

def main():
    """Main pipeline: load, clean, analyze, visualize, and report."""
    print("\n" + "=" * 60)
    print("WEATHER ANALYSIS PIPELINE")
    print("=" * 60 + "\n")
    
    # Step 1: Load data
    df = load_data("Weather_Data.csv")
    if df is None:
        return
    
    # Step 2: Clean data
    df = clean_data(df)
    
    # Step 3: Analyze data
    summary = analyze_data(df)
    print_summary(df)
    
    # Step 4: Save analysis summary
    save_analysis_summary(df)
    
    # Step 5: Generate visualizations
    generate_all_visualizations(df)
    
    # Step 6: Generate text report
    generate_text_report(df, summary)
    
    print("=" * 60)
    print("✅ ALL ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  📊 report/analysis_summary.csv")
    print("  📄 report.txt")
    print("  📈 visualizations/line_chart.png")
    print("  📊 visualizations/histogram.png")
    print("     + Additional visualizations if available")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()