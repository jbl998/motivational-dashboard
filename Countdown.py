# External modules
import time

import pandas as pd
import streamlit as st
import datetime as dt
import numpy as np
import altair as alt
import base64
# Internal modules
import config as cfg
from Timer import dfLayoff

now = dt.datetime.now()
yday = now - dt.timedelta(days=1)
dfLayoff = pd.read_csv(f"{cfg.pathCSV}/layoffs.csv")
dfLayoff["date"] = pd.to_datetime(dfLayoff["date"], format="%Y-%m-%d")
dfLayoffNow = dfLayoff.copy()
dfLayoffNow['date'] = dfLayoffNow['date'].dt.normalize() + pd.Timedelta(hours=9)
dfLayoffNow = dfLayoffNow.loc[dfLayoffNow["date"] >= now]
nextLayoffDT = min(dfLayoffNow['date'])
timeToNextLayoff = nextLayoffDT - now
comp = timeToNextLayoff.components

st.markdown("# Countdown to next layoffs")

img="Countdown"
image_path = f"{cfg.pathIMG}/{cfg.imgInfo[img]['filename']}"
fontSize = cfg.imgInfo[img]['fontsize']
fontColor = cfg.imgInfo[img]['fontcolor']
textPosition = cfg.imgInfo[img]['textposition']
imgWidth = cfg.imgInfo[img]["imgwidth"]

with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()


st.markdown(
    f"""
    <style>
    .image-container {{
        position: relative;
        text-align: left;
        color: white;
    }}
    .image-container img {{
        width: {imgWidth}px;
        height: auto;
    }}
    .image-text1 {{
        position: absolute;
        top: {textPosition[0]["top"]}px;
        left: {textPosition[0]["left"]}px;
        transform: translate(-50%, -50%);
        font-size: {fontSize}px; /* Font size relative to the container width */
        color: {fontColor};
        font-weight: bold;
    }}
    </style>
    <div class="image-container">
        <img src="data:image/png;base64,{encoded_image}" alt="Countodwn to next layoffs">
        <div class="image-text1">{f'{comp.days} days, {comp.hours:02}:{comp.minutes:02}:{comp.seconds:02}'}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if len(dfLayoffNow)>0:
    time.sleep(1)
    st.rerun()
else:
    st.balloons()