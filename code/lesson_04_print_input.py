
"""
Task 1.4: Business Prompt Builder

Ask for business information and create an AI prompt
to find possible solutions to business problems.
"""

# Get basic information from the user.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

# Display a welcome message.
print(f"\nHello, {name}!")

# Create a prompt using the entered information.
prompt = (
    f"Suggest 3 AI solutions for a {business} "
    f"that struggles with {problem}."
)

# Show the generated prompt.
print("--- Your AI Prompt ---")
print(prompt)
