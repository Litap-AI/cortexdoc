from persistent_memory import (
    load_memory
)

def reflect_on_history():

    memory = load_memory()

    print("\nPAST COGNITIVE HISTORY:\n")

    for item in memory[-5:]:

        print("=" * 60)

        print("QUERY:")

        print(item["query"])

        print("\nCONSENSUS:")

        print(item["consensus"])

        print("\nEVALUATION:")

        print(item["evaluation"])
        