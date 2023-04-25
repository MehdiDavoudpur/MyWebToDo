import json


myDict = {}
with open("myJSON.json", 'r') as file:
    a = file.read()
if len(a) == 0:
    with open("myJSON.json", 'w') as file:
        file.write("{}")

with open("myJSON.json", 'r') as file:
    myDict = json.load(file)
    i = len(myDict)
while True:
    newItem = input("Enter New Item & Press Enter: ")
    i = i + 1
    myDict[i] = newItem
    with open("myJSON.json" , 'w') as file:
        json.dump(myDict, file)
    print(myDict)

