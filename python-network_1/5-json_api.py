import requests
import sys

def send_post_request(url, q):
    payload = {'q': q}
    response = requests.post(url, data=payload)
    response_content = response.json()
    if response_content is None:
        print("No result")
    else:
        id = response_content.get('id')
        name = response_content.get('name')
        if id is None or name is None:
            print('Not a valid JSON')
        else:
            print(f"[{id}]", name)
    return response.text

if __name__ == '__main__':
    url = sys.argv[1]
    q = sys.argv[2] if len(sys.argv) > 2 else ""

    response_body = send_post_request(url, q)
    print(response_body)