import json
import os

AGENT_MEMORY = "agent_memory.json"

def load_agent_memory():

    if not os.path.exists(AGENT_MEMORY):

        return {}

    with open(AGENT_MEMORY, "r") as f:

        return json.load(f)

def save_agent_memory(memory):

    with open(AGENT_MEMORY, "w") as f:

        json.dump(memory, f, indent=2)

def update_agent_score(
    agent,
    success=True
):

    memory = load_agent_memory()

    if agent not in memory:

        memory[agent] = {

            "success": 0,

            "failure": 0
        }

    if success:

        memory[agent]["success"] += 1

    else:

        memory[agent]["failure"] += 1

    save_agent_memory(memory)

