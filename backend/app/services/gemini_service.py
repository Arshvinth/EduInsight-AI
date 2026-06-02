
import os
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Generate a final answer using retrieved context
def generate_answer_with_gemini(query: str, context: str) -> str:
    model_name = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

    prompt = f"""
You are an academic assistant.

Use the context below to answer the user's question clearly and accurately.
If the context is insufficient, say you do not have enough information.

Context:
{context}

Question:
{query}
"""

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", str(e))
        return f"[Gemini Error] {str(e)}"
