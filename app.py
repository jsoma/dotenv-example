from dotenv import load_dotenv
import os

load_dotenv()
# environment variables

print("-=-=-=-")

API_KEY = os.getenv("API_KEY")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
PASSWORD = os.getenv("PASSWORD")

url = f"https://example.com/api/?api_key={API_KEY}"
print("URL is", url)

print("------")

login_info = {
    'email': EMAIL_ADDR,
    'pw': PASSWORD
}
print("Login info is", login_info)

print("-=-=-=-")