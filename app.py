import numpy as np
import requests
import streamlit as st

ENDPOINT = "https://cataas.com/cat"
N_COLS = 4

with st.sidebar:
    st.header("Configuration")
    n_photos = st.slider("Number of cat photos:", 4, 64, 16)
    with st.beta_expander("About this app"):
        st.markdown("It's about cats :cat:!")
    st.caption("Source: https://cataas.com/#/")

st.title("Choose your favorite cat :cat:")

cat_images = [requests.get("https://cataas.com/cat?width=400&height=400").content for i in range(n_photos)]
n_rows = 1 + len(cat_images) // N_COLS
rows = [st.beta_container() for _ in range(n_rows)]
cols_per_row = [r.beta_columns(N_COLS) for r in rows]

for image_index, cat_image in enumerate(cat_images):
    with rows[image_index // N_COLS]:
        cols_per_row[image_index // N_COLS][image_index % N_COLS].image(cat_image)
