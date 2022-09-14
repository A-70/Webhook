from colorama import Fore, init
from colorama import init
from numpy import insert
import sqlite3 as sql
import colorama
import ctypes
import string
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from os import system
system("cls")



system("cls")
system("pip install numpy")
system("pip install colorama")
system("cls")


init()
time.sleep(1)

print(Fore.RED + """

             █████╗   ████████═╗      ██████═══╗
            ██╔══██╗       ███ ║    ██      ██ ║
            ███████║      ███╔═╝    ██      ██ ║
            ██╔══██║     ███╔╝      ██      ██ ║
            ██║  ██║    ██╔═╝         ██████ ╔═╝
            ╚═╝  ╚═╝    ══╝            ╚═════╝

                    https://discord.gg/wz8Ktqp2SW  // Designed by A70
                                                        """)

time.sleep(2)


QRequestsWebhook = input(str("webhook: "))
print(Fore.WHITE + "")

contend = input(str("      mensaje: "))
print()

QRequestsUser = input(str("    username: "))
print()

title_x = input(str("   title:"))
print()

QRequestsIconUrl = input(str("     icon url: "))
print()

QRequestsName = input(str("     name: "))
print()

QRequestsUrl = input(str("      url: "))
print()

QRequestsFooter = input(str("       footer: "))
print()

QRequestsname = input(str("     titulo descripción: "))
print()

QRequestsDescription = input(str("      descripción: "))
print()

QRequestsImage = input(str("        image: "))
print()


webhook = DiscordWebhook(url=QRequestsWebhook,
                         username=QRequestsUser, content=contend)

embed = DiscordEmbed(title=title_x,
                     color="FF0000")
embed.set_author(
    name=QRequestsName, url=QRequestsUrl, icon_url=QRequestsIconUrl)
embed.set_footer(text=QRequestsFooter)
embed.set_timestamp()
embed.add_embed_field(name=QRequestsname, value=QRequestsDescription)
embed.set_image(url=QRequestsImage)
embed.set_thumbnail(url=QRequestsImage)


webhook.add_embed(embed)
response = webhook.execute()

time.sleep(0.5)
print("mensaje enviado!")
