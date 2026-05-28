from vision_engine import (
    analyze_image
)

from reasoning_engine import (
    reason_over_context
)

def visual_reasoning(
    image_path,
    query
):

    visual_context = analyze_image(
        image_path
    )

    reasoning = reason_over_context(
        query,
        [visual_context]
    )

    return reasoning
