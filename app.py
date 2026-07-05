import sqlite3
import pandas as pd
import streamlit as st

from src.pipeline import ContentPipeline
from src.topic_manager import get_next_topic

st.set_page_config(page_title="LinkedIn AI Generator", layout="wide")

st.title("🤖 LinkedIn AI Generator")

# -----------------------------
# Next Topic
# -----------------------------

next_topic = get_next_topic()

if next_topic:
    st.success(f"Next Topic: {next_topic['topic']}")
else:
    st.warning("No pending topics.")

# -----------------------------
# Generate Button
# -----------------------------

if st.button("Generate Next Post"):

    pipeline = ContentPipeline()
    pipeline.run()

    st.success("Post Generated!")

# -----------------------------
# Database
# -----------------------------

conn = sqlite3.connect("data/posts.db")

df = pd.read_sql_query(
    """
    SELECT
        generated_at,
        topic,
        category,
        title
    FROM posts
    ORDER BY id DESC
    LIMIT 10
    """,
    conn
)

st.subheader("Recent Posts")

st.dataframe(df, use_container_width=True)

# -----------------------------
# Preview
# -----------------------------

if not df.empty:

    latest = pd.read_sql_query(
        """
        SELECT *
        FROM posts
        ORDER BY id DESC
        LIMIT 1
        """,
        conn
    )

    row = latest.iloc[0]

    st.subheader("Latest Post")

    st.markdown(f"## {row['title']}")

    st.write(row["body"])

    st.write(row["cta"])

    st.write(row["hashtags"])

conn.close()