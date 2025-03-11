import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
