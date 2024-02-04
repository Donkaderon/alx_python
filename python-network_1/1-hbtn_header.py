import requests
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Send a GET request to the specified URL
response = requests.get(url)

# Retrieve the value of the 'X-Request-Id' header from the response
request_id = response.headers.get('X-Request-Id')

# Display the value of the 'X-Request-Id' variable
print(request_id)