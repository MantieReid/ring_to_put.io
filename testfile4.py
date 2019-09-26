import putiopy
from ring_doorbell import Ring
import config
#Have the ring videos downloaded to put.io


helper = putiopy.AuthHelper(config.client, config.application_secret,
                            "https://webhook.site/6e8bc62f-477b-44e6-a67f-9c39795eefb9", type='token')

client = putiopy.Client(config.token)
helper.open_authentication_url()






apples = client.File.search("6740617731310688069", 1)
print(apples)
test = "678"
