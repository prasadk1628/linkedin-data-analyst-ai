from pathlib import Path
from datetime import datetime
import csv

TOPICS_FILE = Path("data/topics.csv")


def get_next_topic():
    """
    Return the first pending topic.
    """

    with open(TOPICS_FILE, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["status"].lower() == "pending":
                return row

    return None


def mark_completed(topic_name):
    """
    Mark a topic as completed.
    """

    rows = []

    with open(TOPICS_FILE, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["topic"] == topic_name:

                row["status"] = "completed"

                row["last_generated"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

            rows.append(row)

    with open(TOPICS_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "topic",
                "category",
                "status",
                "last_generated"
            ]
        )

        writer.writeheader()

        writer.writerows(rows)