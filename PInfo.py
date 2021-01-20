import ipinfo
import dns.resolver
import requests
import rich
from rich.console import Console
from rich import print
mine = '0.4.0'


def hinfo():
    print("[bold blue] Coming Soon!!!![/bold blue]")


def dinfo():  # Defines the dns command
    url = Console().input(
        "[blue]Enter a Domain[/blue] :warning:[bold red1](Do not use WWW)[/bold red1]:warning: [blue]"
    )
    for a in dns.resolver.resolve(url, "a"):
       Console().print(
            "[red3]  A Record :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/]",
            a,
        )
    for mx in dns.resolver.resolve(url, "mx"):
        Console().print(
            "[red3] MX Record :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/]",
            mx,
        )
    for ns in dns.resolver.resolve(url, "ns"):
       Console().print(
            "[red3] NS Record :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/]",
            ns,
        )


def ipi():  # Defines ip info command
    keys_file = open("keys.txt")
    read = keys_file.readlines()
    access_token = read[0].rstrip()
    handler = ipinfo.getHandler(access_token)
    ip_address = Console().input("[bold blue]Enter an IP: [/bold blue]")
    details = handler.getDetails(ip_address)
    ip = details.ip
    city = details.city
    region = details.region
    country = details.country_name
    try:
        hn = details.hostname
        org = details.org
    except AttributeError:
        hn = "No Hostname found for requested IP "
        org = "No Organization found for requested IP"
    Console().print("[red3] INFO FOR [/red3]", ip)
    Console().print("[red3] Location :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red3] ", city + "," + region + country )
    Console().print("[red3] Hostname :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red3] ", hn )
    Console().print("[red3] Organization :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red3] ", org)
    Console().print("[red3] Ping :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red3] ")

def main():


    while True:
        Version = requests.get('https://vault108.github.io/PInfo/about.json').json()["Version"]
        rdate = requests.get('https://vault108.github.io/PInfo/about.json').json()["Date"]
        if Version == mine: Console().print("[cyan1] \n  You have the latest version [/cyan1]")
        if Version > mine: print("Version", mine + " is outdated. Version " + Version + " was released " + rdate )
        if Version < mine: print("Do you have a time machine?")
        print("\n[royal_blue1]Choose service you want to use : [/royal_blue1] ")
        print("[royal_blue1]"
            """
        1 : Check an IP
        2 : Check a URL
        3 : Check DNS
        0 : Exit"""
	"[/royal_blue1]"
        )
        choice = Console().input("\n[royal_blue1]Enter your choice : [/royal_blue1]")

        if choice == "1":
            ipi()
        elif choice == "2":
            hinfo()
        elif choice == "3":
            dinfo()
        elif choice == "0":
            exit()


if __name__ == "__main__":
    main()
