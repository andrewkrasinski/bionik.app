import requests

url = "https://bionic-reading1.p.rapidapi.com/convert"

input_string = input("Enter String to convert ")

payload = "content={}&response_type=html&request_type=html&fixation=1&saccade=10".format(input_string)
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "66e46f5bd6msha0a27d8f61634ccp13d3c8jsn9c3e3329c8b7",
	"X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com"
}	
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)