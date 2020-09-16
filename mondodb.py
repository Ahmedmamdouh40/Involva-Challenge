import pymongo
class mongodbConfig():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["coffee_supply"]

    machines = mydb["coffee_machines"]
    pods = mydb["coffee_pods"]
    print("Config done")

    machine_list= [
        {"code":"CM101" , "type":"COFFEE_MACHINE" , "size":"large" , "waterLine":"false"  , "model":"base"},
        {"code":"CM102" , "type":"COFFEE_MACHINE" , "size":"large" , "waterLine":"true"  , "model":"premium"},
        {"code":"CM103" , "type":"COFFEE_MACHINE" , "size":"large" , "waterLine":"true" , "model":"deluxe"},
        {"code":"CM001" , "type":"COFFEE_MACHINE" , "size":"small" , "waterLine":"false"  , "model":"base"},
        {"code":"CM002" , "type":"COFFEE_MACHINE" , "size":"small" , "waterLine":"false"  , "model":"premium"},
        {"code":"CM003" , "type":"COFFEE_MACHINE" , "size":"small" , "waterLine":"true"  , "model":"deluxe"},
        {"code":"EM001" , "type":"ESPRESSO_MACHINE" , "size":"espresso" , "waterLine":"false"  , "model":"base"},
        {"code":"EM002" , "type":"ESPRESSO_MACHINE" , "size":"espresso" , "waterLine":"false"  , "model":"premium"},
        {"code":"EM003" , "type":"ESPRESSO_MACHINE" , "size":"espresso" , "waterLine":"true"  , "model":"deluxe"},
    ]

    pods_list = [
        {"code":"CP001" , "type":"COFFEE_POD" , "size":"small" , "falvor":"vanilla" , "packSize":"1"},
        {"code":"CP003" , "type":"COFFEE_POD" , "size":"small" , "falvor":"vanilla" , "packSize":"3"},
        {"code":"CP011" , "type":"COFFEE_POD" , "size":"small" , "falvor":"caramel" , "packSize":"1"},
        {"code":"CP013" , "type":"COFFEE_POD" , "size":"small" , "falvor":"caramel" , "packSize":"3"},
        {"code":"CP021" , "type":"COFFEE_POD" , "size":"small" , "falvor":"psl" , "packSize":"1"},
        {"code":"CP023" , "type":"COFFEE_POD" , "size":"small" , "falvor":"psl" , "packSize":"3"},
        {"code":"CP031" , "type":"COFFEE_POD" , "size":"small" , "falvor":"mocha" , "packSize":"1"},
        {"code":"CP033" , "type":"COFFEE_POD" , "size":"small" , "falvor":"mocha" , "packSize":"3"},
        {"code":"CP041" , "type":"COFFEE_POD" , "size":"small" , "falvor":"hazelnut" , "packSize":"1"},
        {"code":"CP043" , "type":"COFFEE_POD" , "size":"small" , "falvor":"hazelnut" , "packSize":"3"},
        {"code":"CP101" , "type":"COFFEE_POD" , "size":"large" , "falvor":"vanilla" , "packSize":"1"},
        {"code":"CP103" , "type":"COFFEE_POD" , "size":"large" , "falvor":"vanilla" , "packSize":"3"},
        {"code":"CP111" , "type":"COFFEE_POD" , "size":"large" , "falvor":"caramel" , "packSize":"1"},
        {"code":"CP113" , "type":"COFFEE_POD" , "size":"large" , "falvor":"caramel" , "packSize":"3"},
        {"code":"CP121" , "type":"COFFEE_POD" , "size":"large" , "falvor":"psl" , "packSize":"1"},
        {"code":"CP123" , "type":"COFFEE_POD" , "size":"large" , "falvor":"psl" , "packSize":"3"},
        {"code":"CP131" , "type":"COFFEE_POD" , "size":"large" , "falvor":"mocha" , "packSize":"1"},
        {"code":"CP133" , "type":"COFFEE_POD" , "size":"large" , "falvor":"mocha" , "packSize":"3"},
        {"code":"CP141" , "type":"COFFEE_POD" , "size":"large" , "falvor":"hazelnut" , "packSize":"1"},
        {"code":"CP143" , "type":"COFFEE_POD" , "size":"large" , "falvor":"hazelnut" , "packSize":"3"},
        {"code":"EP003" , "type":"ESPRESSO_POD" , "size":"espresso" , "falvor":"vanilla" , "packSize":"3"},
        {"code":"EP005" , "type":"ESPRESSO_POD" , "size":"espresso" , "falvor":"vanilla" , "packSize":"5"},
        {"code":"EP007" , "type":"ESPRESSO_POD" , "size":"espresso" , "falvor":"vanilla" , "packSize":"7"},
        {"code":"EP013" , "type":"ESPRESSO_POD" , "size":"espresso" , "falvor":"caramel" , "packSize":"3"},
        {"code":"EP015" , "type":"ESPRESSO_POD" , "size":"espresso" , "falvor":"caramel" , "packSize":"5"},
        {"code":"EP017" , "type":"ESPRESSO_POD" , "size":"espresso" , "falvor":"caramel" , "packSize":"7"}, 
    ]

    machineDocumentExist = machines.count_documents({})
    if machineDocumentExist:
        print("machines already inserted")
    else:
        machines.insert(machine_list)
        print("machines inserted now")

    
    podDocumentExist = pods.count_documents({})
    if podDocumentExist:
        print("pods already inserted")
    else:
        pods.insert(pods_list)
        print("pods inserted now")
    
