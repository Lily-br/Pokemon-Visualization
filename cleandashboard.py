import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set global styles
sns.set_style("whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6), 'font.size': 12})

@st.cache_data
def load_data(file_path: str = 'Pokemon.csv') -> pd.DataFrame:
    """Loads Pokemon dataset from a CSV file."""
    return pd.read_csv(file_path)

def filter_data(df: pd.DataFrame, type1: str, type2: str, legendary: bool) -> pd.DataFrame:
    """Filters Pokemon data based on selected criteria."""
    if type1:
        df = df[df["Type 1"] == type1]
    if type2:
        df = df[df["Type 2"] == type2]
    if legendary:
        df = df[df["Legendary"] == True]
    return df

def plot_histogram(data: pd.Series, title: str, xlabel: str, ylabel: str, color: str = 'skyblue'):
    """Plots a histogram with KDE for a given data series."""
    fig, ax = plt.subplots()
    sns.histplot(data, bins=15, kde=True, ax=ax, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

def plot_boxplots(df: pd.DataFrame):
    """Plots box plots for multiple features."""
    features = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    colors = ['lightgreen', 'lightcoral', 'lightskyblue', 'lightpink', 'lightyellow', 'lightblue']
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    for ax, feature, color in zip(axes.flatten(), features, colors):
        sns.boxplot(y=df[feature], ax=ax, color=color)
        ax.set_title(feature)
    plt.tight_layout()
    st.pyplot(fig)

def main():
    """Main function to run the Streamlit app."""
    df = load_data()
    
    st.title("Pokemon Dashboard")
    
    type1 = st.sidebar.selectbox("Select Type 1:", options=[None] + sorted(df["Type 1"].dropna().unique().tolist()))
    type2 = st.sidebar.selectbox("Select Type 2:", options=[None] + sorted(df["Type 2"].dropna().unique().tolist()))
    legendary = st.sidebar.checkbox("Show only Legendary Pokémon", value=False)
    
    filtered_df = filter_data(df.copy(), type1, type2, legendary)
    
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)
    
    tabs = st.tabs(["Statistical Analysis", "Legendary Analysis", "Correlation Heatmap", "Additional Insights"])
    
    with tabs[0]:
        st.header("1. Statistical Analysis")
        st.subheader("Summary Statistics")
        st.write(filtered_df[["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]].describe())
        
        st.subheader("Distribution of Total Stats")
        plot_histogram(filtered_df["Total"], "Distribution of Total Stats", "Total Stats", "Frequency")
        
        st.subheader("Box Plots for Multiple Features")
        plot_boxplots(filtered_df)
    
if __name__ == "__main__":
    main()
