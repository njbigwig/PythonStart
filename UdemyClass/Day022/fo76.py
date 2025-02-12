import requests

def check_server_status():
    url = "https://status.bethesda.net/en/status"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            for service in data['services']:
                if service['name'] == 'Fallout 76':
                    return service['status']
        except ValueError:
            return "Invalid JSON response"
    return "Unable to fetch server status"

status = check_server_status()
print(f"Fallout 76 server status: {status}")

