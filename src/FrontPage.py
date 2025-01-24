from io import StringIO
import json
import pandas as pd
import streamlit as st
import requests
import datetime as dt
import numpy as np
import time

# Test
import subprocess
import sys

import config as cfg

st.set_page_config(page_title="Motivational Dashboard", page_icon="")

pages = [st.Page("Timer.py"), st.Page("Quotes.py")]

pg = st.navigation(pages)
pg.run()
