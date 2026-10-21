# Module 1 Checkpoint 2: AI Front Desk Design

## Business

**Business name:** Sweet Crumbs Bakery

**Purpose:** Answer common customer questions, calculate accurate order quotes, and prepare AI prompts for questions that the rules cannot answer.

## 1. Intents

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | refund, complaint, late | Sorry about that. A manager will contact you. |
| Greeting | hi, hello, salam | Welcome to Sweet Crumbs Bakery! |
| Hours | hours, timing, open | We are open 9 am to 10 pm every day. |
| Location | location, address, where | We are located on Main Boulevard, Lahore. |
| Delivery | delivery, deliver, home | Delivery costs 200 PKR. Free delivery applies when the discounted subtotal is at least 3,000 PKR. |
| Menu and fees | menu, price, cost, exact item names | Show menu prices and explain how to request a quote. |
| Quote | /quote | Ask for an item and quantity, then calculate the order total. |
| Private question | CNIC, phone number, private information | Prepare a privacy-focused prompt for the local model. |
| Unknown question | No matching rule | Prepare an AI prompt and estimate the cloud AI cost. |

## 2. Business Rules

| Rule | Value |
|---|---|
| Business | Sweet Crumbs Bakery |
| Cupcake | 250 PKR each |
| Brownie | 300 PKR each |
| Chocolate cake | 1,500 PKR each |
| Bulk discount | 10% off for 10 or more items |
| Delivery fee | 200 PKR |
| Free delivery | Discounted subtotal of 3,000 PKR or more |
| Private keywords | Phone, CNIC, address |
| Private model | Local model route; intended model: llama3.2 |
| Private AI cost | Estimated at 0 PKR |
| Example cloud price | 0.8 PKR per 1,000 estimated tokens |
| Token estimate | Approximately one token per four characters |

**Calculation order:** Calculate the subtotal, apply the bulk discount, and then check whether the discounted subtotal qualifies for free delivery.

**AI routing note:** The program prepares prompts and estimates costs. It does not currently call the local or cloud model automatically. The selected model name is a routing label until model integration is implemented.


## 3. Rule Test Results

| You type | Expected result | Pass? |
|---|---|---|
| `WHAT are your hours` | Hours reply despite capitals and surrounding spaces | Pass |
| `which cake is best?` | Cloud AI fallback, not greeting | Pass |
| `my order is late` | Complaint reply and complaint count increases | Pass |
| `/quote`, then chocolate cake, quantity 1 | 1,500 PKR subtotal plus 200 PKR delivery | Pass |
| `/quote`, then cupcake, quantity 15 | 10% discount and free delivery | Pass |
| `/quote`, then brownie, quantity 10 | 10% discount applied | Pass |
| `/quote`, then pizza, quantity 2 | Not on menu; no crash | Pass |
| `what is my CNIC?` | Prepare a privacy-focused prompt and estimate cost as 0 PKR | Pass |
| Press Enter without text | Ask for a question again | Pass |
| `BYE` | Goodbye and session report | Pass |

## 4. Additional Verified Test

**Input:** `/quote`, item `cupcake`, quantity `12`

**Observed result:**
- Subtotal: 3,000 PKR
- Discount: 300 PKR
- Delivery: 200 PKR
- Final total: 2,900 PKR
- Quote count: 1
- Quoted value: 2,900 PKR

**Cloud fallback test:** `which cake is best?` selected the cheap cloud model and estimated 5 input tokens at a cost of 0.0040 PKR.

**Private routing test:** `what is my CNIC?` selected the local model and estimated a cost of 0.0000 PKR.

## 5. Testing Notes

- Mark a test as passed only after running it.
- The complaint rule runs before ordinary FAQ rules.
- The discount is applied before checking the free-delivery threshold.
- Private questions should receive a zero-cost local route.
- AI prompts and costs are currently prepared or estimated; actual model answers and provider charges are not produced by this script.
- Keep screenshots of successful terminal runs for the project submission.

