# day4_app.py
# day4.py
import streamlit as st
import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect("maitri.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        ai_response TEXT,
        timestamp TEXT
    )""")
    conn.commit()
    conn.close()

def save_conversation(user_input, ai_response):
    conn = sqlite3.connect("maitri.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO conversations (user_input, ai_response, timestamp) VALUES (?, ?, ?)",
                (user_input, ai_response, str(datetime.datetime.now())))
    conn.commit()
    conn.close()

def get_conversations():
    conn = sqlite3.connect("maitri.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM conversations ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def run():
    st.title("SAATHI with Memory (Part 4)")

    init_db()

    user_input = st.text_input("Talk to SAATHI")
    if st.button("Send"):
        ai_response = f"SAATHI heard: {user_input}"
        st.write(ai_response)
        save_conversation(user_input, ai_response)

    if st.checkbox("Show Past Conversations"):
        rows = get_conversations()
        for row in rows:
            st.write(f"🕒 {row[3]} — You: {row[1]} | Saathi: {row[2]}")
