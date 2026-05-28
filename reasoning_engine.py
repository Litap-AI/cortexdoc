import ollama

def reason_over_context(
    query,
    contexts
):

    combined_context = "\n".join(contexts)

    prompt = f"""
Question:
{query}

Context:
{combined_context}

Provide a detailed analytical answer.
"""

    response = ollama.chat(

        model='phi3',

        messages=[

            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']
