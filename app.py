import streamlit as st
import cv2
from deepface import DeepFace
import time
from music_suggester import suggest_songs

# Page config
st.set_page_config(page_title="Moodify 🎭", layout="centered")

# CSS: Fonts, styling, layout
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Playfair+Display:wght@700&family=Poppins:wght@300;600&display=swap');

html, body, #root, .main, .block-container, [data-testid="stAppViewContainer"], [data-testid="stMainContent"], [data-testid="stSidebar"] {
    height: 100%;
    background: #f5f1e9 !important;
    color: #134d38 !important;
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    overflow: auto;
}

[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: transparent !important;
    color: #134d38 !important;
}

.css-18e3th9, .css-1d391kg, .block-container {
    background: transparent !important;
    padding: 0 !important;
    margin: 0 auto !important;
    max-width: 1100px;
    height: auto;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

h1, h2, h3, h4 {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: #134d38;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.05);
    margin-bottom: 0.2rem;
}

.stImage > img {
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(19, 77, 56, 0.3);
    max-width: 900px;
    width: 100%;
    margin-bottom: 1.75rem;
}

.stSelectbox > label {
    display: block;
    text-align: center;
    font-weight: 700;
    font-size: 1.3rem;
    margin-bottom: 0.7rem;
    color: #134d38;
    font-family: 'Playfair Display', serif;
}

.stSelectbox > div > div > select {
    background: #a3bb9a;
    color: #f5f1e9;
    border: none;
    border-radius: 16px;
    padding: 14px 24px;
    font-size: 1.15rem;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(19, 77, 56, 0.35);
    transition: background 0.3s ease, color 0.3s ease;
    cursor: pointer;
    width: 280px;
    margin: 0 auto 2rem auto;
    letter-spacing: 0.05em;
}

.stSelectbox > div > div > select:hover,
.stSelectbox > div > div > select:focus {
    background: #8aa67d;
    outline: none;
}

.emotion-box {
    background: #c6d8c3;
    padding: 1rem 1.5rem;
    border-radius: 20px;
    max-width: 320px;
    margin: 0 auto 3rem auto;
    font-weight: 700;
    font-size: 1.4rem;
    text-align: center;
    box-shadow: 0 6px 20px rgba(19, 77, 56, 0.3);
    letter-spacing: 0.08em;
    color: #134d38;
}

.song-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 24px;
    max-width: 900px;
    margin: 0 auto 3rem auto;
    padding-left: 0;
    width: 100%;
}

