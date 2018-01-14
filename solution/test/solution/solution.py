#!/usr/bin/env python3
import csv
import sys
sys.path.insert(0, "../../src/")
from solution.solution import Solution
import unittest

class SolutionTest(unittest.TestCase):
    VLANS = "../resources/test_vlans.csv"
    REQUESTS = "../resources/test_requests.csv"
    OUTPUT = "../resources/test_output.csv"
    
    def setUp(self):
        self.solution = Solution(self.VLANS)
        
    def testProcessRequest(self):
        with open(self.REQUESTS) as requests:
            requestReader = csv.reader(requests)
            requestHeaders = next(requestReader)
            
            with open(self.OUTPUT) as testOutput:
                outputReader = csv.reader(testOutput)
                outputHeaders = next(outputReader)

                for requestLine in requestReader:
                    try:
                        request = {key: int(value) for key, value in zip(requestHeaders, requestLine)}
                        
                        outputRecord = self.solution.processRequest(request["request_id"], request["redundant"])
                        test = {key: int(value) for key, value in zip(outputHeaders, next(outputReader))}
                        
                        if request["redundant"]:
                            record = {key: int(value) for key, value in zip(["request_id", "device_id", "primary_port", "vlan_id"], [request["request_id"], outputRecord[0], 0, outputRecord[1]])}
                            self.assertEqual(test, record)
                            
                            record = {key: int(value) for key, value in zip(["request_id", "device_id", "primary_port", "vlan_id"], [request["request_id"], outputRecord[0], 1, outputRecord[1]])}
                            test = {key: int(value) for key, value in zip(outputHeaders, next(outputReader))}
                            self.assertEqual(test, record)
                        else:
                            record = {key: int(value) for key, value in zip(["request_id", "device_id", "primary_port", "vlan_id"], [request["request_id"], outputRecord[0], 1, outputRecord[1]])}
                            self.assertEqual(test, record)
                    except ValueError as e:
                        e.args = ("Invalid VLAN record:", line)
                        raise

def main():
    unittest.main()

if __name__ == "__main__":
    main()
