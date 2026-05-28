from reasoning_engine import (
    revise_reasoning
)

def build_consensus(
    answer,
    critique,
    evidence
):

    revised = revise_reasoning(
        answer,
        critique,
        evidence
    )

    return revised
