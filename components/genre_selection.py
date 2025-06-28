import streamlit as st

def genre_selector():
    st.subheader("Select Your Favorite Genres")
    genres = ["EDM", "Rock", "Jazz", "House", "Indie", "Fusion", "Trance", "Electronic", "World"]
    selected = st.multiselect("Choose genres you love:", genres)
    return selected