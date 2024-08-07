import requests

url = 'http://{Load Balancer DNS Name}:80/publish_data'  # Replace with your API endpoint

# Function to send POST request with incremental payload
def send_post_requests(n):
    for i in range(1, n + 1):
        payload = {"a": i, "b": i}
        response = requests.post(url, json=payload)
        print(response)

# Send 10 POST requests
send_post_requests(20)
