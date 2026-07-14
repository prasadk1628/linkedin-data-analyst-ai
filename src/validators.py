REQUIRED_FIELDS = [
    "title",
    "hook",
    "body",
    "cta",
    "hashtags",
    "image_specification",
    "estimated_read_time",
    "difficulty",
    "category"
]

IMAGE_SPECIFICATION_FIELDS = [
    "title",
    "purpose",
    "audience",
    "difficulty",
    "main_concept",
    "learning_objective",
    "key_concepts",
    "primary_visual",
    "supporting_visuals",
    "visual_metaphor",
    "style",
    "color_palette",
    "aspect_ratio",
    "branding"
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

    # ---------- Required fields ----------

    for field in REQUIRED_FIELDS:
        if field not in post:
            raise ValueError(f"Missing required field: {field}")

    # ---------- Hashtags ----------

    if not isinstance(post["hashtags"], list):
        raise ValueError("hashtags must be a list")

    if len(post["hashtags"]) != 5:
        raise ValueError("There must be exactly 5 hashtags")

    # ---------- Image Specification ----------

    if not isinstance(post["image_specification"], dict):
        raise ValueError("image_specification must be an object")

    for field in IMAGE_SPECIFICATION_FIELDS:
        if field not in post["image_specification"]:
            raise ValueError(
                f"Missing image specification field: {field}"
            )

    if not isinstance(
        post["image_specification"]["key_concepts"],
        list
    ):
        raise ValueError(
            "image_specification.key_concepts must be a list"
        )

    if not isinstance(
        post["image_specification"]["supporting_visuals"],
        list
    ):
        raise ValueError(
            "image_specification.supporting_visuals must be a list"
        )

    # ---------- Read time ----------

    if not isinstance(post["estimated_read_time"], int):
        raise ValueError("estimated_read_time must be an integer")

    # ---------- Difficulty ----------

    if post["difficulty"] not in VALID_DIFFICULTY:
        raise ValueError(
            f"Invalid difficulty: {post['difficulty']}"
        )

    # ---------- Category ----------

    if post["category"] not in VALID_CATEGORIES:
        raise ValueError(
            f"Invalid category: {post['category']}"
        )

    return True