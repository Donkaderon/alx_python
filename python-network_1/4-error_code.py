# Provides functions for making HTTP requests.
import requests
# Provides access to system-specific parameters and functions.
import sys

if __name__ == '__main__':
    url=sys.argv[1]

    response = requests.get(url)
    status_code = response.status_code
    response_body = response.text

    if response >= 400: 
        print ("Error code:", status_code)
    else: 
        print (response)



