import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set_style("whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6), 'font.size': 12})

@st.cache_data
def load_data():
    return pd.read_csv('Pokemon.csv')

df = load_data()

st.title("Pokemon Dashboard")

st.sidebar.header("Filters")

type1 = st.sidebar.selectbox(
    "Select Type 1:",
    options=[None] + sorted(df["Type 1"].dropna().unique().tolist())
)

type2 = st.sidebar.selectbox(
    "Select Type 2:",
    options=[None] + sorted(df["Type 2"].dropna().unique().tolist())
)

legendary = st.sidebar.checkbox("Show only Legendary Pokémon", value=False)

filtered_df = df.copy()
if type1:
    filtered_df = filtered_df[filtered_df["Type 1"] == type1]
if type2:
    filtered_df = filtered_df[filtered_df["Type 2"] == type2]
if legendary:
    filtered_df = filtered_df[filtered_df["Legendary"] == True]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

tabs = st.tabs([
    "Statistical Analysis",
    "Legendary Analysis",
    "Correlation Heatmap",
    "Additional Insights"
])

with tabs[0]:
    st.header("1. Statistical Analysis")
    
    st.subheader("Summary Statistics")
    st.write(filtered_df[["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]].describe())
    
    st.subheader("Distribution of Total Stats")
    fig1, ax1 = plt.subplots()
    sns.histplot(
        filtered_df["Total"],
        bins=15,
        kde=True,
        ax=ax1,
        color='skyblue'
    )
    plt.title("Distribution of Total Stats")
    plt.xlabel("Total Stats")
    plt.ylabel("Frequency")
    st.pyplot(fig1)
    
    st.subheader("Box Plots for Multiple Features")
    fig2, axes2 = plt.subplots(2, 3, figsize=(20, 10))
    sns.boxplot(y=filtered_df["HP"], ax=axes2[0, 0], color='lightgreen')
    axes2[0, 0].set_title("HP")
    
    sns.boxplot(y=filtered_df["Attack"], ax=axes2[0, 1], color='lightcoral')
    axes2[0, 1].set_title("Attack")
    
    sns.boxplot(y=filtered_df["Defense"], ax=axes2[0, 2], color='lightskyblue')
    axes2[0, 2].set_title("Defense")
    
    sns.boxplot(y=filtered_df["Sp. Atk"], ax=axes2[1, 0], color='lightpink')
    axes2[1, 0].set_title("Sp. Atk")
    
    sns.boxplot(y=filtered_df["Sp. Def"], ax=axes2[1, 1], color='lightyellow')
    axes2[1, 1].set_title("Sp. Def")
    
    sns.boxplot(y=filtered_df["Speed"], ax=axes2[1, 2], color='lightblue')
    axes2[1, 2].set_title("Speed")
    
    plt.tight_layout()
    st.pyplot(fig2)
    
    st.subheader("Violin Plots for Multiple Features")
    fig3, axes3 = plt.subplots(2, 3, figsize=(20, 10))
    sns.violinplot(y=filtered_df["HP"], ax=axes3[0, 0], color='lightgreen')
    axes3[0, 0].set_title("HP")
    
    sns.violinplot(y=filtered_df["Attack"], ax=axes3[0, 1], color='lightcoral')
    axes3[0, 1].set_title("Attack")
    
    sns.violinplot(y=filtered_df["Defense"], ax=axes3[0, 2], color='lightskyblue')
    axes3[0, 2].set_title("Defense")
    
    sns.violinplot(y=filtered_df["Sp. Atk"], ax=axes3[1, 0], color='lightpink')
    axes3[1, 0].set_title("Sp. Atk")
    
    sns.violinplot(y=filtered_df["Sp. Def"], ax=axes3[1, 1], color='lightyellow')
    axes3[1, 1].set_title("Sp. Def")
    
    sns.violinplot(y=filtered_df["Speed"], ax=axes3[1, 2], color='lightblue')
    axes3[1, 2].set_title("Speed")
    
    plt.tight_layout()
    st.pyplot(fig3)
    
    st.subheader("Pair Plot")
    pair_features = st.multiselect(
        "Select features for Pair Plot (up to 4):",
        options=["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"],
        default=["Total", "HP", "Attack", "Defense"]
    )
    
    if 2 <= len(pair_features) <= 4:
        pair_df = filtered_df[pair_features + ['Type 1']]
        fig4 = px.scatter_matrix(
            pair_df,
            dimensions=pair_features,
            color="Type 1",
            title="Pair Plot",
            opacity=0.7,
            height=800
        )
        st.plotly_chart(fig4)
    else:
        st.warning("Please select between 2 to 4 features for the Pair Plot.")
    
    st.subheader("KDE Plots for Multiple Features")
    fig5, ax5 = plt.subplots(figsize=(12, 8))
    for feature in ["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
        sns.kdeplot(filtered_df[feature], shade=True, label=feature, alpha=0.6)
    plt.title("KDE Plots of Numerical Features")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend()
    st.pyplot(fig5)
    
    st.subheader("Strip Plots for Multiple Features")
    fig6, axes6 = plt.subplots(2, 3, figsize=(20, 10))
    sns.stripplot(y=filtered_df["HP"], ax=axes6[0, 0], color='green', alpha=0.5)
    axes6[0, 0].set_title("HP")
    
    sns.stripplot(y=filtered_df["Attack"], ax=axes6[0, 1], color='red', alpha=0.5)
    axes6[0, 1].set_title("Attack")
    
    sns.stripplot(y=filtered_df["Defense"], ax=axes6[0, 2], color='blue', alpha=0.5)
    axes6[0, 2].set_title("Defense")
    
    sns.stripplot(y=filtered_df["Sp. Atk"], ax=axes6[1, 0], color='pink', alpha=0.5)
    axes6[1, 0].set_title("Sp. Atk")
    
    sns.stripplot(y=filtered_df["Sp. Def"], ax=axes6[1, 1], color='yellow', alpha=0.5)
    axes6[1, 1].set_title("Sp. Def")
    
    sns.stripplot(y=filtered_df["Speed"], ax=axes6[1, 2], color='cyan', alpha=0.5)
    axes6[1, 2].set_title("Speed")
    
    plt.tight_layout()
    st.pyplot(fig6)

