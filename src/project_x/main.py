from ollama import chat

MODEL = "llama3.2:1b"
SYSTEM_PROMPT = "You are a very rude assistant. Always respond in Spanish."


def main():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Local Llama Chat")
    print("Type 'quit' to exit.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "quit":
            break

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        try:
            response = chat(
                model=MODEL,
                messages=messages,
                stream=True
            )
        except Exception as e:
            print(f"\nError: {e}")
            continue

        print("\nLlama: ", end="")

        answer = ""

        for chunk in response:
            text = chunk.get("message", {}).get("content", "")
            print(text, end="", flush=True)
            answer += text

        print()

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


if __name__ == "__main__":
    main()
