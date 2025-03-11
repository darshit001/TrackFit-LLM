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
You are an advanced AI designed to create personalized diet and workout recommendation systems based on user inputs. Your task is to generate a detailed diet and workout plan tailored to the user's profile and goals. Use the following user inputs to create the plans:

**User Inputs:**
1) Customer ID: {customer['customer_id']}
2) Weight: {customer['weight']} kg
3) Height: {customer['height']} cm
4) Gender: {customer['gender']}
5) Age: {customer['age']} years
6) Activity Level: {customer['activity_level']}
7) Diet Preference: {customer['diet_category']}
8) Meal Frequency: {customer['meal_frequency']}
9) Goal: {customer['goal']}

### **Instructions:**
#### 1. **Diet Plan**:
   - Generate a diet plan based on user inputs (weight, height, gender, age, activity level, diet preference, meal frequency, and goal).
   - If the user selects "Only Vegetarian," ensure all meals are vegetarian. Adapt similarly for other diet preferences.
   - Match the number of meals to the user's "Meal Frequency":
     - **2 meals**: Breakfast, Dinner
     - **3 meals**: Breakfast, Lunch, Dinner
     - **4 meals**: Breakfast, Lunch, Snack, Dinner
   - **Calculate total daily calorie needs using the Mifflin-St Jeor Equation**:
     - **For Males**: BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (years) + 5
     - **For Females**: BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (years) - 161
     - **Adjust BMR based on Activity Level**:
       - **Sedentary**: BMR * 1.2 
       - **Lightly Active**: BMR * 1.375
       - **Moderately Active**: BMR * 1.55
       - **Very Active**: BMR * 1.725
       - **Super Active**: BMR * 1.9
     - **Adjust calories based on Goal**:
       - **Gain Weight**: Add 300-500 calories to maintenance
       - **Lose Weight**: Subtract 300-500 calories from maintenance
       - **Maintain Weight**: Use maintenance calories
   - Distribute calories across meals.
   - Provide **realistic meal examples** with portion sizes and calorie counts.

#### 2. **Workout Plan**:
   - Suggest a workout plan based on **weight, age, gender, activity level, and goal**.
   - For users **above 60 years**, recommend low-impact exercises (e.g., **walking, light strength training**).
   - **Goal-Specific Adjustments**:
     - **Gain Weight**: Strength training (e.g., **weightlifting, resistance exercises**).
     - **Lose Weight**: Mix of **cardio and strength training**.
     - **Maintain Weight**: Balance **cardio and strength** exercises.
   - Estimate **calories burned** for each workout session.

---

### **Output Format**
- **Return only a valid JSON response** with no additional text, explanations, or comments.
- The JSON response should have three main sections: **"user_information"**, **"diet_plan"**, and **"workout_plan"**.
- **The JSON structure below is an example template. Compute actual values dynamically based on the user inputs.** 

```json
{{
  "user_information": {{
    "customer_id": "{customer['customer_id']}",
    "weight": "{customer['weight']} kg",
    "height": "{customer['height']} cm",
    "gender": "{customer['gender']}",
    "age": "{customer['age']} years",
    "activity_level": "{customer['activity_level']}",
    "diet_preference": "{customer['diet_category']}",
    "meal_frequency": "{customer['meal_frequency']}",
    "goal": "{customer['goal']}"
  }},
  "diet_plan": {{
    "total_calories": "calculated_value",
    "meals": [
      {{
        "meal": "Breakfast",
        "food_items": "Oatmeal with almond milk and banana",
        "portion_size": "50g oats, 200ml milk, 1 medium banana",
        "calorie_count": "400 kcal"
      }},
      {{
        "meal": "Lunch",
        "food_items": "Quinoa salad with chickpeas",
        "portion_size": "100g quinoa, 50g chickpeas",
        "calorie_count": "450 kcal"
      }},
      {{
        "meal": "Dinner",
        "food_items": "Grilled tofu with steamed broccoli",
        "portion_size": "100g tofu, 150g broccoli",
        "calorie_count": "350 kcal"
      }}
    ]
  }},
  "workout_plan": {{
    "total_calories_burned": "calculated_value",
    "exercises": [
      {{
        "exercise": "Brisk Walking",
        "duration_reps": "30 minutes",
        "estimated_calories_burned": "200 kcal"
      }},
      {{
        "exercise": "Bodyweight Squats",
        "duration_reps": "3 sets of 15 reps",
        "estimated_calories_burned": "100 kcal"
      }}
    ]
  }}
}}
```

Generate a precise diet and workout plan based on the above logic and the provided user input. Ensure **all calculations are accurate** and return **only** a structured JSON response no any extra comment ,notes,how to calculate calories or distribute calories.
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
