from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

# ✅ Paste your OpenAI API key here
openai.api_key = "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"

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(input: ChatInput):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if GPT-4 not enabled
            messages=[{"role": "user", "content": input.prompt}]
        )
        return {"response": res.choices[0].message.content.strip()}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
