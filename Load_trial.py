from datetime import datetime
import requests


# count = 0
#
# device_id = '3'
# i = 0
# lasttime = ''
# Brand = 'Lee cooper '
# Location = 'Pantaloons-Phoenix Mall White Field'
#
# while count < 5:
#
#     CurrTm = datetime.now().replace(microsecond=0)
#     id = device_id+'-'+str(i)+'-'+str(CurrTm)
#
#     string1 = '{ "index" : { "_index": "useriylikedata_3", "_type" : "external", "_id" : '+'"'+id+'"'+' }}\n'
#     string2 = '{"DeviceId": '+str(device_id)+ ', "Brand": '+'"'+str(Brand)+'"'+', "Location": '+'"'+str(Location)+'"'+', "Count": '+str(1) + ',"TimeStampVal": '+'"'+str(CurrTm)+'"' + '}\n'
#     print(string1)
#     jsonfile = open('device_upd1.json','a')
#     jsonfile.write(string1)
#     jsonfile.write(string2)
#     jsonfile.close()
#
#     count+=1
#     i+=1




    # Upload the data from JSON file onto Kibana every 1 minute

url = 'https://search-iylike2019-eelpyks3hd2dsvr7etxryrzewa.ap-south-1.es.amazonaws.com/_bulk'
headers = {'content-type': 'application/json'}

jsonfile=open('device_upd1.json','r+')
data = jsonfile.read()
res = requests.put(url,
                   data=data,
                   headers=headers,
                   )
#jsonfile.truncate(0)
jsonfile.close()

print(res.content)
#print(res.content)
#time.sleep(1)