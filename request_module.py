import requests

websites = [
"https://google.com",
"https://maps.google.com",
"https://cnn.com",
"https://amazon.com"
]
try:
    for web in websites:

        resp = requests.get(web)

        #print(resp.status_code)

        if resp.status_code != 200:
            print(f"{web} is down!")

        else:
            print(f"{web} is up!")
except Exception as e:
    print(f"Error: {e}")
    
#dir(resp)

#can schedule with Lambda function
#200 means success