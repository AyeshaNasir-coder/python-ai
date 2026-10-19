
"""
Lesson 1.7: Smart Model Router
Choose an AI model based on the task and estimate its cost.
"""

# 1. Get task and token count from the user
task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

# 2. Set example prices per 1,000 tokens (PKR)
cloud_price_per_1k = 0.5

# 3. Choose a model based on the task
# Private tasks must use the local model
if task == "private":
    model = "llama3.2 (local, Ollama)"
    cost = 0.0

elif task == "code":
    model = "claude (cloud, strong at code)"
    cost = (tokens / 1000) * cloud_price_per_1k

elif task == "chat":
    model = "small cloud model (cheap for chat)"
    cost = (tokens / 1000) * cloud_price_per_1k

else:
    model = "No model selected"
    cost = 0.0

# 4. Check the request length
if tokens < 0:
    warning = "Invalid token count."
elif tokens > 4000:
    warning = "Long request: consider shortening it."
else:
    warning = "Length is fine."

# 5. Display the result
print("\n" + "=" * 40)
print("SMART MODEL ROUTER")
print("=" * 40)

print(f"Task: {task}")
print(f"Estimated tokens: {tokens}")
print(f"Chosen model: {model}")
print(warning)
print(f"Estimated cost: {round(cost, 2)} PKR")

print("=" * 40)
