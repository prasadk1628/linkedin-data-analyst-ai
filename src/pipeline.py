from src.topic_manager import get_next_topic, mark_completed
from src.ai_generator import generate_post
from src.file_manager import save_post
from src.config import MODEL_NAME
from src.database import initialize_database, insert_post


class ContentPipeline:

    def run(self):

        # Create database and table if they don't exist
        initialize_database()

        next_topic = get_next_topic()

        if not next_topic:
            print("🎉 No pending topics found.")
            return

        topic = next_topic["topic"]

        print(f"📌 Selected Topic: {topic}")

        post = generate_post(topic)

        save_post(
            post=post,
            topic=topic,
            model=MODEL_NAME
        )

        insert_post(post, topic, MODEL_NAME)

        mark_completed(topic)

        print("✅ Pipeline completed successfully.")