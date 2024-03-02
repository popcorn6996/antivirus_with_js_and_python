import requests
import json


def check_website_safety(api_key, website):
    url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    payload = {
        "client": {
            "clientId": "AIzaSyA3yqAaeAM2uUyCBdUD2uwjMnqminDtzcY",  # Replace with your client ID
            "clientVersion": "1.0",
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "THREAT_TYPE_UNSPECIFIED", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": website}],
        },
    }
    
    response =  requests.post(url, data=json.dumps(payload))
    
    if response.ok:
        data = response.json()
        if 'matches' in data:
            print(f"The Website '{website} is considered malicious'. ")
        else:
            print(f"The website '{website}' is safe")
    else:
        print('Something went wrong, Please try again later.')
        


if __name__ == "__main__":
    api_key = "AIzaSyA3yqAaeAM2uUyCBdUD2uwjMnqminDtzcY"  
    website = input('Enter website URL: ')
    
    
    check_website_safety(api_key, website)                  