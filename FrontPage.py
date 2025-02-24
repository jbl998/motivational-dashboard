# External modules
import pandas as pd
import streamlit as st
import datetime as dt
import numpy as np
# Internal modules
import config as cfg

st.set_page_config(page_title="Motivational Dashboard", page_icon="")

dfLayoff = pd.read_csv(f"{cfg.pathCSV}/layoffs.csv")
dfLayoff["date"] = pd.to_datetime(dfLayoff["date"], format="%Y-%m-%d")
dfLayoff['date'] = dfLayoff['date'].dt.normalize() + pd.Timedelta(hours=9)
filtered_df = dfLayoff.loc[(dfLayoff['date'] >= dt.datetime.now())]

pages = [st.Page("Timer.py"), st.Page("Countdown.py"), st.Page("Quotes.py")]


pg = st.navigation(pages)
pg.run()


with st.sidebar:
    expander_sidebar = st.expander("Settings")
    pw_input = expander_sidebar.text_input("Password", type="password")
    if pw_input == "BetterPassword69":
        new_dt = expander_sidebar.date_input("Add new layoff date")
        new_dt_DT = dt.datetime(new_dt.year, new_dt.month,new_dt.day,0,0,0,0)
        submit = expander_sidebar.button("Add date")
        if submit:
            dfLayoff = pd.read_csv(f"{cfg.pathCSV}/layoffs.csv")
            dfLayoff = pd.concat([dfLayoff, pd.DataFrame([new_dt], columns=["date"])])
            dfLayoff["date"] = pd.to_datetime(dfLayoff["date"], format="%Y-%m-%d")
            dfLayoff.sort_values(by=["date"],inplace=True)
            dfLayoff.drop_duplicates(inplace=True)
            dfLayoff.to_csv(f"{cfg.pathCSV}/layoffs.csv", index=False)