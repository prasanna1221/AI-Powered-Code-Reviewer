import openai
import sys

#openai.api_key = "your-api-key"

def refactor_code(code_snippet):
    prompt = f"Refactor the following code to improve readability and efficiency:\n\n{code_snippet}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python code_refactor.py <code_snippet>")
    else:
        code_snippet = sys.argv[1]
        refactored_code = refactor_code(code_snippet)
        print("Refactored Code:\n", refactored_code)
