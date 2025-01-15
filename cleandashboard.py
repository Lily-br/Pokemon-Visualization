import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# تنظیمات کلی برای نمودارها
sns.set_style("whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6), 'font.size': 12})

@st.cache_data
def load_data():
    """بارگذاری داده‌های پوکمون از فایل CSV."""
    return pd.read_csv('Pokemon.csv')

df = load_data()

# عنوان داشبورد
st.title("Pokemon Dashboard")

# فیلترهای تعاملی
selected_type1 = st.sidebar.selectbox("Select Type 1:", options=[None] + sorted(df["Type 1"].dropna().unique().tolist()))
selected_type2 = st.sidebar.selectbox("Select Type 2:", options=[None] + sorted(df["Type 2"].dropna().unique().tolist()))
show_legendary = st.sidebar.checkbox("Show only Legendary Pokémon", value=False)

# فیلتر کردن داده‌ها
filtered_df = df.copy()
if selected_type1:
    filtered_df = filtered_df[filtered_df["Type 1"] == selected_type1]
if selected_type2:
    filtered_df = filtered_df[filtered_df["Type 2"] == selected_type2]
if show_legendary:
    filtered_df = filtered_df[filtered_df["Legendary"] == True]

# نمایش داده‌های فیلتر شده
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# ایجاد تب‌های داشبورد
tabs = st.tabs(["Statistical Analysis", "Legendary Analysis", "Correlation Heatmap", "Additional Insights"])

with tabs[0]:
    st.header("1. Statistical Analysis")
    st.subheader("Summary Statistics")
    st.write(filtered_df[["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]].describe())
    
    st.subheader("Distribution of Total Stats")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df["Total"], bins=15, kde=True, ax=ax1, color='skyblue')
    plt.title("Distribution of Total Stats")
    plt.xlabel("Total Stats")
    plt.ylabel("Frequency")
    st.pyplot(fig1)
    
    st.subheader("Box Plots for Multiple Features")
    features = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    colors = ['lightgreen', 'lightcoral', 'lightskyblue', 'lightpink', 'lightyellow', 'lightblue']
    fig2, axes = plt.subplots(2, 3, figsize=(20, 10))
    for ax, feature, color in zip(axes.flatten(), features, colors):
        sns.boxplot(y=filtered_df[feature], ax=ax, color=color)
        ax.set_title(feature)
    plt.tight_layout()
    st.pyplot(fig2)
    
    st.subheader("Pair Plot")
    selected_features = st.multiselect("Select features for Pair Plot (up to 4):", options=["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], default=["Total", "HP", "Attack", "Defense"])
    if 2 <= len(selected_features) <= 4:
        fig3 = px.scatter_matrix(filtered_df[selected_features + ["Type 1"]], dimensions=selected_features, color="Type 1", title="Pair Plot", opacity=0.7, height=800)
        st.plotly_chart(fig3)
    else:
        st.warning("Please select between 2 to 4 features for the Pair Plot.")
    
    st.subheader("KDE Plots for Multiple Features")
    fig4, ax4 = plt.subplots(figsize=(12, 8))
    for feature in ["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
        sns.kdeplot(filtered_df[feature], shade=True, label=feature, alpha=0.6)
    plt.title("KDE Plots of Numerical Features")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend()
    st.pyplot(fig4)
    
with tabs[1]:
    st.header("2. Legendary Analysis")
    st.subheader("Legendary vs Non-Legendary Pokémon")
    legendary_count = filtered_df['Legendary'].value_counts().rename(index={True: 'Legendary', False: 'Non-Legendary'})
    fig5, ax5 = plt.subplots()
    sns.barplot(x=legendary_count.index, y=legendary_count.values, palette='viridis', ax=ax5)
    plt.title("Legendary vs Non-Legendary Pokémon")
    st.pyplot(fig5)
