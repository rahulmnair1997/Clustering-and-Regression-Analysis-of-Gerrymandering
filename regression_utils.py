import numpy as np
import pandas as pd
import geopandas
import json, math, random, shapely, shapefile, plotly, geopandas
from shapely.geometry import Polygon

def format_PA_data(geo_df_PA): 
    geo_df_PA_info = geo_df_PA.groupby('COUNTYFP10').sum()

    data_df = geo_df_PA_info[['NH_WHITE', 'NH_BLACK', 'NH_AMIN',
       'NH_ASIAN', 'NH_NHPI', 'NH_OTHER', 'NH_2MORE', 'HISP', 'H_WHITE',
       'H_BLACK', 'H_AMIN', 'H_ASIAN', 'H_NHPI', 'H_OTHER', 'H_2MORE',
       'HVAP', 'WVAP', 'BVAP', 'AMINVAP', 'ASIANVAP', 'NHPIVAP', 'OTHERVAP',
       '2MOREVAP']]

    totpop_lst = ['NH_WHITE', 'NH_BLACK', 'NH_AMIN',
        'NH_ASIAN', 'NH_NHPI', 'NH_OTHER', 'NH_2MORE', 'HISP', 'H_WHITE',
        'H_BLACK', 'H_AMIN', 'H_ASIAN', 'H_NHPI', 'H_OTHER', 'H_2MORE']
    for feature in totpop_lst: 
        data_df[feature] = geo_df_PA_info[feature] / geo_df_PA_info['TOTPOP']

    vap_lst = ['HVAP', 'WVAP', 'BVAP', 'AMINVAP', 'ASIANVAP', 'NHPIVAP', 'OTHERVAP',
        '2MOREVAP']
    for feature in vap_lst: 
        data_df[feature] = geo_df_PA_info[feature] / geo_df_PA_info['VAP']


    data_df['PRES12D_prop'] = geo_df_PA_info['PRES12D'] / (geo_df_PA_info['PRES12D'] + geo_df_PA_info['PRES12R'])
    data_df['PRES12R_prop'] = geo_df_PA_info['PRES12R'] / (geo_df_PA_info['PRES12D'] + geo_df_PA_info['PRES12R'])


    data_df['T16PRESD_prop'] = geo_df_PA_info['T16PRESD'] / (geo_df_PA_info['T16PRESD'] + geo_df_PA_info['T16PRESR'])
    data_df['T16PRESR_prop'] = geo_df_PA_info['T16PRESR'] / (geo_df_PA_info['T16PRESD'] + geo_df_PA_info['T16PRESR'])

    return data_df