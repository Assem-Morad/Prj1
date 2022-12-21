**<u>Description</u>**

A simple Python script that checks reputation of a list of IP addresses  against AbuseIPDB API V2.

This script iterates on serval API keys, allowing you to scan a large number of IPs at once .

<u>**Usage**</u> 

- **Help**

  - To get script capabilities and examples, use `-h` 

    ![help](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_IPs_Reputations/images/help.jpg)

- **Examples**

  - ```
    py .\CheckIP_Reputation.py -l <api key1> <api key2> <api key3> -f D:/ListOfIPs.csv -o D:/Abuseipdb.csv -m 60
    ```

  - ```
    py .\CheckIP_Reputation.py -a APIKeys.csv -f D:/ListOfIPs.csv -o D:/Abuseipdb.csv -m 60
    ```

    ![execution](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_IPs_Reputations/images/execution.jpg)

- **Output**   

  - Abuseipdb.csv content

    ![results](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_IPs_Reputations/images/results.jpg)

    

  

  



