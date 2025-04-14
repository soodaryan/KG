from dotenv import load_dotenv
import os

load_dotenv()

# Graph 1
NEO4J_URI_1 = os.getenv("NEO4J_URI_1")
NEO4J_USERNAME_1 = os.getenv("NEO4J_USERNAME_1")
NEO4J_PASSWORD_1 = os.getenv("NEO4J_PASSWORD_1")

# Graph 2
NEO4J_URI_2 = os.getenv("NEO4J_URI_2")
NEO4J_USERNAME_2 = os.getenv("NEO4J_USERNAME_2")
NEO4J_PASSWORD_2 = os.getenv("NEO4J_PASSWORD_2")

# Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
