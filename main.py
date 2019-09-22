import putiopy
from ring_doorbell import Ring
import config


def total_vide_count():
  print("getting the total number of videos in the ring account")
  myring = Ring(config.username, config.password)  # enters the username and the password from the config file
  doorbell = myring.doorbells[0]  # selects the first doorbell from the doorbell query lists.

  events = []  # events is a list that will store  info from the histroy.
  counter = 0  # a counter that will be used to count the number of videos
  history = doorbell.history(limit=100)  # get the information about the last 100 videos taken. Histroy is set to thiss.
  while (len(history) > 0):  # keeps doing it until it gets all of the videos info from the ring account.
    events += history  # info from histroy is added to events.
    counter += len(history)  # tells us the total amount of videos in the account.
    history = doorbell.history(
      older_than=history[-1]['id'])  # gets 100 videos that are older than  the last video listed in the list.
  print("total amount of videos is " + str(counter))  # prints out the total amount of videos
  return counter  # returns the counter so it can be used later on.

def ringtoputio():

    videocount = total_vide_count()  # video count holds the total amount of videos
    downloasdurl = []  # this will hold all of the download urls.

    eventidlist = []  # the list that will hold the video ID's
    myring = Ring(config.username, config.password)  # enters the password and username for ring.
    doorbell = myring.doorbells[0]  # gets the first doorbell found in the ring list.
    for doorbell in myring.doorbells:

      # listing the last 100 events of any kind
      for event in doorbell.history(limit=100):
        # print('ID:       %s' % event['id'])  prints every single ID in the histroy list.
        eventidlist.append(event['id'])  # appends the eventids to the eventidlist.
        # print('--' * 50)
      print("the length of eventid list is " + str(len(eventidlist)))  # prints the length of list id eventidlist
      print("eventidlist is " + str(eventidlist))  # prints out all of the items in the eventID list.
      histroy = doorbell.history(limit=100, older_than=eventidlist[
        -1])  # defines histroy to get all of the videos older than the last video listed in the list.

      while (len(eventidlist) < videocount):
        histroy = doorbell.history(limit=100, older_than=eventidlist[
          -1])  # defines histroy to get all of the videos older than the last video listed in the list.

        for event in histroy:
          # print('ID:       %s' % event['id'])
          eventidlist.append(event['id'])  # adds the IDs to the list.
          eventidlist = list(dict.fromkeys(eventidlist))  # removes any duplicates in the list.
        print("the length of eventid list is " + str(len(eventidlist)))  # prints the length of the list
        print("event id list is " + str(eventidlist))  # prints what is in the list.


    for x in eventidlist:
      adddownloadurl = doorbell.recording_url(x)
      downloasdurl.append(adddownloadurl)
      print(downloasdurl)
      print("Progress on getting the links" + str(len(downloasdurl)) + "/" + str(videocount))








    #Have the ring videos downloaded to put.io

    helper = putiopy.AuthHelper(config.client, config.application_secret,
                                "https://webhook.site/6e8bc62f-477b-44e6-a67f-9c39795eefb9", type='token')

    client = putiopy.Client(config.token)
    helper.open_authentication_url()


    for x in downloasdurl:


      transfer = client.Transfer.add_url(str(downloasdurl[x]))
      print(str(eventidlist))



def main():
  ringtoputio()




if __name__ == '__main__':
  main()
