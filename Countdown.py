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

st.markdown("# Countdown to next layoffs")

now = dt.datetime.now()
today = dt.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
yday = now - dt.timedelta(days=1)
dfLayoff = pd.read_csv(f"{cfg.pathCSV}/layoffs.csv")
dfLayoff["date"] = pd.to_datetime(dfLayoff["date"], format="%Y-%m-%d")
dfLayoffNow = dfLayoff.copy()

dfLayoffNow = dfLayoffNow.loc[dfLayoffNow["date"] >= today]
dfLayoffNow['date'] = dfLayoffNow['date'].dt.normalize() + pd.Timedelta(hours=9)
if len(dfLayoffNow) == 0:
    st.markdown(
        """
        (Un)fortunately this dashboard does not know of any future layoffs.
        
        Stay tuned for more exciting news!
        """
    )
elif len(dfLayoffNow) > 0:
    nextLayoffDT = min(dfLayoffNow['date'])
    timeToNextLayoff = nextLayoffDT - now
    comp = timeToNextLayoff.components
    img="Countdown"
    image_path = f"{cfg.pathIMG}/{cfg.imgInfo[img]['filename']}"
    fontSize = cfg.imgInfo[img]['fontsize']
    fontColor = cfg.imgInfo[img]['fontcolor']
    textPosition = cfg.imgInfo[img]['textposition']
    imgWidth = cfg.imgInfo[img]["imgwidth"]

    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    if timeToNextLayoff.total_seconds() >=0:
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
                <img src="data:image/png;base64,{encoded_image}" alt="Countdown to next layoffs">
                <div class="image-text1">{f'{comp.days} days, {comp.hours:02}:{comp.minutes:02}:{comp.seconds:02}'}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
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
                <img src="data:image/png;base64,{encoded_image}" alt="Countdown to next layoffs">
                <div class="image-text1">BOOM</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.balloons()

    if len(dfLayoffNow)>0:
        time.sleep(1)
        st.rerun()