# %%
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import sys


links = [
    'https://int-brain-lab.github.io/iblenv/notebooks_external/data_release_repro_ephys',
    'https://int-brain-lab.github.io/iblenv/notebooks_external/data_release_brainwidemap.html',
]


def check_link(url):
    """
    Check if a URL returns a 404 or other error status code.
    Properly handles redirects by following them to the final destination.

    Args:
        url (str): The URL to check

    Returns:
        tuple: (is_valid, status_code, final_url) where is_valid is a boolean,
               status_code is the HTTP status code, and final_url is the URL after redirects
    """
    # Configure session with retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        # For redirects, we need to use GET with allow_redirects=True
        # to follow the redirect chain to the final destination
        response = session.get(url, timeout=10, allow_redirects=True)

        # Get the final URL after redirects
        final_url = response.url

        # Check if we have a valid response at the final destination
        is_valid = response.status_code < 400

        # If there was a redirect, report it
        if final_url != url:
            print(f"Redirect: {url} → {final_url}")

        return is_valid, response.status_code, final_url

    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False, None, url


# Check each link and print results
print("Checking links for errors...")
has_errors = False

for link in links:
    valid, status_code, final_url = check_link(link)
    if valid:
        print(f"✓ {link} - OK ({status_code})")
    else:
        has_errors = True
        print(f"✗ {link} - ERROR ({status_code})")
