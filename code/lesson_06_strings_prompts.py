
"""
Lesson 1.6: Prompt Cleaner
Clean a user's name and question before sending it to AI.
"""

# 1. Get input from the user
raw_name = input("Your name: ")
raw_question = input("Your question: ")

# 2. Clean the name and question
clean_name = raw_name.strip().title()
clean_question = raw_question.strip()

# 3. Clean the question's first letter
if clean_question:
    clean_question = clean_question[0].upper() + clean_question[1:]

# 4. Estimate the number of tokens
# Rule of thumb: 1 token is about 4 English characters
estimated_tokens = round(len(clean_question) / 4)

# 5. Limit the question to 150 characters
short_question = clean_question[:150]

# 6. Check whether the question mentions Python
mentions_python = "python" in clean_question.lower()

# 7. Build a multi-line prompt
prompt = f"""You are a helpful Python tutor.
Answer the user's question in 3 short lines.
User name: {clean_name}
Question: {short_question}"""

# 8. Display the results
print("\n" + "=" * 40)
print("PROMPT CLEANER RESULTS")
print("=" * 40)

print(f"Cleaned name: {clean_name}")
print(f"Cleaned question: {clean_question}")
print(f"Characters: {len(clean_question)}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")

print("\n--- Final AI Prompt ---")
print(prompt)
print("=" * 40)
