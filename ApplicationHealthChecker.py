import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    application_url = "https://your-application-url.com"  # Change this to the actual URL
    
    check_application_health(application_url)

