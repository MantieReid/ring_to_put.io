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
    for doorbell in myring.doorbells:

          # listing the last 20 events of any kind
          for event in doorbell.history(limit=5):
            print('ID:       %s' % event['id'])


            print('Kind:     %s' % event['kind'])
            print('Answered: %s' % event['answered'])
            print('When:     %s' % event['created_at'])
            print('--' * 50)

            #adds the event IDs to the list.
            eventidlist.append(event['id'])
            # print(eventidlist)

    print(eventidlist)
    ringdownloadlist = [] # list that will hold the urls of all the download links it

    # need to make a counter. That counts the number of items that has been added to the list compared with the eventid list.
    # example 3/5 links added.
    #get the total of the eventid list.  make that the number after the slash.  then make the number in fro

    doorbell = myring.doorbells[0]
    print("time to run for loop")
    for x in eventidlist:
        ringdownloadlist.append(doorbell.recording_url(x))
        print("list is now" + str(ringdownloadlist))

    print(ringdownloadlist)


    helper = putiopy.AuthHelper(config.client, config.application_secret,
                                "https://webhook.site/6e8bc62f-477b-44e6-a67f-9c39795eefb9", type='token')

    client = putiopy.Client(config.token)
    helper.open_authentication_url()

    for x in eventidlist:
        transfer = client.Transfer.add_url(str(ringdownloadlist[x]))



if __name__ == '__main__':
  main()