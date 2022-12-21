**<u>Description</u>**

A simple Python script that iterates on multiple API keys, allowing your scan to take less time than usual.
The more API keys that are used, the faster it is to send a scan request.  If you only have one API key, it will take 15 seconds between requests, and if you add another, it will take 7.30 seconds, and so on.. 


<u>**Usage**</u> 

- **Help**

  - To get script capabilities and examples, use `-h` 

    ![help](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_FileHash_Reputation/images/help.jpg)

- **Examples**

  - ```
    py.exe .\VrT_Multi_ApiKeys.py -a .\APIKeys.csv -f .\sample.csv -o vrtoutput.csv
    ```

  - ```
    py.exe .\VrT_Multi_ApiKeys.py -l ''<apikey1>'' "<apikey2>" "<apikey3>" -f .\sample.csv -o vrtoutput.csv
    ```

    ![execution](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_FileHash_Reputation/images/execution.jpg)

- **Output**   

  - vrtoutput.csv content

    ![results](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_FileHash_Reputation/images/results.jpg)

    

  

  

  



