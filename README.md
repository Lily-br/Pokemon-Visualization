# Pokemon-Visualization

## Overview
This **Pokemon Dashboard** is a Streamlit-based web application that allows users to explore and analyze Pokemon data interactively. The application enables users to filter Pokemon by type, legendary status, and visualize various statistical insights using **matplotlib**, **seaborn**, and **plotly**.

## Features
- **Interactive Filters**: Filter Pokemon by "Type 1", "Type 2", and whether they are Legendary.
- **Statistical Analysis**: Provides summary statistics, histograms, and box plots for various attributes like HP, Attack, Defense, etc.
- **Visualizations**:
  - Distribution plots (histograms, KDE, violin plots)
  - Box plots for comparing attributes
  - Pair plots using **plotly** for feature comparisons
  - Correlation heatmaps
- **Legendary Pokemon Analysis**: A section to analyze the distribution of legendary vs. non-legendary Pokemon.

## Installation
To run this application locally, follow these steps:

### Prerequisites
Ensure you have Python installed (preferably version 3.8 or later). You will also need the following Python packages:

```sh
pip install streamlit pandas matplotlib seaborn plotly
```

### Running the Application
1. Clone this repository or download the script.
2. Place the **Pokemon.csv** dataset in the same directory as `dashboard.py`.
3. Run the Streamlit app:

```sh
streamlit run dashboard.py
```

4. Open the link provided in the terminal to view the dashboard in your web browser.

## Usage
1. **Select Filters**: Use the sidebar to filter Pokemon based on type and legendary status.
2. **Explore Tabs**:
   - "Statistical Analysis" for in-depth stats visualization.
   - "Legendary Analysis" to compare legendary and non-legendary Pokemon.
   - "Correlation Heatmap" to analyze attribute correlations.
   - "Additional Insights" for further exploratory data analysis.
3. **Interact with Plots**: Hover over plots for additional insights.

## Dataset
The application uses a dataset named **Pokemon.csv**, which should contain columns such as:
- `Type 1`, `Type 2`, `Legendary`
- `Total`, `HP`, `Attack`, `Defense`, `Sp. Atk`, `Sp. Def`, `Speed`

Ensure that the dataset follows the expected structure for proper functionality.

## Contributing
Feel free to contribute by submitting issues or pull requests. If you have suggestions for improvements or additional features, let us know!

## License
This project is licensed under the MIT License.

---
Enjoy analyzing Pokemon data with this interactive dashboard! 🚀

