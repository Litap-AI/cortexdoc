from memory_engine import query_memory
from reasoning_engine import reason_over_context

def cognitive_loop(query, iterations=2):

    current_query = query

    final_answer = None

    for step in range(iterations):

        results = query_memory(
            current_query
        )

        contexts = results["documents"][0]

        answer = reason_over_context(
            current_query,
            contexts
        )

        print("\n" + "=" * 60)

        print(f"ITERATION {step+1}")

        print("=" * 60)

        print(answer)

        current_query = (
            f"Refine and verify: {answer}"
        )

        final_answer = answer

    return final_answer
