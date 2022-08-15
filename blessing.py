# Warframe blessing formater
# edit the string for roles you want to assign

# assign roles
affinity_bless = "tenno1"
credit_bless = "tenno2"
resource_bless = "tenno3"
damage_bless = "tenno4"
health_bless = "tenno5"
shield_bless = "tenno6"

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
print(f"BLESSING ROLES: @{affinity_bless} ---> {bless_types[0]} | ", end = "")
if total_blessers > 1:
    print(f"@{credit_bless} ---> {bless_types[1]} | ", end = "")
else:
    pass
if total_blessers > 2:
    print(f"@{resource_bless} ---> {bless_types[2]} | ", end = "")
else:
    pass
if total_blessers > 3:
    print(f"@{damage_bless} ---> {bless_types[3]} | ", end = "")
else:
    pass
if total_blessers > 4:
    print(f"@{health_bless} ---> {bless_types[4]} | ", end = "")
else:
    pass
if total_blessers > 5:
    print(f"@{shield_bless} ---> {bless_types[5]}  | ", end = "")
else:
    pass

# calculate and output time until bless
import datetime
delta = datetime.timedelta(hours=1)
now = datetime.datetime.now()
next_hour = (now + delta).replace(second=0, minute=0)
wait_minutes = (next_hour - now).seconds/60
wait_minutes = int(wait_minutes)
print(f"BLESSING IN {wait_minutes} MINS", end = "")
if total_blessers > 5:
    print(f", SHIELD BLESS WILL BE AT xx:01")
else:
    print()

print("========================================================")
# nag whisper for missing blessers. nags assume you are blessing affinity
nag_mesage = f"Reminder for bless at {relay_name} {relay_instance}. You'll be on"
thank_list = [credit_bless]
if total_blessers > 1:
    print(f"/w {credit_bless} {nag_mesage} {bless_types[1]}")
else:
    pass
if total_blessers > 2:
    print(f"/w {resource_bless} {nag_mesage} {bless_types[2]}")
    thank_list.append(resource_bless)
else:
    pass
if total_blessers > 3:
    print(f"/w {damage_bless} {nag_mesage} {bless_types[3]}")
    thank_list.append(damage_bless)
else:
    pass
if total_blessers > 4:
    print(f"/w {health_bless} {nag_mesage} {bless_types[4]}")
    thank_list.append(health_bless)
else:
    pass
if total_blessers > 5:
    print(f"/w {shield_bless} {nag_mesage} {bless_types[5]}")
    thank_list.append(shield_bless)
else:
    pass
print ("Thanks to ", end = "")
print(', '.join(thank_list), end = "")
print(" for blessing tonight")
print("```")
