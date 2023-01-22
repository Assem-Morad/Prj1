import requests
import json
import csv
import argparse
import time
from datetime import timedelta
from datetime import datetime

example_text = '''example:

py .\CheckIP_Reputation.py -l <api key1> <api key2> <api key3> -p D:/ListOfIPs.csv -o D:/Abuseipdb.csv -m 60
py .\CheckIP_Reputation.py -a APIKeys.csv -f D:/ListOfIPs.csv -o D:/Abuseipdb.csv -m 60
 
'''

parser = argparse.ArgumentParser(description='Customized AbuseIpdb Script that takes serval APIs to boost the amount of queries per day', epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-l','--list', help='<Optional> list of APIs to iterate on ',nargs='+',default=[])
parser.add_argument('-a','--ApiList', help='<Optional>csv file that contains list of APIs to iterate on ',type=str)
parser.add_argument('-p','--IPs', help='<Required> csv file that contains IPs to be scanned ', required=True,type=str)
parser.add_argument('-m','--MaximumAge', help='<Optional> determines how old the reports considered in the query search can be. default 45 days ',type=str)
parser.add_argument('-o','--OutputPath', help='<Required> path of AbuseIpdb output ', required=True,type=str)
args = vars(parser.parse_args())


def apikeys_list():
    global apikeys
    apikeys=[]
    if args['ApiList']:
        with open(args['ApiList'],'r',newline='') as q:
            reader =csv.DictReader(q)
            for _row in reader:
                apikeys.append(_row['ApiKeys'])

    elif args['list']:
        apikeys=args['list']

def read_ips():
    global iplist
    iplist=[]
    with open(args['IPs'],'r',newline='') as f:
        reader =csv.DictReader(f)
        for row in reader:
            iplist.append(row['IPs'])

def default_display():
    global current_time,maxreq
    maxreq= len(apikeys)*1000
    current_time = datetime.now().replace(microsecond=0)
    print("====================================================================================================================")
    print(f"Total API Keys : ({len(apikeys)}) Keys")
    print(f"Total IPs to be scanned: ({len(iplist)}) IPs")
    print(f"Execution Date/Time : {current_time}")
    print(f"Total Number of API requests: '{maxreq}' Requests")
    print("===================================================================================================================")

def write_csv():
    global count,scancount,url,MaximumAge
    url = 'https://api.abuseipdb.com/api/v2/check'
    count = 0
    scancount= 1
    MaximumAge= args['MaximumAge']
    if apikeys:
        with open(args['OutputPath'],"w", newline='') as f:
            dict_keys = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt']
            writer = csv.DictWriter(f, fieldnames=dict_keys)
            writer.writeheader()
            for ip in iplist:
                if ip:
                    while count < len(apikeys):
                        requsted_ip = {'ipAddress': ip,'maxAgeInDays': MaximumAge}
                        req_header = {'Accept':'application/json', 'key':apikeys[count]}
                        response= requests.get(url=url,headers=req_header,params=requsted_ip)

                        if response.status_code == 200:
                            Data_dict = json.loads(response.text)
                            key_value = Data_dict["data"]
                            writer.writerow(key_value)
                            print(f"""[{scancount}] [+]IP: "{ip}" ==> ({key_value})\n""")
                            scancount +=1
                            break

                        elif response.status_code == 429:
                                print('limit exceeded, switching to the next api key!')
                                time.sleep(10)
                                count +=1
                        else:
                            print('An Error Occured: '+ response.status_code)
                            time.sleep(10)

                else:
                    print(f"[{scancount}] [-]Hash: Not Found (Empty Cell !)")
    else:    
        print("API List not found, please set your api keys using one of the paramters defined in the help (-l or -a)")
               

if __name__ == "__main__":
    apikeys_list()
    read_ips()
    default_display()
    write_csv()

