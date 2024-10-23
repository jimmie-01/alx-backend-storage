#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''

import requests
import time

# Dictionary to store URL counts and cached results
url_cache = {}

def get_page(url: str) -> str:
    # Check if the URL is cached and still valid (within 10 seconds)
    if url in url_cache and time.time() - url_cache[url]['timestamp'] < 10:
        url_cache[url]['count'] += 1
        return url_cache[url]['content']

    # If the URL is not cached or expired, fetch the content using requests
    response = requests.get(url)
    
    # Simulate slow response using slowwly.robertomurray.co.uk (optional)
    # time.sleep(5)

    # Store the fetched content in the cache along with the current timestamp and count
    url_cache[url] = {
        'content': response.text,
        'timestamp': time.time(),
        'count': 1
    }

    return response.text
