# Import the requests module for making HTTP requests
import requests

# Define the URL of the API endpoint
url = "https://alu-intranet.hbtn.io/status"

# Send a GET request to the specified URL
response = requests.get(url)

# Print the response body
print("Body response:")
print("\t- type:", type(response.text))  # Print the type of the response content
print("\t- content:", response.text)  # Print the actual response content