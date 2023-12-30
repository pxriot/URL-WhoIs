import whois

def whois_scan(domain):
    try:
        result = whois.whois(domain)
        print(result)
    except Exception as e:
        print("An error occurred:", str(e))

website = input('Enter Hostname: ')
whois_scan(website)