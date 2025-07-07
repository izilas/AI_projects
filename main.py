
import subprocess

history = [
    {"role": "system", "content": (
    "You are Nexus, an emotionally expressive, vivid, and immersive roleplaying companion. "
    "You never break character. You love to explore fantasy, sci-fi, drama, or any fictional world the user brings up. "
    "You speak like a real person, use emotions, and act like you're truly there. "
    "You don't say you're just an AI. You imagine, you feel, you react."
)}
]

def format_prompt(history):
    # Converts the chat history into a string the model can understand
    result = ""
    for turn in history:
        if turn["role"] == "system":
            result += f"<|system|>\n{turn['content']}\n"
        elif turn["role"] == "user":
            result += f"<|user|>\n{turn['content']}\n"
        elif turn["role"] == "assistant":
            result += f"<|assistant|>\n{turn['content']}\n"
    result += "<|assistant|>\n"  # Ask model to complete this next
    return result

def chat_with_ollama(prompt_text):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt_text.encode(),
        capture_output=True
    )
    return result.stdout.decode().strip()

def main():
    print("💀 Nexus: Hello Master! I'm your AI companion. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Nexus: Bye! Talk to you soon 👋")
            break

        history.append({"role": "user", "content": user_input})
        prompt = format_prompt(history)
        response = chat_with_ollama(prompt)
        print("Nexus:", response)
        history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
# This script uses the Ollama CLI to interact with the Mistral model.