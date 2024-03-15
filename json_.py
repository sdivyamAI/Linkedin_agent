import requests

# api_key = 'CPi9hqye810_i1-g6b75AQ'
# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
# params = {'url': 'https://www.linkedin.com/in/divyam102/',
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)


# print(response._content)


gist_response = requests.get(
    "https://gist.githubusercontent.com/sdivyamAI/acdc6fbba8f7d3fe3466786a613bf104/raw/9abf352c96338144c0d726c553b4dbbdf9b21a83/divyam.json"
)

print(gist_response.json()["full_name"])
