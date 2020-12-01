import json
import requests
import shutil

from array import array
with open('xray.json') as json_file:
    data = json.load(json_file)
    counted = 0
    image_url = []
    for p in data:
        image_url.insert(counted,p['link'])
        counted += 1 
with open('ct_scan.json') as json_file:
    data = json.load(json_file)
    for p in data:
        image_url.insert(counted,p['link'])
        counted += 1 

## Set up the image URL and filename
counted = 0
for i in image_url:
    filename = "image/image_" + str(counted)
    counted += 1
    r = requests.get(i, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
       
