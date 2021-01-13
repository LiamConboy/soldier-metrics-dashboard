import requests
import time

"""
Script step 1:
Have normal heart rates, water, and risk scores for 5 soldiers

Script step 2:
Have 2 of the soldiers start to increase heart rate and risk score, decrease water

Script step 3:
Have another soldier different from first 2 soldiers also increase heart rate and risk score, decrease water

Repeat script
"""

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 129
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 37
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 129
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 37
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 129
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 37
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(6)


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################





payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 60
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 150
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 65
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 140
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 45
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 60
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 154
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 60
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 151
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 52
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 57
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 165
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 160
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 68
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 170
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 80
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 55
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 168
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 78
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 175
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 90
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 89
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(6)


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################





payload = {
    "name": "Miller",
    "value": 65
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 140
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 62
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 149
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 159
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 67
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 57
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 163
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 54
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 169
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 175
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 81
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(10)


############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################








payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 129
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 37
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 129
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 37
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 129
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 37
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(6)


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################





payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 60
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 150
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 65
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 140
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 45
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 60
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 154
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 60
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 151
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 52
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 57
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 165
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 160
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 68
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 170
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 80
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 55
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 168
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 78
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

payload = {
    "name": "Conboy",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 120
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 30
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 175
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 90
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 126
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 89
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(6)


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################





payload = {
    "name": "Miller",
    "value": 65
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 140
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 62
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 149
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 59
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 159
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 67
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 57
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 163
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 54
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 169
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)

########################################
########################################
########################################
########################################
########################################

payload = {
    "name": "Miller",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 175
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 81
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 50
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 178
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 92
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 49
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 174
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 91
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

########################################

payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(10)


############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################








payload = {
    "name": "Conboy",
    "value": 73
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Conboy",
    "value": 121
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Conboy",
    "value": 32
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Hiebert",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Hiebert",
    "value": 130
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Hiebert",
    "value": 38
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Miller",
    "value": 70
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Miller",
    "value": 125
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Miller",
    "value": 34
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

####################################

payload = {
    "name": "Memoli",
    "value": 71
}
response = requests.post("http://localhost:5000/api/soldiers/water", json=payload)

payload = {
    "name": "Memoli",
    "value": 123
}
response = requests.post("http://localhost:5000/api/soldiers/heartRate", json=payload)

payload = {
    "name": "Memoli",
    "value": 33
}
response = requests.post("http://localhost:5000/api/soldiers/riskScore", json=payload)

time.sleep(3)