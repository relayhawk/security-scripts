import argparse
import requests

def check_hsts(url):
    response = requests.get(url, timeout=5)
    if response.status_code == 200 and "strict-transport-security" in response.headers:
        return True
    else:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a website supports HSTS")
    parser.add_argument("url", type=str, help="The URL to check")
    args = parser.parse_args()

    if check_hsts(args.url):
        print("HSTS is supported!")
    else:
        print("HSTS is not supported.")
