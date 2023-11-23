import datetime

from givenergy_modbus.client import GivEnergyClient
from givenergy_modbus.model import inverter
from givenergy_modbus.model.plant import Plant

client = GivEnergyClient(host="192.168.4.70")
client.set_charge_slot(slot=1, times=(datetime.time(hour=0, minute=30), datetime.time(hour=6, minute=30)))

p = Plant(number_batteries=1)
client.refresh_plant(p, full_refresh=True, isAIO=False, isAC=False)

print(p.inverter.inverter_serial_number)

stats = client.get_inverter_stats()

print(stats[2])
print(inverter.Generation.from_fw_version(stats[1]))
print(inverter.Model.from_device_type_code(stats[0]))
print(stats[1])

print(p.inverter.dict())
print(p.batteries[0].dict())