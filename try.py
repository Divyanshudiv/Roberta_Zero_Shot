import requests
import json

def interact_with_ollama(prompt, model="gemma2", system_prompt=None, url="http://localhost:8000"):
    """
    Send a prompt to Ollama and retrieve its response.

    Args:
        prompt (str): The prompt to send to the model
        model (str): The name of the model to use (default: "llama2")
        system_prompt (str, optional): System prompt to set context/behavior
        url (str): The URL where Ollama is running (default: http://localhost:11434)

    Returns:
        str: The response from the model
    """
    # Prepare the request payload
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    # Add system prompt if provided
    if system_prompt:
        payload["system"] = system_prompt
    
    try:
        # Send POST request to Ollama
        response = requests.post(f"{url}/api/generate", json=payload)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse the response
        result = response.json()
        return result.get('response', '')
        
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Basic usage
    response = interact_with_ollama("What is the capital of France?")
    print(response)
    
    # Usage with system prompt
    response = interact_with_ollama(
        prompt="What is the capital of France?",
        model="mistral",
        system_prompt="You are a helpful assistant who provides concise answers."
    )
    print(response)