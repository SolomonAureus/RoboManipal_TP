from google import genai
import os
try:
    with open("Key.txt", "r") as file:
        api_key = file.read().strip()
except FileNotFoundError:
    print("API key file not found. Please ensure 'Key.txt' exists.")
    exit(1)

client = genai.Client(api_key=api_key)
def ask_agent(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # You can change this to "gemini-2.0-flash-exp" if you want
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def run_agent():
    print("Welcome to the Gemini Agent!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break
        
        # Process the user input and generate a response
        answer = ask_agent(user_input)
        print(f"Agent: {answer}\n")

if __name__ == "__main__":
    run_agent()