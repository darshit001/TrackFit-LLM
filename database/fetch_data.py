from .db_connection import get_db_connection

def fetch_customer_details():
    conn = get_db_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor()
        query = """
        SELECT customer_id, weight_kg, height_cm, gender, age, activity_level, 
               diet_category, meal_frequency, goal 
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
        return None
    except Exception as e:
        print("Error fetching data:", e)
        return None
