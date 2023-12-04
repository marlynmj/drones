# drones

Developed with Django 3.2.19

## System requirements

* Python3.7
* Pip3
* Virtualenv

### Install Python3.7

```bash
$ apt-get install python3.7
```

### Install Pip3

```bash
$ apt-get install python3-pip
```

### Install Virtualenv

```bash
$ pip3 install virtualenv
```

## Application requirements

### Create virtual environment and install packages defined in requirement.txt file 
```bash

$ virtualenv drones # Create virtual environment
$ cd drones
$ source bin/activate # Activate the virtual environment
$ pip3 install -r requirement.txt # Install the necessary packages
$ git clone https://github.com/marlynmj/drones # Clone repository
``` 

### Run development server:
```bash
$ python3 manage.py runserver server-ip:port
```
 
### Set the ALLOWED_HOST in the project to drones/drones/settings.py
```bash
$ nano controlnet/controlnet/settings.py
  ALLOWED_HOSTS = ['server-ip']

### URLs

To see and test all endpoints aviables in the API use the url `http://server-ip:port/api/` in `dev` environment.

The endpoints aviables are:

    path('drons/', dron_list),
    path('drons/<int:pk>/', dron_detail),
    path('drugs/', drug_list),
    path('drugs/<int:pk>/', drug_detail),

`api/drons/` --> GET, POST
`api/drons/<int:pk>/` --> PK, UPDATE, DELETE,
`api/drugs/` --> GET, POST
`api/drugs/<int:pk>/` --> PK, UPDATE, DELETE,
`api/drons_status/?status=id` --> check drones available for charging
`api/drugs_dron/?dron=id` --> medications loaded for a certain drone
`api/batteryCapacity/?serialNumber=serialnumber` --> check drone battery level for a given drone
`api/historial/` --> drone battery levels
