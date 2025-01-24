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
import pyquotegen


st.markdown("# Motivational quote")

quote_by_category = pyquotegen.get_quote("motivational")

st.text(quote_by_category)
