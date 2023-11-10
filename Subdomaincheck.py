import requests
import time

def check_subdomain_status(subdomain):
    """
    Check the status of a subdomain by sending a GET request to it.

    Args:
    subdomain (str): The subdomain to check.

    Returns:
    str: The status of the subdomain, either 'up' or 'down'.
    """
    try:
        response = requests.get(f"http://{subdomain}")
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException:
        return 'down'

def display_status_table(subdomains):
    """
    Display the status of subdomains in a tabular format.

    Args:
    subdomains (list): List of subdomains to display status for.
    """
    print("Subdomain\tStatus")
    for subdomain in subdomains:
        status = check_subdomain_status(subdomain)
        print(f"{subdomain}\t{status}")

if __name__ == "__main__":
    subdomains = ["subdomain1.example.com", "subdomain2.example.com", "subdomain3.example.com"]

    while True:
        display_status_table(subdomains)
        time.sleep(60)  # Wait for 60 seconds before checking again