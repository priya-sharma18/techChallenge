import requests
import sys

dataKey = sys.argv[1]
METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/instance/'+ dataKey + '/?recursive=true'
METADATA_HEADERS = {'Metadata-Flavor': 'Google'}

if dataKey == 'disks' or dataKey == 'licenses':
    try:
        response = requests.get(url=METADATA_URL, headers=METADATA_HEADERS)
    except:
        print("System/network error")

    #Convert response into json format
    data=response.json()
    print("Below is the metadata information of this VM - ")
    print("-----------------------------------------------")
    print(data)

else:
    print(METADATA_URL)
    try:
        response = requests.get(url=METADATA_URL, headers=METADATA_HEADERS)
    except:
        print("System/network error")
    print(response)

