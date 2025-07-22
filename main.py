import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("models/gemini-1.5-flash")

chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You : ")
    if(user_input.lower()=="exit"):
        break
    response = chat.send_message(user_input)
    print("Gemini",response.text)



