import requests
from requests.exceptions import RequestException
import datetime

USERNAME = "XXX"
TOKEN = "XXXX" 
GRAPHID = "XXXXh"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token": "XXXXX",
    "username": "XXXX",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

data1 = None   
    
for attempt in range(3):  # Retry up to 3 times
    try:
        response = requests.post(url=pixela_endpoint, json=pixela_parameters, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        break  # Exit loop on success
    except RequestException as e:
        print(f"Post Attempt {attempt + 1} failed: {e}")
    else:
        print("All attempts failed.")
        
data1 = response.json()
print(f"User: {data1} {response} {response.text}\n\n")



pixela_graph = f"{pixela_endpoint}/{USERNAME}/graphs"

pixela_graph_parameters = {
    "id": GRAPHID,
    "name": "Pages Read",
    "unit": "pp",
    "type": "int",
    "color": "momiji"
}

# Authentication
pixela_headers = {
    "X-USER-TOKEN": TOKEN
}

data2 = None  

for attempt in range(3):  # Retry up to 3 times
    try:
        response = requests.post(url=pixela_graph, json=pixela_graph_parameters, headers=pixela_headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        break  # Exit loop on success
    except RequestException as e:
        print(f"Post Attempt {attempt + 1} failed: {e}")
    else:
        print("All attempts failed.")
        
data2 = response.json()
print(f"Graph: {response.text}\n\n")



pixela_graph_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

tds = datetime.datetime.now()
#tds = datetime.datetime(year=2025, month=3, day=18)
print(tds, tds.strftime("%Y%m%d"))

pixela_update_parameters = {
    "id": GRAPHID,
    "date": tds.strftime("%Y%m%d"),
    "quantity": "15"
}

# Authentication
pixela_headers = {
    "X-USER-TOKEN": TOKEN
}

data3 = None  

for attempt in range(3):  # Retry up to 3 times
    try:
        response = requests.post(url=pixela_graph_update, json=pixela_update_parameters, headers=pixela_headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        break  # Exit loop on success
    except RequestException as e:
        print(f"Post Attempt {attempt + 1} failed: {e}")
    else:
        print("All attempts failed.")
        
data3 = response.json()
print(f"Update: {response.text}\n\n")


pixela_pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20250320"

pixela_updatedata_parameters = {
    "quantity": "9"
}

# Authentication
pixela_headers = {
    "X-USER-TOKEN": TOKEN
}

data4 = None  

for attempt in range(3):  # Retry up to 3 times
    try:
        response = requests.put(url=pixela_pixel_update, json=pixela_updatedata_parameters, headers=pixela_headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        break  # Exit loop on success
    except RequestException as e:
        print(f"Post Attempt {attempt + 1} failed: {e}")
    else:
        print("All attempts failed.")
        
data4 = response.json()
print(f"Pixel Update: {response.text}\n\n")


pixela_pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20250318"

# Authentication
pixela_headers = {
    "X-USER-TOKEN": TOKEN
}

data5 = None  

for attempt in range(3):  # Retry up to 3 times
    try:
        response = requests.delete(url=pixela_pixel_update, headers=pixela_headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        break  # Exit loop on success
    except RequestException as e:
        print(f"Post Attempt {attempt + 1} failed: {e}")
    else:
        print("All attempts failed.")
        
data5 = response.json()
print(f"Pixel Delete: {response.text}\n\n")
    
    