import openai

# Initialize the OpenAI client
client = openai.OpenAI(
    api_key="API_KEY",	#API_KEY 
    base_url="API_BASE"	#API_BASE
)

# Start an interactive chat session
print("Chatbot: Hello! I'm your chatbot. Ask me anything!")

while True:
    user_input = input("You: ")

    # Exit the chat if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Send the user input to the chat completion API
    response = client.chat.completions.create(
        model="LLM_MODEL",	#LLM_Model 
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    # Print the chatbot's response
    chatbot_response = response.choices[0].message.content  # Access content attribute directly
    print("Chatbot:", chatbot_response)