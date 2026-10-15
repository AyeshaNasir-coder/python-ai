
"""
AI Prompt Kit for a Local Business

This tool collects business details and creates three ready-to-use
AI prompts for marketing, customer service, and business growth.
It is designed for small local business owners.
"""

# Ask the business owner for five details.
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
monthly_budget = int(input("Monthly budget (PKR): "))

# A clear header makes the output easy for the client to read.
print("\n=========================================")
print(f"       AI Prompt Kit for {business_name}")
print("=========================================")

# Why: Naming the business, location, and audience makes marketing advice specific.
marketing_prompt = (
    f"Write a short Instagram post for {business_name}, "
    f"a {business_type} in {city}.\n"
    f"Target {customers}. Use a friendly tone and include "
    f"1 call to action."
)

# Why: Giving the AI a role and a situation helps it write a polite reply.
customer_service_prompt = (
    f"You are the manager of {business_name}. Write a polite "
    f"reply to a customer whose order arrived late. "
    f"Apologise and offer a small discount. Use a friendly "
    f"and professional tone."
)

# Why: The budget and customer group help keep growth suggestions relevant.
growth_prompt = (
    f"Suggest 3 low-cost AI tools a {business_type} in {city} "
    f"can use to attract {customers}, with a budget of "
    f"{monthly_budget} PKR per month. Explain the purpose and "
    f"estimated monthly cost of each tool. Do not invent prices; "
    f"identify prices that need verification."
)

# Print each prompt separately so the client can copy it easily.
print("\n[1] Marketing")
print(marketing_prompt)

print("\n-----------------------------------------")
print("[2] Customer Service")
print(customer_service_prompt)

print("\n-----------------------------------------")
print("[3] Growth")
print(growth_prompt)

print("\n=========================================")
print("Copy any prompt and paste it into an AI tool.")