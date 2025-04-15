import requests
import time

session = requests.Session() # Use session instead of requests for faster requests

url = "https://example.com" # Put the URL you want to visit here

# User agent to spoof (Chrome 120 on Windows 10)
userAgent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Time delay between visits (seconds)
delay = 10

# Number of times to visit (set to None for infinite)
visit_limit = 100

def visit_website():
    try:
        response = session.get(url, headers=userAgent) # Use session for faster + headers for spoofing
        print(f"Visited {url}, Status: {response.status_code}")
    except session.RequestException as e:
        print(f"Failed to reach {url}, Error: {e}")

def main():
    count = 0
    while visit_limit is None or count < visit_limit:
        # start = time.time() # Uncomment this line and the line 2 lines under to measure and print elapsed time
        visit_website()
        # print("Elapsed:", time.time() - start)
        count += 1
        # time.sleep(delay) disable this for faster visits

if __name__ == "__main__":
    main()
