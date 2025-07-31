import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    print("Hello from aiagent!")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("Error: No prompt provided.")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:]).strip()

    if not prompt:
        print("Error: Empty prompt provided.")
        sys.exit(1)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )

    if "--verbose" in sys.argv:
        print()
        print("Verbose mode enabled.")
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print()
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
