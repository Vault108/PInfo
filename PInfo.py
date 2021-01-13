import subprocess
import ipinfo
import dns.resolver
import requests
import rich
from rich.panel import Panel
from rich.console import Console
from rich import print
from rich.console import render_group


def hinfo():
    print("[bold blue] Coming Soon!!!![/bold blue]")


def dinfo():  # Defines the dns command
    console = Console()
    url = console.input(
        "[blue]Enter a Domain[/blue] :warning:[bold red](Do not use WWW)[/bold red]:warning: [blue][/blue]"
    )
    for a in dns.resolver.resolve(url, "a"):
        print(
            "[red]  A Record :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red]",
            a,
        )
    for mx in dns.resolver.resolve(url, "mx"):
        print(
            "[red] MX Record :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red]",
            mx,
        )
    for ns in dns.resolver.resolve(url, "ns"):
        print(
            "[red] NS Record :arrow_forward:  :arrow_forward:  :arrow_forward:  :arrow_forward: [/red]",
            ns,
        )


def ipi():  # Defines ip info command
    console = Console()
    keys_file = open("keys.txt")
    read = keys_file.readlines()
    access_token = read[0].rstrip()
    handler = ipinfo.getHandler(access_token)
    ip_address = console.input("[bold blue]Enter an IP: [/bold blue]")
    details = handler.getDetails(ip_address)
    ip = details.ip
    city = details.city
    region = details.region
    country = details.country_name
    ping = subprocess.check_output("ping -c 4 " + ip_address, shell=True)
    ping_out = ping.decode()
    try:
        hn = details.hostname
        org = details.org
    except AttributeError:
        hn = "No Hostname found for requested IP "
        org = "No Organization found for requested IP"

    @render_group()
    def get_panels():
        yield Panel(
            city + "," + region + " " + country,
            style="black on spring_green2",
            title="Location",
        )
        yield Panel(org, style="black on spring_green1", title="Organization")
        yield Panel(hn, style="black on medium_spring_green", title="Hostnmame")
        yield Panel(ping_out, style="black on cyan2", title="Ping")

    rich.print(Panel(get_panels(), title="INFO FOR " + ip))


def main():


    while True:
        mine = '0.3.0'
        Version = requests.get('https://vault108.github.io/PInfo/about.json').json()["Version"]
        rdate = requests.get('https://vault108.github.io/PInfo/about.json').json()["Date"]
        if Version == mine: print("You have the latest version")
        if Version > mine: print("Version", mine + " is outdated. Version " + Version + " was released " + rdate )
        if Version < mine: print("Do you have a time machine?")
#        print("Welcome")
        print("\nChoose service you want to use : ")
        print(
            """
        1 : Check an IP
        2 : Check a URL
        3 : Check DNS
        0 : Exit"""
        )
        choice = input("\nEnter your choice : ")

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
