from tools import search_memory

class CognitiveAgent:

    def __init__(self, name):

        self.name = name

    def think(self, context):

        raise NotImplementedError

class PlannerAgent(CognitiveAgent):

    def think(self, context):

        answer = context["answer"]

        related = search_memory(
            answer
        )

        response = f"""

RESEARCH DIRECTIONS:

1. Investigate related concepts
2. Compare supporting evidence
3. Explore recurring themes

RELATED CONTEXT:

{related[:2]}
"""

        return response
    

    
from reasoning_engine import (
    reason_over_context
)

class ReasoningAgent(CognitiveAgent):

    def think(self, context):

        query = context["query"]

        paragraphs = context["paragraphs"]

        return reason_over_context(
            query,
            paragraphs
        )
    
class SkepticAgent(CognitiveAgent):

    def think(self, context):

        answer = context["answer"]

        critique = f"""
Potential weaknesses in reasoning:

- Is evidence sufficient?
- Are there contradictory interpretations?
- Could context be incomplete?

Analyzed Answer:
{answer}
"""

        return critique
    
class EvidenceAgent(CognitiveAgent):

    def think(self, context):

        query = context["query"]

        evidence = search_memory(query)

        return {
            "evidence": evidence[:3]
        }
