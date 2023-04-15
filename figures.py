import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import requests
import time

# ============================ FUNCTIONS ===============================
# -------- Update chart layout -------------
def chart_update_layout(figure, x_axis, y_axis):
    figure.update_layout(
        font_size=12,
        #width=450,
        height=300,
        autosize=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(14,17,23,255)',
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="rgba(100,100,100,0.3)",
            font_size=14,
            #font_family="Rockwell"
        ),

        legend_title_text='',
        legend=dict(
            orientation='h',
            yanchor='top',
            y=1.05,
            xanchor='left',
            x=0.01,
            font=dict(
                size=12,
                color="white"
            ),
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(0,0,0,0)",
            borderwidth=2
        ),
        legend_font=dict(size=12),  # legend location


        xaxis=dict(
            title=x_axis,
            title_font=dict(size=14, color='rgba(170,170,170,0.7)'), #, family='Arial Black'
            gridcolor='rgba(100,100,100,0.3)',
            linecolor='rgba(100,100,100,0.7)',
            tickfont=dict(color='rgba(100,100,100,1)')
            # rangeslider=dict(bgcolor='rgba(0,0,0,0)',yaxis_rangemode='auto')
        ),

        yaxis=dict(
            title=y_axis,
            title_font=dict(size=14, color='rgba(171,171,171,0.7)'), #, family='Arial Black'
            title_standoff=3,
            gridcolor='rgba(100,100,100,0.3)',
            linecolor='rgba(100,100,100,0.7)',
            tickfont=dict(color='rgba(100,100,100,1)')
        )
    )


def chart_update_layout_y2(figure, y2_axis, y2_range):
    figure.update_layout(

        yaxis2=dict(
            title=y2_axis,
            title_font=dict(size=14, color='rgba(171,171,171,0.7)'),  # , family='Arial Black'
            title_standoff=3,
            gridcolor='rgba(100,100,100,0)',
            linecolor='rgba(100,100,100,0.7)',
            tickfont=dict(color='rgba(100,100,100,1)'),
            overlaying="y", side="right", range=y2_range
        )

    )

def chart_update_legend(figure, names):
    series_names = names

    for idx, name in enumerate(series_names):
        figure.data[idx].name = name


# ============================ HISTORICAL DAILY TIME SERIES ===============================

# ------------------------ DATA ------------------------------------
## ----------- Data Frame ---------------
gainDailyUrl = 'https://node-api.flipsidecrypto.com/api/v2/queries/42de9e27-af83-4af3-ab82-dad0bc0d8d3c/data/latest'
df_gains_initial = pd.read_json(gainDailyUrl).sort_values(by="DATE").reset_index(drop=True)
df_gains_start_index = df_gains_initial.index[df_gains_initial['DATE'] == '2022-01-01'].tolist()
df_gains = df_gains_initial.loc[df_gains_start_index[0]:]


df_l1_table = pd.DataFrame(np.array([['Sui', 2, 3,4]
                                        , ['Sei', 5, 6,7]
                                        , [7, 8, 9,10]
                                        , ['test','','','']]),
                   columns=['Project', 'Category', 'Funding', 'Notes'])

df_l2_table = pd.DataFrame(np.array([[1, 2, 3,4]
                                        , [4, 5, 6,7]
                                        , [7, 8, 9,10]
                                        , ['test','','','']]),
                   columns=['Project', 'Category', 'Funding', 'Notes'])

df_other_table = pd.DataFrame(np.array([[1, 2, 3,4, '']
                                        , ['Sync Swap', 'Confirmed $SYNC(04/23)', 6,'', '']
                                        , ['Azuro', 'Confirmed $AZUR(02/23)', 9, '', '']
                                        , ['test','','','','']]),
                   columns=['Project', 'Category', 'Funding', 'Strategy', 'Notes'])

# ------------------------ PLOTS ------------------------------------
# Plots (Gain - Key Statistics)



## ------- TABLES -----------

# --> Top Project Table
rowEvenColor = 'rgba(180, 180, 180, 0.8)'
rowOddColor = 'rgba(117, 117, 117, 0.8)'

fig_l1_table = go.Figure()
fig_l1_table.add_trace(
    go.Table(
        header = dict(
                    values=df_l1_table.columns,
                    line_color='rgba(217, 217, 217, 0.8)',
                    fill_color='rgba(51, 45, 48, 0.8)',
                    align=['left','center'],
                    font=dict(color='white', size=12),
                    height=40

                ),
        cells = dict(
                    values=df_l1_table.transpose().values.tolist(),
                    line_color='rgba(217, 217, 217, 1)',
                    fill_color = [[rowOddColor,rowEvenColor]*40],
                    align=['left', 'center'],
                    font=dict(color='white', size=12),
                    height=30
                )
    )
)

fig_l2_table = go.Figure()
fig_l2_table.add_trace(
    go.Table(
        header = dict(
                    values=df_l2_table.columns,
                    line_color='rgba(217, 217, 217, 0.8)',
                    fill_color='rgba(51, 45, 48, 0.8)',
                    align=['left','center'],
                    font=dict(color='white', size=12),
                    height=40

                ),
        cells = dict(
                    values=df_l2_table.transpose().values.tolist(),
                    line_color='rgba(217, 217, 217, 1)',
                    fill_color = [[rowOddColor,rowEvenColor]*40],
                    align=['left', 'center'],
                    font=dict(color='white', size=12),
                    height=30
                )
    )
)

fig_other_table = go.Figure()
fig_other_table.add_trace(
    go.Table(
        header = dict(
                    values=df_other_table.columns,
                    line_color='rgba(217, 217, 217, 0.8)',
                    fill_color='rgba(51, 45, 48, 0.8)',
                    align=['left','center'],
                    font=dict(color='white', size=12),
                    height=40

                ),
        cells = dict(
                    values=df_other_table.transpose().values.tolist(),
                    line_color='rgba(217, 217, 217, 1)',
                    fill_color = [[rowOddColor,rowEvenColor]*40],
                    align=['left', 'center'],
                    font=dict(color='white', size=12),
                    height=30
                )
    )
)