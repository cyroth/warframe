#!/usr/bin/env python3
# Warframe blessing formatter

from configparser import ConfigParser
from dataclasses import dataclass
from enum import Enum
from typing import TypeVar
import datetime as dt
import sys

T = TypeVar('T')

def assert_in_enum(string: str, enum: T) -> T:
    if string not in [variant.value for variant in enum]:
        print(f"\033[31mInvalid relay: '{string}'\033[0m")
        print(f"Valid relays are: {[variant.value for variant in enum]}")
        quit(1)
    
    return enum(string)


class Region(Enum):
    Asia = "as"
    Europe = "eu"
    NorthAmerica = "na"


class Relay(Enum):
    Larunda = "larunda"
    Strata = "strata"
    Kronia = "kronia"
    Maroo = "maroo"
    Orcus = "orcus"


class Role(Enum):
    Affinity = "affinity"
    Credit = "credit"
    Resource = "resource"
    Damage = "damage"
    Health = "health"
    Shield = "shield"


@dataclass
class BlessConfig:
    name: str
    region: Region
    instance: int
    roles: dict[Role, str]

    def __init__(self, file: str) -> None:
        config = ConfigParser()
        if not config.read(file):
            print(f"\033[31mCould not read from file: '{file}'\033[0m")
            quit(1)

        # Setup
        self.relay = assert_in_enum(config.get('bless_setup', 'relay_name'), Relay)
        self.instance: int = config.get('bless_setup', 'relay_instance')

        # Bless
        roles: list[Role] = list(map(lambda role: Role(role), "affinity credit resource damage health shield".split(" ")))
        names: list[str] = [config.get('roles', role.value) for role in roles]
        self.roles: dict[Role, str] = {role: name for (role, name) in zip(roles, names) if not not name}

        # Config
        self.name: str = config.get('config', 'my_name')
        self.region = assert_in_enum(config.get('config', 'region'), Region)

    # For debugging purposes
    def __str__(self) -> str:
        return f"""BlessConfig {{
    name: {self.name},
    region: {self.region.name},
    relay: {self.relay.name},
    instance: {self.instance},
    roles: {{ {", ".join([f"{role.value}: {name}" for (role, name) in self.roles.items()]) } }}
}}"""

    def command(self) -> str:
        # Calculate time until bless
        delta = dt.timedelta(hours=1)
        now = dt.datetime.now()
        next_hour: dt.datetime = (now + delta).replace(second=0, minute=0)
        wait_minutes: int = (next_hour - now).seconds // 60
        global wait_min_global
        wait_min_global = wait_minutes

        return f"!bless pc {self.region.value} {self.relay.value} {self.instance} {wait_minutes} min " + \
            " ".join(map(lambda role: role.value, self.roles.keys()))


separator: str = "=" * 80
bless_config = BlessConfig("bless.ini" if len(sys.argv) == 1 else sys.argv[1])
message: str = f"\n{separator}\n".join([
    "```", 
    f"{bless_config.command()}",
    f"BLESSING ROLES: " + \
        " | ".join(f"@{name} ==> {role.name}" for (role, name) in bless_config.roles.items()) + \
        " || Blessing in " + str(wait_min_global) + " minutes" + \
        (" (Shield bless will be delayed by 1 minute)" if Role.Shield in bless_config.roles.keys() else ""),
    "\n".join(
        f"/w {name} Reminder for bless at {bless_config.relay.name} {bless_config.instance} in {bless_config.region.name} region. " + \
            f"Role: {role.name}" for (role, name) in bless_config.roles.items()),
    f"Roll call: @{' @'.join(bless_config.roles.values())} :clem:",
    f"Thanks to {', '.join(list(bless_config.roles.values())[:-1])} and {list(bless_config.roles.values())[-1]} for blessing.",
    "60 second warning to leave the relay before shield bless" if Role.Shield in bless_config.roles.keys() else "No shield",
    "```"
])

print(message)
input("Press Enter to continue...")