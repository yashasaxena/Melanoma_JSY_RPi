import requests
import json
import base64
import glob
import os
import csv
#import watchdog


#file = filepath of image on pi
#image = open(file, 'rb')
#image_read = image.read()
#image_64_encode = base64.encodestring(image_read)
#assumes 1 image is sent at a time

# initializing dictionary for image data
image_data = {}

#end point URL
url = 'http://vcm-1856.vm.duke.edu:5900/CloudMelanomaData'

# encoded an image file to base64
image_directory = '/media/usbstick/Melanoma Images/'
files = glob.glob('/media/usbstick/Melanoma Images/'+'*.jpg')

#glob to extract all image files

c = 0

for img in files:
    with open(img, 'r') as image_read:
        image_64_encode = base64.b64encode(image_read.read())
    #image_64_encode_bytes = image_64_encode.decode('utf-8')
    image_key = "image" + str(c)
    image_data[image_key] = [image_64_encode_bytes]
    c = c + 1

# store post request data in variable r
r = requests.post(url, json=image_data)

result_data = r.json()

# writing results from json results to a csv file

headers = "% Malignant, % Benign/n"
results = result_data[1]['prediction']
c = 0

results_file = open('/media/usbstick/diagnosis.csv', 'w')
results_file.write(headers)

for x in range(0, len(results_data)-1):
    key = 'prediction' + str(c)
    row = results_data[x+1][key][0] + ',' + results_data[x+1][key][1]
    csv.write(row)
    c = c+1

# r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }