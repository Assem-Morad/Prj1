**<u>Description</u>**

A simple Python script that checks IP reputation using the AbuseIPDB API v2.

this script iterates on serval API keys, allowing you to scan a large number of IPs at once .

<u>**Usage**</u> 

- **Help**

  - To get script capabilities and examples, use `-h` 

    ![help](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_IPs_Reputions/images/help%20.jpg)

- **Examples**

  - ```
    py .\CheckIP_Reputation.py -l <api key1> <api key2> <api key3> -f D:/ListOfIPs.csv -o D:/Abuseipdb.csv -m 60
    ```

  - ```
    py .\CheckIP_Reputation.py -a APIKeys.csv -f D:/ListOfIPs.csv -o D:/Abuseipdb.csv -m 60
    ```

    ![execution](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_IPs_Reputions/images/execution%20.jpg)

- **Output**   

  - vrtoutput.csv content

    ![results](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_IPs_Reputions/images/results%20.jpg)

    

  

  

  



