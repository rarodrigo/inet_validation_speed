#!/usr/bin/python
import speedtest
import requests

#Global variables
ENDPOINT = "things.ubidots.com" #URL related webpage to create dashboard
DEVICE_LABEL = "raspberry-pi" #Not necessary to be raspeberry and can use any linux inside container or run in your machine
VARIABLE_LABEL = "city" #Variable created inside Ubidots portal
TOKEN = "YOUR TOKEN"

#Get value related your connection using library SpeedTest
st = speedtest.Speedtest()

#Get values related class of server near of your provider
st.get_best_server()

#Execute Post Related City and Provider of SpeedTest
def post_var(payload_ci_sp, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
    url = "http://{}/api/v1.6/devices/{}".format(url, device)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    if VARIABLE_LABEL == 'city':
        req = requests.post(url=url, headers=headers, json=payload_ci_sp)

    else:
        print("Error with variable City")

#Main function to capture payload each variable(city,provider)
def main():
    # Builds Payload and topic
    payload_ci_sp = {VARIABLE_LABEL: {"value": 30, "context": {"city": st.best['name'], "provider": st.best['sponsor']}}}

    #Send Data
    post_var(payload_ci_sp)

#It only to execute main function + post_var
if __name__ == "__main__":
    main()

#Capture all values related your connection
payload = {'Download': round(st.download() / 1000000, 2) , 'Upload': round(st.upload() / 1000000, 2), 'Ping': round(st.results.ping, 2)}

#Execute post of values
r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry-pi/?token='TOKEN'', data=payload)
