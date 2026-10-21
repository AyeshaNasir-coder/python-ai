
"""AI Front Desk for Sweet Crumbs Bakery.

Answers FAQs, calculates order quotes, routes unknown questions,
and tracks customer activity and estimated AI costs.
"""

# Why: Constants make business settings easy to update.
BOT_NAME = "Sweet Crumbs Desk"
BUSINESS_NAME = "Sweet Crumbs Bakery"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.8

print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask a question, type /quote for a price, or bye to exit.")

# Why: Clean the customer's name once for consistent replies.
customer_name = input(
    f"{BOT_NAME}: What is your name? "
).strip().title()

if not customer_name:
    customer_name = "Customer"

message_count = 0
answered_count = 0
unanswered_count = 0
complaint_count = 0
quote_count = 0
total_quoted_value = 0
total_ai_cost = 0.0

while True:
    message = input(f"{customer_name}: ").strip().lower()
    message_count += 1

    if message == "":
        print(f"{BOT_NAME}: Please enter a question.")

    # Why: Complaints are handled before general FAQ rules.
    elif (
        "refund" in message
        or "complaint" in message
        or "late" in message
    ):
        complaint_count += 1
        answered_count += 1
        print(
            f"{BOT_NAME}: Sorry about that. "
            "A manager will contact you."
        )

    elif message in ("bye", "exit"):
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    elif "agent" in message or "human" in message:
        print(f"{BOT_NAME}: Connecting you to a human...")
        break

    elif message == "/quote":
        item = input(
            f"{BOT_NAME}: Which item? "
        ).strip().lower()
        quantity_text = input(
            f"{BOT_NAME}: How many? "
        ).strip()

        # Why: Validate quantity before int() to avoid ValueError.
        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print(
                f"{BOT_NAME}: Please enter a positive whole number."
            )
        else:
            quantity = int(quantity_text)
            price = 0

            if item in ("cupcake", "cupcakes"):
                price = 250
            elif item in ("brownie", "brownies"):
                price = 300
            elif item in ("chocolate cake", "chocolate cakes"):
                price = 1500

            if price == 0:
                print(
                    f"{BOT_NAME}: Sorry, {item} "
                    "is not on our menu."
                )
            else:
                subtotal = price * quantity
                discount = 0

                if quantity >= 10:
                    discount = subtotal * 0.10

                discounted_subtotal = subtotal - discount

                if discounted_subtotal >= FREE_DELIVERY_LIMIT:
                    delivery = 0
                else:
                    delivery = DELIVERY_FEE

                total = discounted_subtotal + delivery

                quote_count += 1
                total_quoted_value += total
                answered_count += 1

                print(
                    f"{BOT_NAME}: {quantity:,} x {item} = "
                    f"{subtotal:,.0f} PKR"
                )
                print(
                    f"     Discount: -{discount:,.0f} PKR | "
                    f"Delivery: {delivery:,.0f} PKR"
                )
                print(f"     Total: {total:,.0f} PKR")

    # Route private-information questions before general FAQs.
    elif (
        "cnic" in message
        or "phone number" in message
        or "my phone" in message
        or "my address" in message
        or "private information" in message
    ):
        unanswered_count += 1
        question = message.capitalize()[:150]
        estimated_tokens = round(len(question) / 4)
        selected_model = "Local model"
        estimated_cost = 0.0
        total_ai_cost += estimated_cost

        prompt = f"""You are {BOT_NAME} for {BUSINESS_NAME}.
Customer name: {customer_name}
Customer question: {question}

Protect personal information.
Never guess or invent private details.
Answer briefly and suggest asking staff if needed."""

        print(f"{BOT_NAME}: This needs AI assistance.")
        print(f"Selected model: {selected_model}")
        print(f"Estimated input tokens: {estimated_tokens}")
        print(f"Estimated AI cost: {estimated_cost:.4f} PKR")
        print("Prompt to run in an AI tool:")
        print(prompt)

    elif (
        message == "hi"
        or message == "hello"
        or message.startswith("salam")
    ):
        answered_count += 1
        print(f"{BOT_NAME}: Welcome to {BUSINESS_NAME}!")

    elif (
        "hour" in message
        or "timing" in message
        or "open" in message
    ):
        answered_count += 1
        print(
            f"{BOT_NAME}: We are open 9 am to 10 pm every day."
        )

    elif (
        "location" in message
        or "where are you" in message
        or "where is the bakery" in message
    ):
        answered_count += 1
        print(
            f"{BOT_NAME}: We are located on Main Boulevard, Lahore."
        )

    elif (
        "delivery" in message
        or "deliver" in message
        or "home delivery" in message
    ):
        answered_count += 1
        print(
            f"{BOT_NAME}: Delivery costs {DELIVERY_FEE} PKR. "
            f"Orders of {FREE_DELIVERY_LIMIT:,} PKR or more "
            "after discount qualify for free delivery."
        )

    elif "payment" in message or "pay" in message:
        answered_count += 1
        print(
            f"{BOT_NAME}: Please ask our staff about "
            "the available payment methods."
        )

    elif (
        "menu" in message
        or "price" in message
        or "cost" in message
        or message == "cake"
        or message == "brownie"
        or message == "cupcake"
    ):
        answered_count += 1
        print(
            f"{BOT_NAME}: Cupcake: 250 PKR, Brownie: 300 PKR, "
            "Chocolate cake: 1,500 PKR. "
            "Type /quote for an exact order quote."
        )

    else:
        unanswered_count += 1
        question = message.capitalize()[:150]
        estimated_tokens = round(len(question) / 4)

        selected_model = "Cheap cloud model"
        estimated_cost = (
            estimated_tokens / 1000
        ) * CLOUD_PRICE_PER_1K_TOKENS
        total_ai_cost += estimated_cost

        prompt = f"""You are {BOT_NAME}, the front desk assistant
for {BUSINESS_NAME}.
Customer name: {customer_name}
Customer question: {question}

Answer in a friendly and concise way.
Use only known business information.
Do not invent prices, policies, or opening hours.
If you do not know the answer, say so and suggest
contacting a staff member."""

        print(f"{BOT_NAME}: I need AI assistance for this question.")
        print(f"Selected model: {selected_model}")
        print(f"Estimated input tokens: {estimated_tokens}")
        print(f"Estimated AI cost: {estimated_cost:.4f} PKR")
        print("Prompt to run in an AI tool:")
        print(prompt)

print("=" * 50)
print("Session report")
print(f"Messages: {message_count}")
print(f"Answered by rules: {answered_count}")
print(f"Unanswered / AI-routed: {unanswered_count}")
print(f"Complaints: {complaint_count}")
print(f"Quotes: {quote_count}")
print(f"Quoted value: {total_quoted_value:,.0f} PKR")
print(f"Estimated AI cost: {total_ai_cost:.4f} PKR")
print("=" * 50)

