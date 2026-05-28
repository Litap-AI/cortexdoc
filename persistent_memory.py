import json
import os

MEMORY_FILE = "memory_store.json"

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []

    with open(MEMORY_FILE, "r") as f:

        return json.load(f)

def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:

        json.dump(memory, f, indent=2)

def add_memory(entry):

    memory = load_memory()

    entry["weight"] = 1
    
    entry["source"] = entry.get(
        "source",
        "unknown_document"
    )
      
    entry["modality"] = entry.get(
    "modality",
    "text"

    )


    memory.append(entry)

    save_memory(memory)

def reinforce_memory(query):

    memory = load_memory()

    for item in memory:

        if item["query"] == query:

            item["weight"] += 1

    save_memory(memory)

def get_strong_memories():

    memory = load_memory()

    ranked = sorted(
        memory,
        key=lambda x: x["weight"],
        reverse=True
    )

    return ranked

def decay_memories():

    memory = load_memory()

    updated = []

    for item in memory:

        item["weight"] -= 0.1

        if item["weight"] > 0:

            updated.append(item)

    save_memory(updated)

def compress_memories():

    memory = load_memory()

    unique = {}

    for item in memory:

        query = item["query"]

        if query not in unique:

            unique[query] = item

        else:

            unique[query]["weight"] += item["weight"]

    save_memory(
        list(unique.values())
    )


