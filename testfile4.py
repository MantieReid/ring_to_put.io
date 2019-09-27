import putiopy
from ring_doorbell import Ring
import config
#Have the ring videos downloaded to put.io


helper = putiopy.AuthHelper(config.client, config.application_secret,
                            "https://webhook.site/6e8bc62f-477b-44e6-a67f-9c39795eefb9", type='token')

client = putiopy.Client(config.token)
helper.open_authentication_url()




#apples = client.File.search("6740617731310688069", 1)
#print(apples)
List_files_on_putio = client.File.list()
print(List_files_on_putio)

print(List_files_on_putio[2:5])
mylist = List_files_on_putio.copy()


# note, PutIo only shows up to 17 chars for the name.
print("mylist is now " + str(mylist))
if "67392322092207368" in str(mylist):
  print("yes 67392322092207368 is in the list")

changename = client.File.rename('62650943', "testfile")

print(changename)


test = "678"
