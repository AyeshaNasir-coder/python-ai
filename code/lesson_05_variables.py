
"""
Lesson 1.5: AI Model Profile Card
Store model settings and estimate chat cost.
"""

# 1. Store the AI model profile

MODEL = "gemini-4-argon"                 # str: text
max_tokens = 300                         # int: whole number
temperature = 0.7                        # float: decimal
stream = False                           # bool: True or False
api_key = None                           # None: no value yet

system_prompt = "You are a helpful Python tutor."

# 2. Example price for practice, not a real API price
price_per_1k_tokens = 0.5                # PKR

# 3. Get token count from the user
tokens_used = int(input("Tokens used: "))

# 4. Calculate estimated cost
cost = (tokens_used / 1000) * price_per_1k_tokens

# 5. Display the model profile
print("\n--- AI Model Profile Card ---")

print(f"Model: {MODEL} | Type: {type(MODEL)}")
print(f"Max tokens: {max_tokens} | Type: {type(max_tokens)}")
print(f"Temperature: {temperature} | Type: {type(temperature)}")
print(f"Streaming: {stream} | Type: {type(stream)}")
print(f"API key: {api_key} | Type: {type(api_key)}")
print(f"System prompt: {system_prompt} | Type: {type(system_prompt)}")

# 6. Display the cost estimate
print("\n--- Cost Estimate ---")
print(f"Tokens used: {tokens_used}")
print(f"Estimated cost: {round(cost, 2)} PKR")
