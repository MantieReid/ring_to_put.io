import putiopy
from ring_doorbell import Ring
import config

def main():

    eventidlist = []
    myring = Ring(config.username,config.password)

    #get a list of all devices.

    print("list all devices", myring.devices)
    print("list all stickup cams",myring.stickup_cams)
    print("list all chimes", myring.chimes)
    print("list all doorbells", myring.doorbells)




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


if __name__ == '__main__':
  main()
