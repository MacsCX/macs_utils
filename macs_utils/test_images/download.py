import requests
import random
base_url = 'https://api.adorable.io/avatars/{0}/{1}.jpg'

for x in range(100):
    size = random.randint(150, 300)
    file_name = '{}_{}.jpg'.format(x, size)
    url = base_url.format(size, x)

    with open(file_name, 'wb') as file:
        req = requests.get(url)
        file.write(req.content)

