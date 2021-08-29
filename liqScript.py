import requests
import sys

#response = requests.get("http://api.open-notify.org/astros.json")
#print(response.json())

args = sys.argv

print(args)

def validateCurrency(cur):
    if(len(cur.split(':')) < 2):
        print('invalid currency passed')
        return False
    else:
        return True

def getLiquidity(arg=args[len(args)-1]): 
    try:
        
        if not arg:
            
            print('No Currency argument provided')
            
            return 'No Currency argument provided'
            
        elif not validateCurrency(arg):
            
            print('invalid currency passed')
            
            return 'invalid currency passed'
            
        else:
            
            response2 = requests.post("https://an54zzyt9h.execute-api.ap-south-1.amazonaws.com/default/test",json={"command":"getAvaialableLiquidity","data":{"userAddress": arg.split(':')[0], "currency": arg}})
            response2.raise_for_status()
            print(response2.json())
            if response2.json()["liquidity"]:
                # call send grid here
                print("Available Liquidity " + response2.json()["liquidity"] )
                return response2.json()
                
    except requests.exceptions.HTTPError as error:
        print(error)
 
def main():
    getLiquidity()

if __name__ == '__main__':
    main()   