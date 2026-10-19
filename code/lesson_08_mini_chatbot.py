
"""
Lesson 1.8: Business Helper Bot
Business: Care Plus Clinic
A rule-based chatbot for common clinic questions.
"""

BOT = "Care Plus Clinic Bot"

# Welcome message
print(f"{BOT}: Welcome! I can help with timings, fees, location and appointments.")
print(f"{BOT}: Type 'bye' to end the chat.")

# Memory: remember the visitor's name
name = input(f"{BOT}: What is your name? ").strip().title()

if name == "":
    name = "friend"

print(f"{BOT}: Nice to meet you, {name}!")

# Count messages and unanswered questions
count = 0
unanswered = 0

# Main chatbot loop
while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    # Exit rule
    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Thank you for contacting us.")
        break

    # Empty input rule
    elif message == "":
        print(f"{BOT}: Please type a question.")

    # Complaint rule comes first
    elif "complaint" in message or "problem" in message or "bad service" in message:
        print(f"{BOT}: We are sorry to hear that. Please contact our clinic reception.")

    # Opening hours
    elif "hour" in message or "open" in message or "timing" in message:
        print(f"{BOT}: Our clinic is open from 9 am to 8 pm, Monday to Saturday.")

    # Consultation fees
    elif "fee" in message or "price" in message or "cost" in message:
        print(f"{BOT}: Our example consultation fee is 1,000 PKR.")

    # Location
    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: Our example clinic address is Main Boulevard, Lahore.")

    # Appointments
    elif "appointment" in message or "book" in message or "visit" in message:
        print(f"{BOT}: Please contact our clinic reception to arrange an appointment.")

    # Greeting
    elif message == "hi" or message == "hello" or message.startswith("salam"):
        print(f"{BOT}: Hello, {name}! How can we help you today?")

    # Fallback rule
    else:
        unanswered += 1
        prompt = (
            "You are a friendly assistant for Care Plus Clinic. "
            "Do not diagnose medical conditions. "
            f"Answer this general question in 2 lines: {message}"
        )
        print(f"{BOT}: I do not have an answer for that question yet.")
        print(f"{BOT}: In Module 2, AI could use this prompt:")
        print(f"  {prompt}")

# Chat summary
print("=" * 40)
print(f"Chat summary: {count} messages, {unanswered} unanswered.")

