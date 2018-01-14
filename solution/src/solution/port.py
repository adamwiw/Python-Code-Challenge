class Port:
    "Port represents a VLAN"
    def __init__(self, deviceId, vlanId):
        self.__deviceId = deviceId
        self.__vlanId = vlanId
    
    def __eq__(self, other):
        return self.__deviceId == other.deviceId and self.__vlanId == other.vlanId
    
    def __hash__(self):
        return hash((self.__deviceId, self.__vlanId))
    
    def __repr__(self):
        return "device id: " + str(self.__deviceId) + " vlan id: " + str(self.__vlanId)
    
    @property
    def deviceId(self):
        return self.__deviceId
    
    @property
    def vlanId(self):
        return self.__vlanId
    
