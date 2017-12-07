import requests
import base64
import watchdog


#file = filepath of image on pi
#image = open(file, 'rb')
#image_read = image.read()
#image_64_encode = base64.encodestring(image_read)
#assumes 1 image is sent at a time

image_data = {'image_b64': image_64_encode}

url = 'http://vcm-1856.vm.duke.edu:5900/ClientMelanomaData'

r = requests.post(url, data=image_data)





# r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }