
import os
from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads your .env file

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello and tell me one interesting fact about AI in one sentence."}
    ]
)

print(message.content[0].text)