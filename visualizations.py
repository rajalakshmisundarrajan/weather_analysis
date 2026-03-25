import matplotlib.pyplot as plt
import os

def create_viz_directory():
    """Create visualizations directory if it doesn't exist."""
    if not os.path.exists("visualizations"):
        os.makedirs("visualizations")

def plot_temperature_over_time(df, date_col, temp_col):
    """Plot temperature values over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(df[date_col], df[temp_col], linewidth=2, color='tomato')
    plt.title("Temperature Over Time", fontsize=16, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel(f"{temp_col} (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("visualizations/line_chart.png", dpi=300)
    plt.close()
    print("✅ Line chart saved: visualizations/line_chart.png")

def plot_temperature_distribution(df, temp_col):
    """Plot histogram of temperature distribution."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[temp_col], bins=20, color='skyblue', edgecolor='black')
    plt.title("Temperature Distribution", fontsize=16, fontweight='bold')
    plt.xlabel(f"{temp_col} (°C)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig("visualizations/histogram.png", dpi=300)
    plt.close()
    print("✅ Histogram saved: visualizations/histogram.png")

def plot_humidity_distribution(df, humidity_col):
    """Plot humidity distribution if humidity data exists."""
    if humidity_col in df.columns:
        plt.figure(figsize=(10, 6))
        plt.hist(df[humidity_col], bins=20, color='lightgreen', edgecolor='black')
        plt.title("Humidity Distribution", fontsize=16, fontweight='bold')
        plt.xlabel(f"{humidity_col} (%)", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig("visualizations/humidity_histogram.png", dpi=300)
        plt.close()
        print("✅ Humidity chart saved: visualizations/humidity_histogram.png")

def generate_all_visualizations(df):
    """Generate all available visualizations."""
    create_viz_directory()
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    date_col = [col for col in df.columns if 'date' in col.lower()]
    
    # Plot temperature over time if date and temperature exist
    if date_col and numeric_cols.tolist():
        plot_temperature_over_time(df, date_col[0], numeric_cols[0])
    
    # Plot temperature distribution
    if numeric_cols.tolist():
        plot_temperature_distribution(df, numeric_cols[0])
    
    # Plot humidity if available
    humidity_cols = [col for col in df.columns if 'humidity' in col.lower()]
    if humidity_cols:
        plot_humidity_distribution(df, humidity_cols[0])
