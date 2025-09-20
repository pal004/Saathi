import streamlit as st
from PIL import Image
import numpy as np
import random

# Try to import DeepFace
try:
    from deepface import DeepFace
    DEEPFACE_AVAILABLE = True
except Exception:
    DEEPFACE_AVAILABLE = False



def analyze_emotion_with_deepface(pil_img: Image.Image):
    """
    Analyze emotion using DeepFace if available,
    else return 'neutral'.
    """
    try:
        img_arr = np.array(pil_img.convert("RGB"))
        result = DeepFace.analyze(img_arr, actions=["emotion"], enforce_detection=False)

        # DeepFace sometimes returns a list
        if isinstance(result, list):
            result = result[0]

        emo = result.get("dominant_emotion", "neutral")
        return emo.lower()
    except Exception:
        return "neutral"


# ---------------- Persona Templates ----------------
TEMPLATES = {
    "Zen": {
        "happy": "You're looking calm. Want a 2-minute breathing reset?",
        "neutral": "Low energy sensed. Shall we do a short pranayama?",
        "sad": "I notice low mood. Let's try 4-4-8 breathing for 1 minute.",
        "angry": "You seem tense. A quick stretch + breathing might help.",
        "surprise": "Something unexpected happened? Want to talk it out?",
        "fear": "Grounding breathing can help. Ready to try?",
        "disgust": "Feeling off? Small breathing reset might help."
    },
    "Coach": {
        "happy": "Great energy! Keep it up — small wins stack.",
        "neutral": "Let's do two micro-tasks and a 5-minute break.",
        "sad": "You can do this — 5-minute stretch then a small task.",
        "angry": "Channel that energy: finish one quick task, then breathe.",
        "surprise": "Use this alertness to tackle a short task now.",
        "fear": "Focus on one tiny doable action, then breathe.",
        "disgust": "Pivot to a different task to reset your mind."
    },
    "Buddy": {
        "happy": "Looking good! Want a cheeky joke or a short story?",
        "neutral": "Hey — want a short chit-chat? Tell me one good thing.",
        "sad": "That's rough. Want a joke or should I just listen?",
        "angry": "Ugh. Want me to roast the problem or play chill music?",
        "surprise": "Woah! Spill the tea — I'm all ears.",
        "fear": "Small steps. Want me to distract with a meme or a joke?",
        "disgust": "Gross day — vent or want a dumb space joke?"
    }
}

JOKES = [
    "Why did the astronaut bring a broom? To sweep up the space dust!",
    "Space travel tip: don't forget to pack your 'space' socks.",
    "I tried to attend a space party but there was no atmosphere."
]


# ---------------- MAIN APP ----------------
def run():
    st.title("Emotion Recognition (Part 2)")
    st.write("Upload an image and Saathi will sense your emotion 🤖")

    uploaded = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])

    if uploaded:
        pil_img = Image.open(uploaded)
        st.image(pil_img, caption="Your Image", use_container_width=True)

        # Use DeepFace if installed, else random fallback
        if DEEPFACE_AVAILABLE:
            emotion = analyze_emotion_with_deepface(pil_img)
        else:
            emotion = random.choice(
                ["happy", "sad", "neutral", "angry", "fear", "surprise", "disgust"]
            )

        st.success(f"Detected Emotion: **{emotion}**")

        persona = st.radio("Choose SAATHI's persona", ["Zen", "Coach", "Buddy"])

        suggestion = TEMPLATES.get(persona, {}).get(emotion, "Let's take a mindful pause together.")
        st.info(f"SAATHI says: {suggestion}")

        # Buddy persona adds a joke
        if persona == "Buddy" and emotion in ["sad", "angry", "disgust"]:
            st.write("Here’s something to cheer you up 🤭:")
            st.write(random.choice(JOKES))
