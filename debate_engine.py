from communication_engine import Message

def run_debate(
    answer,
    critique,
    evidence
):

    messages = []

    messages.append(

        Message(
            "Reasoner",
            "Skeptic",
            answer
        )
    )

    messages.append(

        Message(
            "Skeptic",
            "Reasoner",
            critique
        )
    )

    messages.append(

        Message(
            "EvidenceAgent",
            "Moderator",
            str(evidence)
        )
    )

    return messages
