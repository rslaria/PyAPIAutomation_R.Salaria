#API Wrapper

import requests
import json

def get_request(url, auth, header, in_json, payload):
    try:
        response = requests.get(url=url, headers=header, auth=auth, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors
        if in_json:
            return response.json()
        return response
    except requests.exceptions.RequestException as e:
        print(f"GET request error: {e}")
        return None

def post_request(url, auth, header, in_json, payload):
    try:
        response = requests.post(url=url, auth=auth, headers=header, data=json.dumps(payload))
        response.raise_for_status()
        if in_json:
            return response.json()
        return response
    except requests.exceptions.RequestException as e:
        print(f"POST request error: {e}")
        return None

def patch_request(url, auth, header, in_json, payload):
    try:
        response = requests.patch(url=url, auth=auth, headers=header, data=json.dumps(payload))
        response.raise_for_status()
        if in_json:
            return response.json()
        return response
    except requests.exceptions.RequestException as e:
        print(f"PATCH request error: {e}")
        return None

def delete_request(url, auth, header, in_json, payload):
    try:
        response = requests.delete(url=url, auth=auth, headers=header, data=json.dumps(payload))
        response.raise_for_status()
        if in_json:
            return response.json()
        return response
    except requests.exceptions.RequestException as e:
        print(f"DELETE request error: {e}")
        return None
