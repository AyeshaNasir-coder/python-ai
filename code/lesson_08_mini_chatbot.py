
"""Lesson 1.8: Business Helper Bot.
Answer common questions for Care Plus Clinic.
"""

BOT = "Care Plus Clinic Bot"

print(f"{BOT}: Hi! Ask about timings, fees, location or appointments.")
print(f"{BOT}: Type 'bye' to exit.")

# Why: Asking the name once makes later replies more personal.
name = input(f"{BOT}: What is your name? ").strip().title()

if not name:
    name = "Friend"

message_count = 0
unanswered_count = 0
complaint_count = 0

while True:
    message = input(f"{name}: ").strip().lower()
    message_count += 1

    if message == "bye" or message == "exit":
        print(f"{BOT}: Take care, {name}!")
        break

    elif message == "":
        print(f"{BOT}: Please enter a question.")

    # Why: Complaints should be handled before ordinary questions.
    elif ("complaint" in message or "problem" in message
          or "bad service" in message):
        complaint_count += 1
        print(
            f"{BOT}: Sorry to hear that. "
            "Please contact our clinic reception for help."
        )

    elif message == "hi" or message == "hello" or message.startswith("salam"):
        print(f"{BOT}: Hello, {name}! How can we help you?")

    elif "timing" in message or "hour" in message or "open" in message:
        print(f"{BOT}: We are open 9 am to 8 pm, Monday to Saturday.")

    elif "fee" in message or "price" in message or "cost" in message:
        print(f"{BOT}: Example consultation fee is 1,000 PKR.")

    elif "location" in message or "address" in message or "where" in message:
        print(f"{BOT}: Our example address is Main Boulevard, Lahore.")

    elif "appointment" in message or "book" in message or "visit" in message:
        print(f"{BOT}: Please contact reception to arrange an appointment.")

    else:
        unanswered_count += 1

        # Why: Unknown questions are counted so the business can
        # identify where its chatbot needs improvement.
        prompt = (
            "You are a friendly assistant for Care Plus Clinic. "
            "Answer in 2 short lines. Do not diagnose medical conditions. "
            f"Customer question: {message}"
        )

        print(f"{BOT}: I do not know the answer to that yet.")
        print(f"{BOT}: AI prompt for Module 2: {prompt}")

print("=" * 40)
print(
    f"Chat summary: {message_count} messages, "
    f"{unanswered_count} unanswered."
)
print(f"Complaints received: {complaint_count}")


