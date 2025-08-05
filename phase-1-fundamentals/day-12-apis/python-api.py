"""
[ ] Day 12: Working with APIs
• Topic: Basics of APIs, making HTTP requests with requests.
• Resource: FreeCodeCamp Python Requests Tutorial.
• Task: Use a public API (e.g., weather API) to fetch data and print it.
"""

# Day 12
# Task: Use a public API (e.g., weather API) to fetch data and print it.

# Imports
import requests

# Define Baseline API URL
BASE_URL = 'https://fakestoreapi.com'

# Define Parameters
query_params = {
    'limit': 3
}

# Make the request
response = requests.get(f'{BASE_URL}/products', params=query_params)
print(response.json())