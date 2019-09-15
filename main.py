import putiopy
from ring_doorbell import Ring
import config

def main():

    eventidlist = []
    myring = Ring(config.username,config.password)
    doorbell = myring.doorbells[0]

    events = []
    counter = 0
    history = doorbell.history(limit=100)
    while (len(history) > 0):
      events += history
      counter += len(history)
      history = doorbell.history(older_than=history[-1]['id'])
      print(history)
      # adds the event IDs to the list.
      #eventidlist.append(event['id'])
      #print(eventidlist)

    print("total number of videos is {}".format(counter))

    for event in events:
      eventidlist.append(event['id']) # add all of the ids to the event list



    print(eventidlist)
    print("items in list is " + str(len(eventidlist)))

    ringdownloadlist =[] # will be used to store all of the download links for the video

    counternumber = 0 # will be used as a counter to show the progress of the urls being added to the list.
    for x in eventidlist:
      ringdownloadlist.append(doorbell.recording_url(x))
      counternumber +=1
      print("the number of items in the list is now " + str(counternumber) + " " + "/" + str(len(eventidlist)))
      print(eventidlist)




    #Have the ring videos downloaded to put.io

    helper = putiopy.AuthHelper(config.client, config.application_secret,
                                "https://webhook.site/6e8bc62f-477b-44e6-a67f-9c39795eefb9", type='token')

    client = putiopy.Client(config.token)
    helper.open_authentication_url()

    for x in eventidlist:
      transfer = client.Transfer.add_url(str(ringdownloadlist[x])) +  print(ringdownloadlist)
      print(str(ringdownloadlist))

    #get a list of all devices.

    print("list all devices", myring.devices)
    print("list all stickup cams",myring.stickup_cams)
    print("list all chimes", myring.chimes)
    print("list all doorbells", myring.doorbells)

    """
    def eventidtolist():

      for doorbell in myring.doorbells:
        # listing the last 20 events of any kind
        for event in doorbell.history(limit=100):


          print('ID:       %s' % event['id'])
          #print('Kind:     %s' % event['kind'])
          #print('Answered: %s' % event['answered'])
          #print('When:     %s' % event['created_at'])
          #print('--' * 50)
          #adds the event IDs to the list.
          eventidlist.append(event['id'])
          print(eventidlist)

    #need to get all of the event ids for ring. All of them.

    eventidtolist()
    print(eventidlist)
    lasteventid = 0
    lasteventid = eventidlist[-1]

    def eventidtolistolderthan():

      for doorbell in myring.doorbells:
        # listing the last 20 events of any kind
        for event in doorbell.history(limit=100,older_than=lasteventid):
          print('ID:       %s' % event['id'])
          eventidlist.append(event['id'])
          print(eventidlist)
          print("length of the list is "  + str(len(eventidlist)))

    # ringdownloadlist = [] # list that will hold the urls of all the download links it

    eventidtolistolderthan()

"""
if __name__ == '__main__':
  main()
