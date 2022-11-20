# import urllib library
from urllib.request import urlopen

# import json
import json
import urllib.parse

# store the URL in url as
# parameter for urlopen
url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)
print(data_json['product']['nutrient_levels'])
levels:data_json['product']['nutrient_levels']

