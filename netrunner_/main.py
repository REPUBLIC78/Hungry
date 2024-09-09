from netrunner_.function import *
    
while True:
    try:
        command = input()
        
        if command[0] == '/':
            
            if '/scrape' in command:
                url = command[8:]
                scrape_url(url)
                
            if '/money' in command:
                money_courses()
            
            if '/findlinks' in command:
                url = command[10:]
                find_links(url)
                
            if '/exit' in command:
                break
            
            if '/status' in command:
                url = command[8:]
                response_status(url)
        else: 
            continue
    except:
        continue
            
