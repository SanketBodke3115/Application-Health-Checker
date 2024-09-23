import requests

def check_application_health(url):
    try:
        # Send a GET request to the application URL
        response = requests.get(url)
        
        # Check if the response status code indicates the application is up
        if response.status_code == 200:
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status Code: {response.status_code}")
    
    # Handle cases where the application is unreachable
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    # Replace this with your application's URL
    application_url = "https://your-application-url.com"  # Change this to the actual URL
    
    # Check the health of the application
    check_application_health(application_url)

