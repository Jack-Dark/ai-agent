import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    try:
        generate_content(client, messages, args.verbose)

    except Exception as e:
        print("===================================")
        print("Error while calling the Gemini API.")
        print("===================================")
        print(e)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0,
        ),
    )

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return

    for function_call in response.function_calls:
        function_call_result = call_function(function_call)
        if not len(function_call_result.parts):
            raise Exception("No parts in function call, I guess?")
        if not function_call_result.parts[0].function_response:
            raise Exception("Function did not return a response")
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Function did not return a response")

        function_results = []
        function_results.append(
            function_call_result.parts[0].function_response.response
        )

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        # print(f"Calling function: {function_call.name}({function_call.args})")


if __name__ == "__main__":
    main()
