class ModeratorAgent:

    def evaluate(
        self,
        answer,
        critique,
        evidence
    ):

        confidence = 0

        if len(evidence) > 0:
            confidence += 1

        if "insufficient" not in critique.lower():
            confidence += 1

        if len(answer) > 100:
            confidence += 1

        if confidence == 3:
            verdict = "HIGH CONFIDENCE"

        elif confidence == 2:
            verdict = "MEDIUM CONFIDENCE"

        else:
            verdict = "LOW CONFIDENCE"

        return {
            "confidence": verdict,
            "score": confidence
        }
    