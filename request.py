import requests

# Base URL
base_url = "http://127.0.0.1:8000/"

# POST Request to shorten a URL
post_url = f"{base_url}shorten/"
post_data = {
        "original_url": "https://www.google.com",
        "expiry_hours": 24,
        "password": "Ap@123456789"
}
post_response = requests.post(base_url, json=post_data)
print(f"get Response: {post_response.json()}")
