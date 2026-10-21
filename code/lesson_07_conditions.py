

"""Lesson 1.7: Smart Model Router.
Choose a model based on task type and estimate its cost.
"""

task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

# Example price for practice, not a real model price.
cloud_price_per_1k = 0.8

# Why: Private tasks should use a local model to avoid sending
# sensitive information to a cloud model.
if task == "private":
    model = "llama3.2 (local, Ollama)"
    price = 0

elif task == "code":
    model = "claude (cloud, strong at code)"
    price = cloud_price_per_1k

elif task == "chat":
    model = "small cloud model (cheap for chat)"
    price = 0.2

else:
    model = "No model selected"
    price = 0

# Why: Negative token counts are invalid, and long requests
# may need shortening to reduce cost.
if tokens < 0:
    print("Invalid token count.")
elif tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# Stretch: Ask whether the user has a paid account.
paid_answer = input("Is this a paid user? (yes/no): ").strip().lower()

if paid_answer == "no" and tokens > 2000:
    print("Upgrade to send long requests.")

if tokens >= 0:
    cost = (tokens / 1000) * price
    print(f"Chosen model: {model}")
    print(f"Estimated cost: {cost:.2f} PKR")
