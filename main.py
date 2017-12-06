import requests
import base64


#file = filepath of image on pi
#image = open(file, 'rb')
#image_read = image.read()
#image_64_encode = base64.encodestring(image_read)

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