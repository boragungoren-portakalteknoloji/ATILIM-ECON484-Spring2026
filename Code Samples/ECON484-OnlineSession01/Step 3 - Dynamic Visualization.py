import pandas as pd
import plotly.express as px
from ipywidgets import interact, widgets, fixed

# 1. Load the dataset
df = pd.read_csv('survey_data.csv')

# 2. Get the list of all columns except RESP_ID for the dropdown menus
# RESP_ID is excluded as it is a unique identifier, not a categorical variable.
categorical_options = [col for col in df.columns if col != 'RESP_ID']


# 3. Define the Interactive Function
def plot_categorical_relationship(var_x, var_y):
    """
    Generates an interactive Sunburst chart based on selected variables.
    Sunburst acts as a dynamic alternative to Mosaic plots for hierarchical data.
    """

    # Group and count the intersections of selected categories
    count_df = df.groupby([var_x, var_y]).size().reset_index(name='Total_Count')

    # Create the visualization
    # The 'path' parameter determines the hierarchy: from Outer Category to Inner Response
    fig = px.sunburst(
        count_df,
        path=[var_x, var_y],
        values='Total_Count',
        color=var_x,
        title=f"Interactive Analysis: {var_x} vs {var_y}",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        width=800,
        height=800
    )

    # Update layout for a cleaner 'Operational' look
    fig.update_layout(
        margin=dict(t=50, l=0, r=0, b=0),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
    )

    fig.show()


# 4. Create the Interactive Interface
# Using @interact to generate the UI components (Dropdowns)
interact(
    plot_categorical_relationship,
    var_x=widgets.Dropdown(
        options=categorical_options,
        value='EDUCATION',
        description='Base Variable:',
        style={'description_width': 'initial'}
    ),
    var_y=widgets.Dropdown(
        options=categorical_options,
        value='Q1',
        description='Target Variable:',
        style={'description_width': 'initial'}
    )
);

# STRATEGIC NOTE:
# This UI eliminates the 'Translation Tax' by allowing non-technical stakeholders
# to explore data consistency (e.g., checking Q1 vs Q9) without modifying the source code.