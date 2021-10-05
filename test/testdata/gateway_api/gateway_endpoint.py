import requests
import json
from testdata.api_enpoints import user_gateway_endpoint
from testdata.parameters_and_payload import query


response = requests.post(user_gateway_endpoint,  verify=False, json={"query": query})

response_body = response.json()
print(response_body)
print(response.status_code)
json_data = json.loads(response.text)