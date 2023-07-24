# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
# import data from a web server

import urllib.request
import urllib.error

def webpage(url):
    try:
        weburl = urllib.request.urlopen(url)
        
    # Chat GPT error handler!   
    except urllib.error.URLError as e:
       if hasattr(e, 'reason'):
           print('ERROR: Cannot reach the server.')
           print('Reason: ', e.reason)
       elif hasattr(e, 'code'):
          print('ERROR: Server cannot fulfill this request.')
          print('Error code: ', e.code)
    else:
        # everything is fine
        print("Result Code:", weburl.getcode())
        data = weburl.read()
        print(data)
    

def main():
    
    webpage("https://www.linkedin.com/in/dave-dempski")
    
    webpage("http://www.google.com")
    
 
if __name__ == "__main__":
    main()
