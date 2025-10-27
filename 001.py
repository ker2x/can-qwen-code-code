#!/usr/bin/env python3
import requests
import sys
import argparse
import os

def chat_with_ollama(model, prompt, host='192.168.1.17', port=11434):
    """Send a prompt to Ollama and return the response."""
    try:
        response = requests.post(
            f'http://{host}:{port}/api/generate',
            json={
                'model': model,
                'prompt': prompt,
                'stream': False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"
    except KeyError:
        return "Error: Unexpected response format from Ollama"

def main():
    """Main chat loop."""
    parser = argparse.ArgumentParser(description='Ollama Chat CLI')
    parser.add_argument('--model', '-m', default='qwen3-coder',
                       help='Model to use (default: qwen3-coder)')
    parser.add_argument('--host', '-H', default='192.168.1.17',
                       help='Ollama server host (default: 192.168.1.17)')
    parser.add_argument('--port', '-p', type=int, default=11434,
                       help='Ollama server port (default: 11434)')
    parser.add_argument('--list-models', action='store_true',
                       help='List available models and exit')

    args = parser.parse_args()

    if args.list_models:
        print("Available models:")
        try:
            response = requests.get(f'http://{args.host}:{args.port}/api/tags')
            response.raise_for_status()
            models = response.json()['models']
            for model in models:
                print(f"  {model['name']}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching models: {e}")
        return

    print("Ollama Chat CLI")
    print("=" * 30)
    print(f"Using model: {args.model}")
    print(f"Host: {args.host}:{args.port}")
    print("Type 'quit', 'exit', or Ctrl+C to exit")
    print("Type 'help' for available commands")
    print("-" * 30)

    while True:
        try:
            user_input = input("\n> ")

            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            elif user_input.lower() == 'help':
                print("Available commands:")
                print("  quit/exit - Exit the program")
                print("  help - Show this help message")
                print("  clear - Clear the screen")
                print("  list-models - List available models")
                print("  <message> - Send a message to the model")
                continue
            elif user_input.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif user_input.strip() == "":
                continue

            response = chat_with_ollama(args.model, user_input, args.host, args.port)
            print(f"\nResponse:\n{response}\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
