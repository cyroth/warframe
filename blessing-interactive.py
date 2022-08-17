#!/usr/bin/env python3
# Warframe blessing formater
# edit the string for roles you want to assign

# your name. needed so you don't thank yourself
my_name = "tenno1"

# assign roles
affinity_bless = "tenno1"
credit_bless = "tenno"
resource_bless = "tenno"
damage_bless = "tenno"
health_bless = "tenno"
shield_bless = "tenno"

# get info for message to paste to #bless in Discord
region = "as"
bless_types = ['affinity', 'credit', 'resource', 'damage', 'health', 'shield']
relay_list = ['larunda', 'strata', 'kronia', 'maroo', 'orcus']
relay_name = None
print (f"Valid relays {relay_list}")
while relay_name not in relay_list[0:]:
    relay_name = input("Relay name? ")
relay_instance = input("Relay instance? ")

# get count of blessers
total_blessers = input("How many blessers? ")
total_blessers = int (total_blessers)

print("```")
print("========================================================")
# output !bless command
print(f"!Bless pc {region} {relay_name} {relay_instance} 15m ", end = "")
print(*bless_types[0:total_blessers])

# output roles to paste into relay chat
print("========================================================")
print(f"BLESSING ROLES: @{affinity_bless} ---> {bless_types[0].capitalize()} | ", end = "")
if total_blessers > 1:
    print(f"@{credit_bless} ---> {bless_types[1].capitalize()} | ", end = "")
else:
    pass
if total_blessers > 2:
    print(f"@{resource_bless} ---> {bless_types[2].capitalize()} | ", end = "")
else:
    pass
if total_blessers > 3:
    print(f"@{damage_bless} ---> {bless_types[3].capitalize()} | ", end = "")
else:
    pass
if total_blessers > 4:
    print(f"@{health_bless} ---> {bless_types[4].capitalize()} | ", end = "")
else:
    pass
if total_blessers > 5:
    print(f"@{shield_bless} ---> {bless_types[5].capitalize()}  | ", end = "")
else:
    pass

# calculate and output time until bless
import datetime
delta = datetime.timedelta(hours=1)
now = datetime.datetime.now()
next_hour = (now + delta).replace(second=0, minute=0)
wait_minutes = (next_hour - now).seconds/60
wait_minutes = int(wait_minutes)
print(f"Blessing in {wait_minutes} minutes", end = "")
if total_blessers > 5:
    print(f" | Shield bless will be at xx:01")
else:
    print()
print("========================================================")

# nag whisper for missing blessers and list for thanks
nag_mesage = f"Reminder for bless at {relay_name.capitalize()} {relay_instance}. You'll be on"
roll_call = [affinity_bless]
print(f"/w {affinity_bless} {nag_mesage} {bless_types[0].capitalize()}")
if total_blessers > 1:
    print(f"/w {credit_bless} {nag_mesage} {bless_types[1].capitalize()}")
    roll_call.append(credit_bless)
else:
    pass
if total_blessers > 2:
    print(f"/w {resource_bless} {nag_mesage} {bless_types[2].capitalize()}")
    roll_call.append(resource_bless)
else:
    pass
if total_blessers > 3:
    print(f"/w {damage_bless} {nag_mesage} {bless_types[3].capitalize()}")
    roll_call.append(damage_bless)
else:
    pass
if total_blessers > 4:
    print(f"/w {health_bless} {nag_mesage} {bless_types[4].capitalize()}")
    roll_call.append(health_bless)
else:
    pass
if total_blessers > 5:
    print(f"/w {shield_bless} {nag_mesage} {bless_types[5].capitalize()}")
    roll_call.append(shield_bless)
else:
    pass
print("========================================================")

# roll call and thank you message
roll_call.remove(my_name)
print ("Roll call. @", end = "")
print(' @'.join(roll_call), end = "")
print(" :clem:")
print("========================================================")
print ("Thanks to ", end = "")
print(', '.join(roll_call), end = "")
print(" for blessing")
print("```")
