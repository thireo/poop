import matplotlib.pyplot as plt
import datetime as dt

types = ["No Bowel Movement", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7"]
urgencies = ["Not Urgent", "Urgent"]
sizes = ["Small", "Small-Medium", "Medium", "Medium-Large", "Large", "Very-Large"]
bloodyness = ["No","Yes"]
timeywhimey = "%Y-%m-%d %H:%M"

data = []

getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]

with open("export_20210912.csv","r") as file:
    for line in file.readlines():
        #print(line.split(",")[2].split("\"")[1])
        #if(line.split(",")[2].split("\"")[1] == types[5]):
        dataline = line.split(",")
        if(dataline[0].find("_id") < 0):
            print(dataline)

            temptime = dt.datetime.strptime(dataline[1].split("\"")[1],timeywhimey).timestamp()
            temptype = types.index(line.split(",")[2].split("\"")[1])
            if(temptype != types.index("No Bowel Movement")):
                tempurgency = urgencies.index(line.split(",")[5].split("\"")[1]) 
                tempsize = sizes.index(line.split(",")[4].split("\"")[1])
                tempblood = bloodyness.index(line.split(",")[6].split("\"")[1])
            
            data.append({"time":temptime,"type":temptype,"urgency":tempurgency,"size":tempsize,"blood":tempblood})
            #print(types.index(line.split(",")[2].split("\"")[1]))
    print(getValues("type",data))
    #print(file.readline())
    #print(file.readline().split(",")[2])
data = data[::-1]
plt.plot(getValues("time",data))
plt.show()