# Personalized Diet and Workout Recommendation System

This project generates personalized diet and workout plans using customer data from a PostgreSQL database and the Groq API for AI-driven recommendations.

## Project Overview
The system follows these steps:
1. Fetch customer data from PostgreSQL.
2. Generate a detailed prompt based on customer details.
3. Use the Groq API to create personalized diet and workout plans.
4. Display the generated plans in JSON format.

---

## Folder Structure
```

├── .env
├── main.py
├── database/
│   ├── db_connection.py
│   ├── fetch_data.py
├── services/
│   ├── generate_prompt.py
│   ├── groq_service.py
├── README.md
├── requirements.txt
```

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
