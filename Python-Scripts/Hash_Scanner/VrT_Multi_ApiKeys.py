from ast import Global
from glob import glob
from pip._vendor import requests
from datetime import timedelta
from datetime import datetime
import csv
import json
import time
import argparse

example_text = '''example:

py .\VRT.py -l <api key1> <api key2> <api key3> -f D:/listofhashes.csv -o D:/VtOutPut.csv
py .\VRT.py -a APIKeys.csv -f D:/listofhashes.csv -o D:/VtOutPut.csv
 
'''

parser = argparse.ArgumentParser(description='Customized Virustotal Scripts that takes serval APIs to scan faster', epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-l','--list', help='<Optional> list of APIs to iterate on ',nargs='+',default=[])
parser.add_argument('-a','--ApiList', help='<Optional>csv file that contains list of APIs to iterate on ',type=str)
parser.add_argument('-f','--Hashes', help='<Required> csv file that contains hashes to be scanned ', required=True,type=str)
parser.add_argument('-o','--OutputPath', help='<Required> path of VT output ', required=True,type=str)

args = vars(parser.parse_args())

url = 'https://www.virustotal.com/vtapi/v2/file/report'
count=0
scancount=1

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

def read_Hashes():
    global mylist
    mylist=[]
    with open(args['Hashes'],'r',newline='') as f:
        reader =csv.DictReader(f)
        for row in reader:
            mylist.append(row['Hash'])

def default_display():
    global PauseEqustion,estimatedtime,current_time,td
    PauseEqustion= (60/(len(apikeys)*4))+0.25
    estimatedtime= int(len(mylist)*PauseEqustion)
    current_time = datetime.now().replace(microsecond=0)
    td = timedelta(seconds=estimatedtime) 
    print("====================================================================================================================")
    print(f"Total API Keys : ({len(apikeys)}) Keys")
    print(f"Time Interval Between Requests: ({PauseEqustion:.2f}) Seconds")
    print(f"Total Hashes: ({len(mylist)}) Hashes")
    print(f"Start Execution Date/Time : {current_time}")
    print(f"Total Estimated Time: ({td}) ")
    print(f"Expected Finish Date/Time: {current_time+td}")
    print("===================================================================================================================")
     

def write_results():
    global count,scancount

    if apikeys:

        with open(args['OutputPath'],'w',newline='') as d:
                Writer=csv.writer(d,delimiter=',')
                Writer.writerow(['Hash','Detected Engines'])     
                for row_ in mylist:
                    if row_:
                        while True:                
                            params = {'apikey':apikeys[count], 'resource':row_}
                            response = requests.get(url, params=params)

                            if(response.status_code == 200):
                                json_data=json.loads(response.text)
                                check=json_data['response_code']           #0 means unknown hash #1 means known hash       
                                if check ==0:                                      
                                    Writer.writerow([row_,'Unknown hash '])
                                    print(f"[{scancount}] [+]Hash: {row_} ==> Unknown hash ")

                                elif check !=0:                                    
                                    we=str(json_data['positives']) + '/' + str(json_data['total'])
                                    Writer.writerow([row_,we])
                                    print(f"[{scancount}] [+]Hash: {row_} ==> ({we}) Detected Engines") 

                                count=count+1  
                                time.sleep(PauseEqustion)
                                if count==len(apikeys):
                                    count=0
                                break
                            elif(response.status_code == 204):
                                print('limit exceeded')
                                time.sleep(10)
                            else:
                                print('An Error Occured: '+ response.status_code)
                                time.sleep(10)
                        if count==0:
                            count=0
                    else:
                        print(f"[{scancount}] [-]Hash: Not Found (Empty Cell !)")
                        Writer.writerow(["",""])
                    scancount= scancount+1
        print('Completed , Thanks for your time <3') 
    else:    
        print("API List not found, please set your api keys using one of the paramters defined in the help (-l or -a)") 
                  
if __name__ == "__main__":
    apikeys_list()
    read_Hashes()
    default_display()
    write_results()
