from database.fetch_data import fetch_customer_details
from services.generate_prompt import generate_prompt
from services.groq_service import get_groq_response

def main():
    customer = fetch_customer_details()
    if not customer:
        print("No customer data found!")
        return

    prompt = generate_prompt(customer)
    response = get_groq_response(prompt)

    if response:
        print(response)
    else:
        print("Failed to generate a response.")

if __name__ == "__main__":
    main()
