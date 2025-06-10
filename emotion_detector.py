from music_suggester import suggest_songs

# Streamlit sidebar for user taste preferences
tastes = st.sidebar.multiselect(
    "🎧 What genres do you like?", 
    ["Pop", "Lofi", "Rap", "DHH", "EDM", "Rock"], 
    default=["Pop", "Rap"]
)
