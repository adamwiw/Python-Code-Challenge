import csv
from solution.port import Port

class Solution:
    def __init__(self, VLANsLocation):
        self.__primaryPorts = []
        self.__secondaryPorts = []
        self.__portsIntersection = []
        
        self.__loadVLANs(VLANsLocation)
        self.__populateIntersection()
        self.__sortPorts()

    def __appendVLAN(self, vlan):
        port = Port(int(vlan["device_id"]), int(vlan["vlan_id"]))
        if int(vlan["primary_port"]): 
            self.__primaryPorts.append(port)
        else:
            self.__secondaryPorts.append(port)
    
    def __loadVLANs(self, VLANsLocation):
        with open(VLANsLocation) as VLANs:
            reader = csv.reader(VLANs)
            headers = next(reader)

            for line in reader:
                try:
                    self.__appendVLAN({key: int(value) for key, value in zip(headers, line)})
                except ValueError as e:
                    e.args = ("Invalid VLAN record:", line)
                    raise 
                
    def __populateIntersection(self):
        self.__portsIntersection = list(set(self.__primaryPorts).intersection(self.__secondaryPorts))
                
    def __sortPorts(self):
        self.__primaryPorts.sort(key=lambda x: (x.vlanId, x.deviceId))
        self.__secondaryPorts.sort(key=lambda x: (x.vlanId, x.deviceId))
        self.__portsIntersection.sort(key=lambda x: (x.vlanId, x.deviceId))

    def processRequest(self, requestId, redundant):        
        if redundant:
            primaryPortIndex = self.__primaryPorts.index(self.__portsIntersection[0])
            secondaryPortIndex = self.__secondaryPorts.index(self.__portsIntersection[0])

            output = (self.__portsIntersection[0].deviceId, self.__portsIntersection[0].vlanId)
                        
            self.__primaryPorts.pop(primaryPortIndex)
            self.__secondaryPorts.pop(secondaryPortIndex)
            self.__portsIntersection.pop(0)
        else:
            primaryPort = self.__primaryPorts.pop(0)   
            
            if primaryPort in self.__portsIntersection:
                self.__portsIntersection.pop(0)
          
            output = (primaryPort.deviceId, primaryPort.vlanId)
        
        return output
