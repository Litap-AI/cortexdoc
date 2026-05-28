from persistent_memory import (
    reinforce_memory,
    get_strong_memories
)

reinforce_memory(
    "What military strategies appear repeatedly?"
)

reinforce_memory(
    "What military strategies appear repeatedly?"
)

memories = get_strong_memories()

for item in memories:

    print("=" * 60)

    print("QUERY:")
    print(item["query"])

    print("\nWEIGHT:")
    print(item["weight"])
    