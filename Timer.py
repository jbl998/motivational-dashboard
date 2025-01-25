# External modules
import pandas as pd
import streamlit as st
import datetime as dt
import numpy as np
import altair as alt
import base64
# Internal modules
import config as cfg

now = dt.datetime.now()
yday = now - dt.timedelta(days=1)


dfLayoff = pd.read_csv(f"{cfg.pathCSV}/layoffs.csv")
dfLayoff["date"] = pd.to_datetime(dfLayoff["date"], format="%Y-%m-%d")

dfLayoffNow = dfLayoff.copy()
dfLayoffNow["date"] = dfLayoffNow.loc[dfLayoffNow["date"] <= now]
layoffDT = max(dfLayoffNow["date"])

dfLayoffYDAY = dfLayoff.copy()
dfLayoffYDAY["date"] = dfLayoffYDAY.loc[dfLayoffYDAY["date"] <= yday]
layoffDTYDAY = max(dfLayoffYDAY["date"])


daysCount = int(np.floor((now - layoffDT).total_seconds() / 86400.0))
daysCountOld = int(np.floor((yday - layoffDTYDAY).total_seconds() / 86400.0))


st.markdown("# Days since last layoffs")

img = st.selectbox("Select image", cfg.imgInfo.keys())

image_path = f"{cfg.pathIMG}/{cfg.imgInfo[img]['filename']}"
fontSize = cfg.imgInfo[img]['fontsize']
fontColor = cfg.imgInfo[img]['fontcolor']
textPosition = cfg.imgInfo[img]['textposition']
imgWidth = cfg.imgInfo[img]["imgwidth"]

# Encode the image in Base64
with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()


# Render the image with text overlay
if len(textPosition) == 1:
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
            <img src="data:image/png;base64,{encoded_image}" alt="Layoff Meme">
            <div class="image-text1">{daysCount}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif len(textPosition) == 2:
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            text-align: left;
            color: white;
        }}
        .image-container img {{
            width: 612px;
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
        .image-text2 {{
            position: absolute;
            top: {textPosition[1]["top"]}px;
            left: {textPosition[1]["left"]}px;
            transform: translate(-50%, -50%);
            font-size: {fontSize}px; /* Font size relative to the container width */
            color: #000000;
            font-weight: bold;
        }}
        </style>
        <div class="image-container">
            <img src="data:image/png;base64,{encoded_image}" alt="Layoff Meme">
            <div class="image-text1">{daysCountOld}</div>
            <div class="image-text2">{daysCount}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Write info
st.text(
    f"Last round of layoffs were on the {layoffDT.strftime('%d/%m/%Y')}"
)


expander_timer = st.expander("See previous dates")
expander_timer.dataframe(dfLayoff)