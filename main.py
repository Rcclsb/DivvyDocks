# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json, urllib.request, time


def get_docks(ids):
    with urllib.request.urlopen('https://gbfs.divvybikes.com/gbfs/en/station_status.json') as response:
        html = response.read()
    data = json.loads(html)
    station_data = data.get("data").get("stations")
    final_data = []
    for station in station_data:
        if int(station.get("station_id")) in ids:
            useful_data = {"station_id":station.get("station_id"),"bikes_available": station.get("num_bikes_available"), "docks_available": station.get("num_docks_available"), "ebikes_avaiable": station.get("num_ebikes_available")}
            final_data.append(useful_data)
    return {"time": time.time(), "data": final_data}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ellis Ave & 58 = 328
    # Lake Park Ave & 56 = 345
    # Ellis Ave & 55 = 420
    # University Ave & 57 = 423
    # Museum of Science and Industry = 424
    # Harper Ave & 59 = 425
    # Ellis Ave & 60 = 426
    complete_data = []
    cycle_start = time.time()
    while True:
        complete_data.append(get_docks([423, 328, 426, 420, 345, 424, 425]))
        if time.time()>cycle_start+3600:
            file = open("dock_data_"+str(round(time.time()))+".json","w")
            file.write(json.dumps(complete_data))
            file.close()
            complete_data = []
            cycle_start = time.time()
        time.sleep(60)
    print(complete_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
