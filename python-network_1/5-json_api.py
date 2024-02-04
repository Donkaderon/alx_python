import requests
import sys

# Get the letter from command line arguments
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

# Send POST request
url = "http://0.0.0.0:5000/search_user"
data = {"q": q}
response = requests.post(url, data=data)

# Process the response
try:
    json_data = response.json()
    if json_data:
        user_id = json_data.get("id")
        user_name = json_data.get("name")
        if user_id is not None and user_name is not None:
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")