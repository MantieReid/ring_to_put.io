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

#print(List_files_on_putio[2:5])
mylist = List_files_on_putio.copy()


testlist = ["6741861927501764421", "6741861927501764421", "6741844996740683589"]


#TODO: get rid of the char del, its no longer needed since getting mylist[x].id no longer cuts off part of the id.
#remove the last two characters in the string for each.
newtestlist = [x[:-2] for x in testlist]
#print("New test list is now " + str(newtestlist))

#for x in mylist:
  #if newtestlist[x] in mylist[x].name:
   # print("I have found the ring video on put.io")
  #  print(mylist[x].name)


#x = 0
#while x < 2:
  #if newtestlist[x] in mylist:
   ##x+=1

testlistfiles = []
testlistfiles.append(List_files_on_putio)

print(mylist)
print("Time to priint this from the list " )
print(List_files_on_putio)


ringdict = {
    "ID" : "",
    "Date" : ""

}



for x in range(0, int(len(newtestlist))):
  if newtestlist[x] in str(mylist[x].name):
   print("video " + str(newtestlist[x]) +  " has been found in " + str(mylist[x].name))
   print("its Id is " + str(mylist[x].id))


#TODO: need to make a code that will change the name of the file to the date of when the video was taken.
#This can be done by stroring the dates in a dictionary list along with the IDS.
#Afterwards, we can then serach and select the date based on the ID we get.





# note, PutIo only shows up to 17 chars for the name.
#print("mylist is now " + str(mylist))
# if "67392322092207368" in str(mylist):
#print("yes 67392322092207368 is in the list")

f = client.File.get(662650943)
f.rename("new name23")


test = "678"
