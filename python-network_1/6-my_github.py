import requests
import sys

def get_user_id(username, password):
    """
    Retrieves the user ID from the GitHub API using the provided username and password.

    Args:
        username (str): The GitHub username.
        password (str): The personal access token used as the password for authentication.

    Returns:
        int or None: The user ID if it is successfully retrieved, None otherwise.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    try:
        response = requests.get(url, auth=(username, password), headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        user_data = response.json()
        user_id = user_data.get("id")
        if user_id is not None:
            return user_id
        else:
            print("Failed to retrieve user ID")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Authentication failed. Please check your credentials.")
        else:
            print(f"Failed to retrieve user data. Error: {e}")

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