REQUIRED_FIELDS = [
    "title",
    "hook",
    "body",
    "cta",
    "hashtags",
    "image_prompt",
    "estimated_read_time",
    "difficulty",
    "category"
]

VALID_DIFFICULTY = {
    "Beginner",
    "Intermediate",
    "Advanced"
}

VALID_CATEGORIES = {
    "SQL",
    "Excel",
    "Python",
    "Power BI",
    "Statistics",
    "Data Cleaning",
    "Data Visualization"
}


def validate_post(post: dict):
    """
    Validate the AI-generated post.
    Raises ValueError if anything is invalid.
    """

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in post:
            raise ValueError(f"Missing required field: {field}")

    # Check hashtags
    if not isinstance(post["hashtags"], list):
        raise ValueError("hashtags must be a list")

    if len(post["hashtags"]) != 5:
        raise ValueError("There must be exactly 5 hashtags")

    # Check read time
    if not isinstance(post["estimated_read_time"], int):
        raise ValueError("estimated_read_time must be an integer")

    # Check difficulty
    if post["difficulty"] not in VALID_DIFFICULTY:
        raise ValueError(
            f"Invalid difficulty: {post['difficulty']}"
        )

    # Check category
    if post["category"] not in VALID_CATEGORIES:
        raise ValueError(
            f"Invalid category: {post['category']}"
        )

    return True