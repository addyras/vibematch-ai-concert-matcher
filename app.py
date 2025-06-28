import streamlit as st
<<<<<<< HEAD
from components.genre_selection import genre_selector
from components.concerts import load_concerts, filter_concerts_by_genre

st.set_page_config(page_title="VibeMatch – Concert Matcher", page_icon="🎶")
st.title("🎵 VibeMatch – Find Your Concert Match")

st.markdown("Welcome to VibeMatch – where music meets connection.")

selected_genres = genre_selector()
concerts = load_concerts()

if selected_genres:
    st.subheader("🎫 Concerts Matching Your Vibe")
    filtered = filter_concerts_by_genre(concerts, selected_genres)
    if filtered:
        for c in filtered:
            st.markdown(f"**{c['name']}** in _{c['location']}_ on **{c['date']}** – _Genres: {', '.join(c['genre'])}_")
    else:
        st.info("No matching concerts found. Try different genres.")
else:
    st.info("Select genres to see matching concerts.")
=======

st.set_page_config(page_title="VibeMatch", layout="centered")
st.title("🎵 VibeMatch – Find Your Concert Match")

st.write("Welcome to the MVP of VibeMatch. This version allows users to pick music genres, select concerts, and preview potential matches.")

st.info("🚧 This is a work in progress. Matching logic, chat, and UI features will be added in future commits.")
>>>>>>> 7475f8117a76f7105af90c4a0a990e598bbc04e5
