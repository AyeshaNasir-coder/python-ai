

"""Lesson 1.6: Prompt Cleaner.
Clean and measure a question before sending it to AI.
"""

# Why: Cleaning removes unnecessary spaces and improves readability.
raw_name = input("Your name: ")
raw_question = input("Your question: ")

clean_name = raw_name.strip().title()
clean_question = raw_question.strip().capitalize()

# Why: Empty questions need safe handling before estimating tokens.
characters = len(clean_question)
estimated_tokens = round(characters / 4)

# Check for Python regardless of capitalization.
mentions_python = "python" in clean_question.lower()

# Limit the question to 150 characters.
short_question = clean_question[:150]

# Stretch: Replace a bad word before building the prompt.
safe_question = short_question.replace("stupid", "***")

# Why: A clear prompt tells the AI how to respond.
prompt = f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {safe_question}"""

print("=" * 40)
print(f"Cleaned question: {clean_question}")
print(f"Characters: {characters}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print("=" * 40)
print(prompt)