.song-list-item {
    padding: 1rem 1.5rem;
    border-radius: 18px;
    background: #d9e4d7;
    box-shadow: 0 4px 15px rgba(19, 77, 56, 0.15);
    text-align: center;
    transition: background 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.song-list-item:hover {
    background: #c0d0b8;
}

.enjoy-text {
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 0.25rem;
    color: #1c3a2d;
    font-style: italic;
    font-family: 'Poppins', sans-serif;
}

.song-link {
    color: #134d38;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.3rem;
    text-decoration: none;
    border-bottom: 2px solid transparent;
    transition: border-color 0.3s ease;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 100%;
    display: inline-block;
}

.song-link:hover {
    border-bottom: 2px solid #5a8a66;
}

.title-container {
    text-align: center;
    margin-bottom: 1rem;
}

.title-container h1 {
    font-size: 3.8rem;
    font-weight: 700;
    color: #134d38;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.07);
}

.title-container p {
    font-size: 1.4rem;
    font-weight: 400;
    letter-spacing: 0.05em;
    color: #134d38;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.03);
    margin-top: -1rem;
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-container">
    <h1>🎭 Moodify</h1>
    <p>Let your face pick the playlist</p>
</div>
""", unsafe_allow_html=True)

tastes = st.selectbox("🎧 Select your favorite genre", ["Pop", "Rap", "DHH", "EDM", "Rock"], index=0)

if "cap" not in st.session_state:
    st.session_state.cap = cv2.VideoCapture(0)

cap = st.session_state.cap
frame_placeholder = st.empty()
emotion_placeholder = st.empty()
song_placeholder = st.empty()

emotion_buffer = []
BUFFER_SIZE = 7
MIN_COUNT_THRESHOLD = 4
last_emotion = None
last_trigger_time = 0
COOLDOWN_SECONDS = 5


def get_smoothed_emotion(buffer):
    if not buffer:
        return ""
    counts = {}
    for emo in buffer:
        counts[emo] = counts.get(emo, 0) + 1
    dominant_emotion = max(counts, key=counts.get)
    if counts[dominant_emotion] >= MIN_COUNT_THRESHOLD:
        return dominant_emotion
    return ""

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("❌ Could not read from webcam")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        current_time = time.time()
        cooldown_remaining = max(0, int(COOLDOWN_SECONDS - (current_time - last_trigger_time)))

        if cooldown_remaining > 0:
            cv2.putText(rgb_frame, f"⏳ Next mood in: {cooldown_remaining}s", (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 100, 100), 3, cv2.LINE_AA)

        frame_placeholder.image(rgb_frame, channels="RGB", use_container_width=True)

        if st.session_state.get("frame_count", 0) % 10 == 0 and cooldown_remaining == 0:
            try:
                result = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion'].capitalize()

                emotion_buffer.append(dominant_emotion)
                if len(emotion_buffer) > BUFFER_SIZE:
                    emotion_buffer.pop(0)

                smoothed_emotion = get_smoothed_emotion(emotion_buffer)

                if smoothed_emotion != last_emotion and smoothed_emotion != "":
                    emotion_placeholder.markdown(
                        f'<div class="emotion-box">😊 Detected Emotion:<br><strong>{smoothed_emotion}</strong></div>',
                        unsafe_allow_html=True)

                    songs = suggest_songs(smoothed_emotion, [tastes])
                    if not songs:
                        songs = suggest_songs(smoothed_emotion, ["Pop"])
                    if not songs:
                        songs = suggest_songs("Neutral", ["Pop", "Rock", "EDM"])

                    if songs:
                        song_list_md = '<div class="song-list">'
                        for s in songs:
                            song_list_md += (
                                '<div class="song-list-item">'
                                '<div class="enjoy-text">Enjoy your song!</div>'
                                f'<a class="song-link" href="{s["url"]}" target="_blank" rel="noopener noreferrer">{s["title"]}</a>'
                                '</div>'
                            )
                        song_list_md += "</div>"
                        song_placeholder.markdown(song_list_md, unsafe_allow_html=True)
                    else:
                        song_placeholder.warning("No songs found for this emotion + genre combo.")

                    last_emotion = smoothed_emotion
                    last_trigger_time = current_time

            except Exception as e:
                st.error(f"⚠️ Detection error: {e}")

        st.session_state.frame_count = st.session_state.get("frame_count", 0) + 1
        time.sleep(0.03)

except KeyboardInterrupt:
    cap.release()
    st.write("Webcam stopped.")

st.markdown("""
<hr style="margin-top: 2rem; margin-bottom: 1rem; border: none; height: 1px; background: #bcd2bc;"/>
<div style="text-align: center; margin-bottom: 1.5rem;">
    <p style="font-family: 'Poppins', sans-serif; font-size: 1.1rem; color: #134d38; font-weight: 500; margin-bottom: 0.5rem;">
        Connect with me:
    </p>
    <a href="https://www.linkedin.com/in/your-linkedin-id" target="_blank" style="margin: 0 12px;">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="32" />
    </a>
    <a href="https://github.com/your-github-id" target="_blank" style="margin: 0 12px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111432.png" width="32" />
    </a>
    <a href="https://www.instagram.com/your-instagram-id" target="_blank" style="margin: 0 12px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="32" />
    </a>
</div>
""", unsafe_allow_html=True)