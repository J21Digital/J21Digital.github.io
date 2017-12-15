#J2Encrypt - J21 Data encryption - Python3
import base64
import hashlib

def j2encrypt(mergeValues):
    hashData = bytes('', 'utf-8')

    if(len(mergeValues) >= 2):
        for i in mergeValues:
            if(i != None):
                hashData += base64.b64encode(bytes(i, 'utf-8'))
        storedHash = hashlib.md5(hashData)
        storedHash = storedHash.hexdigest()
        return storedHash
        
    else:
        raise ValueError("Input requires at least 2 entries for secure encryption.")

#Sample usage.
#inputData = {'value4', 'value5'}
#print(j2encrypt(inputData))
