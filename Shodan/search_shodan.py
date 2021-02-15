import shodan
import sys
import requests
import pymysql
import pandas as pd
API_KEY = 'SECRET'

try:
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="scada")
except Exception as e:
        print("MySQL connection cannot be established: "+str(e))
        exit()
print("Instruction ---------------------")
print("To enter a searh similar/copy-paste of the below queries provided")
print("country:IN port: <any_port>")
print("country:IN port:2152 org:Power Grid Corporation of India Limited")
print("country:IN port:502 product:BMX P34 2020")
print("Ports for SCADA:502, 102, 20000, 1911, 4911, 47808, 44818, 18245, 18246, 5092, 1962, 5006, 5007, 9600, 789, 2404, 2455, 20547")
print("---------------------------------")
data = []
try:
        api = shodan.Shodan(API_KEY)
        # Perform the search
        
        # Loop through the matches and print each IP
        for service in api.search_cursor(input("Enter your query: ")):
                #print(service['ip_str'])
                list=[]
                list.append(service['ip_str'])
                list.append(service['org'])
                list.append(service['port'])
                list.append(service['data'])
                try:
                        cve=[]
                        # Print vuln information
                        for item in service['vulns']:
                                CVE = item.replace('!','')
                                cve.append(item)
                except Exception as e:
                        pass
                list.append(cve)
                list.append(service['location']['country_name'])
                try:
                        list.append(service['tags'][0])
                except Exception as e:
                        list.append("None")
                list = tuple(list)
                data.append(list)
        
except Exception as e:
        print("Shodan Error:"+str(e))

finally:
        df = pd.DataFrame.from_records(data)
        cursor=connection.cursor()
        proc=""
        for row in df.itertuples():
                for x in range(0,len(row[5])):
                        proc+=row[5][x]
                proc=proc.replace(",","  ")
                proc=proc.replace("[","")
                proc=proc.replace("]","")
                try:
                        cursor.execute("INSERT INTO shodan(IP, organization, PORT, Data, Vuln, date, country,tag) VALUES ('{}','{}','{}','{}','{}',now(),'{}','{}')".format(row[1], row[2], row[3], row[4], proc,row[6],row[7]))
                        connection.commit()
                        proc=""
                except Exception as e:
                        pass
        print("Table updated...")
