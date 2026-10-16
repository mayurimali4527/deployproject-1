import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)
article="""The white-booted racket-tail (Ocreatus underwoodii) is a species in the hummingbird family, Trochilidae. It is found in Colombia, Ecuador and Venezuela, where it inhabits humid forests and forest edges, most commonly at elevations of 1,600 to 2,200 metres (5,200 to 7,200 ft). The species shows pronounced sexual dimorphism: males have elongated outer tail feathers with bare shafts ending in distinctive oval flags, while both sexes have white leg puffs. It feeds primarily on nectar, but also catches small insects in flight. The female lays two eggs in a tiny cup nest constructed from plant fibres and lichen. This male white-booted racket-tail of the subspecies O. u. melanantherus was photographed in Refugio Paz de las Aves, a nature reserve in Ecuador, showing its green plumage and racket-shaped tail feathers while in flight."""
prompt=f"""

summarize below article in 50 words
{article}
"""

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

# Display response
print("\nGemini Response:\n")
print(response.text)
