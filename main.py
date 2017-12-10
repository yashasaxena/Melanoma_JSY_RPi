import requests
import base64
import glob
import os
#import watchdog


#file = filepath of image on pi
#image = open(file, 'rb')
#image_read = image.read()
#image_64_encode = base64.encodestring(image_read)
#assumes 1 image is sent at a time

# encoded an image file to base64
with open('melanoma_test2.jpg', 'rb') as image_file:
    image_64_encode = base64.b64encode(image_file.read())

# storing image data into a dictionary
image_data = {}

image_data["test_image"] = image_64_encode

#end point URL
url = 'http://vcm-1856.vm.duke.edu:5900/jawad'

r = requests.post(url, json=image_data)





# r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }