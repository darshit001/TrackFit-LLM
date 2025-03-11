Diet and Workout Recommendation System

This project generates personalized diet and workout plans based on customer details fetched from a PostgreSQL database. The system uses the Groq API to create customized recommendations.

Features

Fetches customer details from PostgreSQL database

Generates diet and workout plans based on user data and goals

Calculates total daily calorie needs using the Mifflin-St Jeor Equation

Provides detailed meal and workout plans in JSON format

Technologies Used

Python

PostgreSQL

Groq API

Dotenv (for environment variable management)

Installation

Clone this repository:

git clone <repository_url>
cd <project_directory>

Install required dependencies:

pip install psycopg2 groq python-dotenv

Create a .env file in the root folder and add the following:

DB_NAME=<your_database_name>
DB_USER=<your_database_username>
DB_PASSWORD=<your_database_password>
DB_HOST=<your_database_host>
DB_PORT=<your_database_port>
GROQ_API_KEY=<your_groq_api_key>

Usage

Ensure your PostgreSQL database is running and accessible.

Run the script:

python main.py

The generated diet and workout plan will be displayed in the console as a JSON response.

Database Table Structure

The customerdetails table should have the following columns:

customer_id

weight_kg

height_cm

gender

age

activity_level

diet_category

meal_frequency

goal

Output JSON Structure

{
  "user_information": {
    "customer_id": "1",
    "weight": "70 kg",
    "height": "175 cm",
    "gender": "Male",
    "age": "30 years",
    "activity_level": "Moderately Active",
    "diet_preference": "Vegetarian",
    "meal_frequency": "3 meals",
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
      },
      {
        "meal": "Lunch",
        "food_items": "Quinoa salad with chickpeas",
        "portion_size": "100g quinoa, 50g chickpeas",
        "calorie_count": "450 kcal"
      },
      {
        "meal": "Dinner",
        "food_items": "Grilled tofu with steamed broccoli",
        "portion_size": "100g tofu, 150g broccoli",
        "calorie_count": "350 kcal"
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
      },
      {
        "exercise": "Bodyweight Squats",
        "duration_reps": "3 sets of 15 reps",
        "estimated_calories_burned": "100 kcal"
      }
    ]
  }
}

License

This project is licensed under the MIT License.

Author

Darshit Radadiya

