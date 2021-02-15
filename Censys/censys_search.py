import censys.ipv4
import pandas as pd
import json
import os
ipv4 = censys.ipv4.CensysIPv4(api_id="API HERE", api_secret="SECRET")
ipv4.view('8.8.8.8')

x=[]
print("1:location.country_code:IN and 443.https.get.body:SCADA")
print("2:location.country_code:IN and  metadata.device_type: SCADA")
print("3:location.country_code:IN and  80.http.get.body: SCADA")
print("4:tags.raw:modbus and location.country:India")
print("5:metadata.device_type: scada controller gateway")
print("6:502.modbus.device_id.support: True  and location.country: India")
opt=int(input("Select the option"))
if opt==1:
    result = ipv4.search("location.country_code:IN and 443.https.get.body:SCADA")
    for i in result:
        x.append(i)
if opt==2:
    result = ipv4.search("location.country_code:IN and metadata.device_type: SCADA")
    for i in result:
        x.append(i)
if opt==3:
    result = ipv4.search("location.country_code:IN and 80.http.get.body: SCADA")
    for i in result:
        x.append(i)
if opt==4:
    result = ipv4.search("location.country_code:IN and tags.raw:modbus")
    for i in result:
        x.append(i)
if opt==5:
    result = ipv4.search("location.country_code:IN and metadata.device_type: scada controller gateway")
    for i in result:
        x.append(i)
if opt==6:
    result = ipv4.search("502.modbus.device_id.support: True  and location.country: India")
    for i in result:
        x.append(i)

df=pd.DataFrame.from_dict(x)
df.style.hide_index()
df.to_csv(input("Enter <filename>.csv you want to save (Ex - temp1.csv)"))


