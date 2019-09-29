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


testlist = ['6741862210969605957', '6741861927501764421', '6741844996740683589']

#remove the last two characters in the string for each.
newtestlist = [x[:-1] for x in testlist]
print("New test list is now " + str(newtestlist))


#x = 0
#while x < 2:
  #if newtestlist[x] in mylist:
   ##x+=1



for i in range(0, len(mylist)):
  if newtestlist[i] in mylist:
   print("video " + str(newtestlist))



# note, PutIo only shows up to 17 chars for the name.
#print("mylist is now " + str(mylist))
# if "67392322092207368" in str(mylist):
#print("yes 67392322092207368 is in the list")

f = client.File.get(662650943)
f.rename("new name23")


test = "678"
