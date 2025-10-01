import json
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='mcp_client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_input_json(file_path='mcp_input.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        logging.info("Successfully loaded JSON input.")
        return data
    except Exception as e:
        logging.error(f"Error loading JSON input: {e}")
        raise

def retrieve_context(context_sources):
    context = ""
    for file_name in context_sources:
        try:
            with open(file_name, 'r') as f:
                content = f.read()
                context += f"\n--- Content from {file_name} ---\n{content}\n"
            logging.info(f"Successfully loaded context from {file_name}.")
        except Exception as e:
            logging.warning(f"Could not read context file {file_name}: {e}")
    return context

def assemble_prompt(query, context, inject_facts):
    if inject_facts and context:
        prompt = f"Context:\n{context}\n\nQuery:\n{query}"
    else:
        prompt = f"Query:\n{query}"
    logging.info("Prompt assembled successfully.")
    return prompt

def simulate_ollama_response(prompt):
    response = f"Ollama response to prompt:\n{prompt[:500]}...\n[Response truncated for brevity]"
    logging.info("Simulated query to Ollama completed.")
    return response

def save_response(response):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"ollama_response_{timestamp}.txt"
    try:
        with open(file_name, 'w') as f:
            f.write(response)
        logging.info(f"Response saved to {file_name}")
    except Exception as e:
        logging.error(f"Error saving response: {e}")
        raise

def main():
    try:
        # Load input
        input_data = load_input_json()
        query = input_data.get("query", "")
        context_sources = input_data.get("context_sources", [])
        inject_facts = input_data.get("inject_facts", False)

        # Retrieve context from files
        context = retrieve_context(context_sources)

        # Assemble prompt
        prompt = assemble_prompt(query, context, inject_facts)

        # Simulate Ollama response
        response = simulate_ollama_response(prompt)

        # Save response
        save_response(response)

    except Exception as e:
        logging.error(f"Unhandled exception: {e}")

if __name__ == "__main__":
    main()