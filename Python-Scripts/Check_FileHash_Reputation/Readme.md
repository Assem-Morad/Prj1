**<u>Description</u>**

A simple Python script that takes serval API keys to iterate on, this will let your scan takes less time than usual.
The more api keys used the less time it takes to send a scan request. for example If you have one API key,then it will take 15 seconds between requests and if you add another api key it will take 7.30 seonds between requests and so on. 


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

    ![execution](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_FileHash_Repution/images/execution.jpg)

- **Output**   

  - vrtoutput.csv content

    ![results](https://github.com/Assem-Morad/Prj1/blob/main/Python-Scripts/Check_FileHash_Reputation/images/results.jpg)

    

  

  

  



