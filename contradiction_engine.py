from persistent_memory import (
    load_memory
)

def detect_contradictions():

    memory = load_memory()

    contradictions = []

    for i in range(len(memory)):

        for j in range(i + 1, len(memory)):

            item1 = memory[i]
            item2 = memory[j]

            query1 = item1["query"]
            query2 = item2["query"]

            answer1 = item1["answer"]
            answer2 = item2["answer"]

            # Simple contradiction heuristic
            if query1 == query2:

                if answer1 != answer2:

                    contradictions.append({

                        "query": query1,

                        "answer_1": answer1,

                        "answer_2": answer2,

                        "source_1": item1["source"],

                        "source_2": item2["source"]
                    })

    return contradictions
