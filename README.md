# Validation process of Internet Connection ( Latency, Upload, Download )

This project was developed to help identify some situation related low performance of Internet link without any access in homepage ( browser ).

## Requirements

Follow these steps

1. Install **speedtest-cli** - ```pip install speedtest-cli``` [Link](https://pypi.org/project/speedtest-cli/)
2. Install **request** - Library to execute post via API - ```pip install requests``` [Documentation Link](https://pypi.org/project/requests/)
3. Minimum Python Version 2.7.x. At the moment of documentation using as below:
```
Python 2.7.17
```
4. Created account [Ubidots](www.ubidots.com) to show a dashboard with captured values and execute API ( post ) of variable.

## Create Dashboard

There is some documentation how to create variable inside of Ubidots dashboard and we had post inside my BLOG to explain how to make deployment using this environment.

The point you can export those values for any management tools or only execute directly via python to get values, but behind this deploy a schedule process was done via crontab process in Ubuntu machine to get values each 30 minutes.

## Example

1. Dashboard of Gauge
![alt text](https://github.com/rarodrigo/inet_validation_speed/blob/master/Gauge_Internet.png)

2. Dashboard of List
![alt text](https://github.com/rarodrigo/inet_validation_speed/blob/master/List_City_Provider.png)

## Comments

This project already use some public library of Python Project to get benefits and quickly overview of your Internet Connection.

All the variable used in the project were to get values related some carachteristics are viable for me. Follow the example:

1. Get **City** of Internet connection is being tested based in your connection
2. Get **Sponsor** of provider which your Ping, Upload and Download are being executed

If you need to get more information which are feasible for your connection can be visualized via variable and class ```get_best_server```

If you have other ideas, feel free to contact (e.g. create a new issue) to help this be developed.
