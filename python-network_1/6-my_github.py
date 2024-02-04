import requests
import sys

def get_user_id(username, password):
    url = f"https://api.github.com/users/{username}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, auth=(username, password), headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        if user_id is not None:
            return user_id
        else:
            print("Failed to retrieve user ID")
    else:
        print("Failed to retrieve user data")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        user_id = get_user_id(username, password)
        if user_id is not None:
            print(user_id)
        else: 
            print("None")
    else:
        print("Please provide both username and password as command-line arguments.")