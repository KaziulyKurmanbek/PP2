import json
with open("/Users/qurmanbek/Desktop/GitHub/PP2/lab04/JSON/sample-data.json", "r") as f:
    data = json.load(f)
print("Inherit status")
print("="*50)
print("DN")
print("-"*50)
for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn")
    descr = attr.get("descr")
    speed = attr.get("speed")
    mtu = attr.get("mtu")
    print(f"{dn:50} {descr:11} {speed:7} {mtu}")