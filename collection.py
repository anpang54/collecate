# start
name = "Collection"
version = "0.1.1"
print("\n\t\033[1m{name} v{version}\033[0m\n")

# get data
from json import load, dump
with open("data.json", "r") as file:
    data = load(file)

# loop
while True:

    # get item
    item = input("Brick: ").lower()

    if item == "save":
        with open("data.json", "w") as file:
            dump(data, file, indent=4)
        print("Successfully saved.\n")
        continue
    if item == "exit":
        print("Exiting...\n")
        exit()

    # inspect
    print(f"Inspecting {item}... ", end="")
    if item in data and data[item] != 0:
        print(f"you have {data[item]}.")
    else:
        print(f"you don't have any {item}.")
    print()

    # get change
    change = input("Change (+/-): ")

    if change == "":
        print("No action done.")
        pass

    data[item] = (data[item] if item in data else 0) + int(change)
    print("Successfully changed.\n")
