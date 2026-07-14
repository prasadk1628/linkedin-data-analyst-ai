from pathlib import Path
from datetime import datetime
import csv
import json

DATA_DIR = Path("data")
POSTS_DIR = Path("generated_posts")

DATA_DIR.mkdir(exist_ok=True)
POSTS_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "posts.csv"

HEADER = [
    "generated_at",
    "topic",
    "title",
    "hook",
    "body",
    "cta",
    "hashtags",
    "image_specification",
    "estimated_read_time",
    "difficulty",
    "category",
    "model"
]


def save_post(post: dict, topic: str, model: str):

    timestamp = datetime.now()

    filename = (
        POSTS_DIR /
        f"{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    )

    # ---------- Save readable text ----------

    with open(filename, "w", encoding="utf-8") as f:

        f.write(f"TITLE\n\n{post['title']}\n\n")

        f.write(f"HOOK\n\n{post['hook']}\n\n")

        f.write(f"BODY\n\n{post['body']}\n\n")

        f.write(f"CTA\n\n{post['cta']}\n\n")

        f.write("HASHTAGS\n\n")

        for tag in post["hashtags"]:
            f.write(tag + "\n")

        f.write("\n")

        f.write("IMAGE SPECIFICATION\n\n")

        f.write(
            json.dumps(
                post["image_specification"],
                indent=4
            )
        )

    # ---------- Save CSV ----------

    row = [
        timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        topic,
        post["title"],
        post["hook"],
        post["body"],
        post["cta"],
        ",".join(post["hashtags"]),
        json.dumps(post["image_specification"]),
        post["estimated_read_time"],
        post["difficulty"],
        post["category"],
        model
    ]

    file_exists = CSV_FILE.exists()

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(HEADER)

        writer.writerow(row)

    print("✅ Content saved successfully.")