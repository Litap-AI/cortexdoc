from agents import (
    ReasoningAgent,
    SkepticAgent,
    PlannerAgent,
    EvidenceAgent
)

from debate_engine import run_debate
from moderator_agent import ModeratorAgent
from consensus_engine import build_consensus

from persistent_memory import add_memory


def cognitive_society(query, paragraphs):

    context = {
        "query": query,
        "paragraphs": paragraphs
    }

    reasoning_agent = ReasoningAgent(
        "Reasoner"
    )

    answer = reasoning_agent.think(
        context
    )

    skeptic = SkepticAgent(
        "Skeptic"
    )

    critique = skeptic.think({
        "answer": answer
    })

    planner = PlannerAgent(
        "Planner"
    )

    plan = planner.think({
        "answer": answer
    })

    evidence_agent = EvidenceAgent(
        "Evidence"
    )

    evidence = evidence_agent.think({
        "query": query
    })

    debate = run_debate(
        answer,
        critique,
        evidence
    )

    moderator = ModeratorAgent()

    evaluation = moderator.evaluate(
        answer,
        critique,
        evidence
    )

    consensus = build_consensus(
        answer,
        critique,
        evidence
    )

    # MEMORY STORAGE HERE
    add_memory({

        "query": query,

        "answer": answer,

        "consensus": consensus,

        "evaluation": evaluation,

        "source": "sample.pdf"

        
    })

    return {

        "answer": answer,

        "critique": critique,

        "plan": plan,

        "evidence": evidence,

        "debate": debate,

        "evaluation": evaluation,

        "consensus": consensus
    }
