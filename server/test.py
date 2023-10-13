import requests

url = 'http://localhost:5000/predict_home_price'
data = {'location':'1st Phase JP Nagar', 'total_sqft':"1000", 'bath':"2", 'balcony':"1", 'room':"2"}

response = requests.post(url, data=data)

print(response.text)


# url = 'http://localhost:5000/get_location_names'
#
# response = requests.get(url)
#
# print(response.text)