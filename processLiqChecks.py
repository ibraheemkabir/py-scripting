from liqScript import getLiquidity
import requests
import pandas as pd
import openpyxl
import datetime

INTERVAL = 12
url = "https://emailapi.netcorecloud.net/v5/mail/send"
item = {"currency":'RINKEBY:0xfe00ee6f00dd7ed533157f6250656b4e007e7179'}
file_path = "CURRENCY_LIST.xlsx"
data = pd.read_excel(file_path)

def processCurrencyList():
    for row in data.itertuples(index=True, name=None):
        processCurrencyInfo({'currency':row[1],'minimum':row[2],'last_update':row[3],'index': row[0],'admin_email':row[4]})

def sendMail(liquidity,email):
    print('do send grid')
    if liquidity:
        payload = "{\"from\":{\"email\":\"ibraheemkabir9@pepisandbox.com\",\"name\":\"Bridge Liquidity Information\"},\"subject\":\"Your Liquidity Level is Low\",\"content\":[{\"type\":\"html\",\"value\":\"Hello, Your Liquidity level is now {liquidity} which is lower than your set limit, add liquidity now\"}],\"personalizations\":[{\"to\":[{\"email\":\"{email}\",\"name\":\"Test\"}]}]}"
        headers = {
            'api_key': "4f10ca6bd9691e40b077e8de12499ab4",
            'content-type': "application/json"
        }
        response = requests.request("POST", url, data=payload, headers=headers)

def updateDate(index):
    wb = openpyxl.load_workbook(file_path)
    wb['Sheet1'].cell(column=(index+2), row=3, value=datetime.datetime.now())
    wb.save(file_path)
    
def processCurrencyInfo(item=item):
    print(item,'Processitem')
    try:
        liquidity = getLiquidity(item['currency'])
        time_elapsed_btw_notifications = datetime.datetime.now() - item['last_update']
        
        if liquidity['liquidity']:
            
            if (item['minimum'] >= int(float(liquidity['liquidity']))) and (time_elapsed_btw_notifications.seconds > (3600*INTERVAL)):
                
                sendMail(liquidity['liquidity'],item['admin_email'])
                updateDate(item['index'])
                print('notification email sent for'+ item['currency'] + liquidity['liquidity'] +  'left')
                
        return liquidity
    
    except requests.exceptions.HTTPError as error:
        print(error)

def main():
    processCurrencyList()

if __name__ == '__main__':
    main()