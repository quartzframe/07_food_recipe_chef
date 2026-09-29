import os
import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing. Copy .env.example to .env and add your API key.")

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.1-flash-lite"

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def chat(message, history):
    contents = []
    for item in history:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content", "")
            if role in ("user", "assistant") and content:
                contents.append(
                    types.Content(
                        role=role,
                        parts=[types.Part.from_text(text=str(content))]
                    )
                )
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            user_msg, assistant_msg = item
            if user_msg:
                contents.append(types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=str(user_msg))]
                ))
            if assistant_msg:
                contents.append(types.Content(
                    role="model",
                    parts=[types.Part.from_text(text=str(assistant_msg))]
                ))

    contents.append(types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)]
    ))

    response = client.models.generate_content(
        model=MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            thinking_config=types.ThinkingConfig(thinking_level="low"),
            temperature=0.4,
        ),
    )
    return response.text or "I couldn't generate a response."

demo = gr.ChatInterface(
    fn=chat,
    title="Recipe Chef",
    description="Powered by Gemini 3.1 Flash-Lite",
    examples=[
        "What can you help me with?",
        "Give me a practical step-by-step plan.",
        "Ask me the questions you need before giving a recommendation."
    ],
)

if __name__ == "__main__":
    demo.launch()
