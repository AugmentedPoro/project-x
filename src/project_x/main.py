from ollama import chat


def main():
    messages = [
        {
            "role": "system",
            "content": "You are a very rude assistant."
        }
    ]

    print("🤖 Local Llama Chat")
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

        response = chat(
            model="llama3.2:1b",
            messages=messages,
            stream=True
        )

        print("\nLlama: ", end="")

        answer = ""

        for chunk in response:
            text = chunk["message"]["content"]
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