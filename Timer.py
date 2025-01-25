from io import StringIO
import json
import pandas as pd
import streamlit as st
import requests
import datetime as dt
import numpy as np
import time
import altair as alt
import base64

import config as cfg

layoffDT = dt.datetime(2025, 1, 21, 8, 0, 0)
now = dt.datetime.now()
daysCount = int(np.floor((now - layoffDT).total_seconds() / 86400.0))


st.markdown("# Days since last layoffs")

image_path = f"{cfg.pathIMG}/layoff_meme_blank.png"
# Encode the image in Base64
with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()

# Render the image with text overlay
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
    .image-text {{
        position: absolute;
        top: 114px;
        left: 196px;
        transform: translate(-50%, -50%);
        font-size: 24px; /* Font size relative to the container width */
        color: #9ef8eb;
        font-weight: bold;
    }}
    </style>
    <div class="image-container">
        <img src="data:image/png;base64,{encoded_image}" alt="Layoff Meme">
        <div class="image-text">{daysCount}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Write info
st.text(
    f"Last round of layoffs were on the {layoffDT.strftime('%d/%m/%Y')} at {layoffDT.strftime('%H:%M')}"
)
