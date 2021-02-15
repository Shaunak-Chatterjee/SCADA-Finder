import pandas as pd
import pymysql
import sys
file = sys.argv[1]
data = pd.read_csv (file)   
df = pd.DataFrame(data, columns= ['location.country','location.registered_country' , 'location.city', 'ip', 'protocols'])
df.rename(columns = {'location.country': 'COUNTRY', 'location.registered_country': 'REG_COUNTRY', 'ip':'IP', 'location.city' : 'CITY', 'protocols':'PROTOCOLS'},inplace = True)
#print(df.columns)
try:
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="scada")
    cursor=connection.cursor()
    #cursor.execute("INSERT INTO censys (country,registered_country,city,ip,protocols) VALUES ('INDIA','IN','JAIPUR','1.1.1.1','502')")
    for row in df.itertuples():
        proc=""
        for x in range(0,len(row[5])):
            proc+=row[5][x]
        proc=proc.replace("'","")
        proc=proc.replace(","," ")
        proc=proc.replace("[","")
        proc=proc.replace("]","")
        try:
            cursor.execute("INSERT INTO censys (country,registered_country,city,ip,protocols,date) VALUES ('{}','{}','{}','{}','{}',now())".format(row[1], row[2], row[3], row[4],proc))
            connection.commit()
        except Exception as e:
            print(e)
    print("Table updated...")
except Exception as e:
    print(e)
