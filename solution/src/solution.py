#!/usr/bin/env python3
import csv
import sys
import time
from solution.solution import Solution

if __name__ == "__main__":
    start_time = time.time()
    if(len(sys.argv)==3):
        solution = Solution(sys.argv[1])
        
        with open(sys.argv[2]) as requests:
            reader = csv.reader(requests)
            headers = next(reader)
            
            with open('output.csv', 'w') as output:
                outputWriter = csv.writer(output)
                outputWriter.writerow(["request_id", "device_id", "primary_port", "vlan_id"])
                
                for line in reader:
                    try:
                        request = {key: int(value) for key, value in zip(headers, line)}
                        outputRecord = solution.processRequest(request["request_id"], request["redundant"])
                        if request["redundant"]:
                            outputWriter.writerow([request["request_id"], outputRecord[0], 0, outputRecord[1]])
                        outputWriter.writerow([request["request_id"], outputRecord[0], 1, outputRecord[1]])
                    except ValueError as e:
                        e.args = ("Invalid request record:", line)
                        raise
    
    print("--- %s seconds ---" % (time.time() - start_time))
