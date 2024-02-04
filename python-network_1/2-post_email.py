# Provides functions for making HTTP requests.
import sys
# Provides access to system-specific parameters and functions.
import requests

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter.

    Returns:
        str: The response body text of the POST request.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py [URL] [email]")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)

