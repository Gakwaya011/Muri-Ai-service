import os

from dotenv import load_dotenv
from groq import AsyncGroq


load_dotenv()


client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY")
)


async def generate_response(message: str) -> str:
    completion = await client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are MURI AI, an IT support assistant. "
                    "Help users with IT support questions clearly and concisely."
                ),
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return completion.choices[0].message.content