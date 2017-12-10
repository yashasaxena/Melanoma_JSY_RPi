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

# initializing dictionary for image data
image_data = {}

#end point URL
url = 'http://vcm-1856.vm.duke.edu:5900/jawad'

# encoded an image file to base64
image_directory = '/media/usbstick/Melanoma Images/'
files = glob.glob('/media/usbstick/Melanoma Images/'+'*.jpg')

#glob to extract all image files

for img in files:
    with open(img, 'rb') as image_read:
        image_64_encode = base64.b64encode(image_read.read())
        image_data["test_image"].append(image_64_encode)



r = requests.post(url, json=image_data)





# r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }