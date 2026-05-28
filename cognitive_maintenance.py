from persistent_memory import (
    decay_memories,
    compress_memories,
    get_strong_memories
)

def maintain_cognition():

    print("\nRunning memory decay...\n")

    decay_memories()

    print("Compressing memory...\n")

    compress_memories()

    print("Top active memories:\n")

    memories = get_strong_memories()

    for item in memories[:5]:

        print("=" * 50)

        print(item["query"])

        print("Weight:", round(item["weight"], 2))

        