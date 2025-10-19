import requests

response = requests.get("https://api.github.com")
print(response.json())

response = requests.get("https://api.github.com/repos/pandas-dev/pandas/issues")
print(response.json())

response = requests.get("https://api.github.com/repos/pandas-dev/pandas/issues/1")
print(response.json())

response = requests.get("https://api.github.com/repos/pandas-dev/pandas/issues/1/comments")
print(response.json())

response = requests.get("https://api.github.com/repos/pandas-dev/pandas/issues/1/comments/1")
print(response.json())