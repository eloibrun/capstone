# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown'
                                    options=[
                                        {label: 'All Sites', 'value': 'All'}
                                        {label: 'site1', 'value': 'site1'}
                                        {label: 'site2', 'value': 'site2'}
                                        {label: 'site3', 'value': 'site3'}
                                        {label: 'site4', 'value': 'site4'}
                                    ]
                                    value='All'
                                    placeholder='Select launch Site here
                                    searchable=True'
                                    )

                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                @app.callback(Output(component_id='success-pie-chart', component_property='figure')
                                    Input(component_id='site-dropdown', component_property='value'))
                                def get_pie_chart(entered_site):
                                        filtered_df=spacex_df
                                        if entered_site=='All':
                                                fig = px.pie(filtered_df, values='class',
                                                names='success-pie-chart',
                                                title='success rate all sites')
                                                return fig
                                        else
                                                filtered_df = spacex_df[['Launch_Site']==entered_site]
                                                fig = px.pie(filtered_df, values='class',
                                                names='success-pie-chart',
                                                title='success rate selected site')
                                                return fig
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                    min=0, max=10000, step=1000,
                                    marks={0: '0',
                                            100: '100'},
                                    value=[min_payload, max_payload])


                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                @app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure')
                                    Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")]
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])
                                def get_scatter_chart(entered_site):
                                        filtered_df=spacex_df
                                        if entered_site=='All':
                                                fig = px.scatter(filtered_df, y='class', x='PAYLOAD_MASS__KG_', color="Booster Version Category",
                                                names='success-payload-scatter-chart',
                                                title='Payload mass kg vs success all sites')
                                                return fig
                                        else
                                                filtered_df = spacex_df[['Launch_Site']==entered_site]
                                                fig = px.scatter(filtered_df, y='class', x='PAYLOAD_MASS__KG_', color="Booster Version Category",
                                                names='success-payload-scatter-chart',
                                                title='Payload mass kg vs success selected site')
                                                return fig
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure')
    input(component_id='site-dropdown', component_property='value')
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure')
    Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")

# Run the app
if __name__ == '__main__':
    app.run_server()
