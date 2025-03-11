# Personalized Diet and Workout Recommendation System

This project generates personalized diet and workout plans using customer data from a PostgreSQL database and the Groq API for AI-driven recommendations.

## Project Overview
The system follows these steps:
1. Fetch customer data from PostgreSQL.
2. Generate a detailed prompt based on customer details.
3. Use the Groq API to create personalized diet and workout plans.
4. Display the generated plans in JSON format.

---

## Prerequisites
Before running the code, ensure you have the following:

- Python 3.10+
- PostgreSQL database
- Required Libraries:
  - `psycopg2`
  - `dotenv`
  - `groq`

### Installation
Install dependencies using pip:
```bash
pip install psycopg2 dotenv groq
```

---

## Environment Variables
Create a `.env` file in your project root with the following keys:

```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
GROQ_API_KEY=your_groq_api_key
```

---

## Code Implementation
```python
import os
import psycopg2
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Database connection details
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# Initialize Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# Function to fetch customer details from PostgreSQL
def fetch_customer_details():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
        SELECT customer_id, weight_kg, height_cm, gender, age, activity_level, diet_category, meal_frequency, goal 
        FROM customerdetails 
        ORDER BY customer_id DESC  
        LIMIT 1;
        """
        cursor.execute(query)
        customer = cursor.fetchone()

        cursor.close()
        conn.close()

        if customer:
            return {
                "customer_id": customer[0],
                "weight": customer[1],
                "height": customer[2],
                "gender": customer[3],
                "age": customer[4],
                "activity_level": customer[5],
                "diet_category": customer[6],
                "meal_frequency": customer[7],
                "goal": customer[8]
            }
        else:
            return None
    except Exception as e:
        print("Error fetching data:", e)
        return None

def generate_prompt(customer):
    prompt = f"""
    (Prompt content as described in the previous code)
    """
    return prompt

# Function to get a response from Groq
def get_groq_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-70b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("Failed to generate a response:", e)
        return None

# Main function
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

# Run the script
if __name__ == "__main__":
    main()
```

---

## Usage Instructions
1. Add customer data to the PostgreSQL database.
2. Ensure the `.env` file is correctly configured.
3. Run the Python script:
```bash
python main.py
```

---

## Expected JSON Response Format
```json
{
  "user_information": {
    "customer_id": "123",
    "weight": "70 kg",
    "height": "175 cm",
    "gender": "Male",
    "age": "30 years",
    "activity_level": "Moderately Active",
    "diet_preference": "Vegetarian",
    "meal_frequency": "3",
    "goal": "Gain Weight"
  },
  "diet_plan": {
    "total_calories": "calculated_value",
    "meals": [
      {
        "meal": "Breakfast",
        "food_items": "Oatmeal with almond milk and banana",
        "portion_size": "50g oats, 200ml milk, 1 medium banana",
        "calorie_count": "400 kcal"
      }
    ]
  },
  "workout_plan": {
    "total_calories_burned": "calculated_value",
    "exercises": [
      {
        "exercise": "Brisk Walking",
        "duration_reps": "30 minutes",
        "estimated_calories_burned": "200 kcal"
      }
    ]
  }
}
```

---

## Future Improvements
- Add dynamic input validation for customer data.
- Implement caching to improve performance.
- Enhance the prompt logic for more precise recommendations.

If you have questions or need further explanations, feel free to ask! 🚀
