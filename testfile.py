import putiopy
from ring_doorbell import Ring
import config

def main():
    downloasdurl = []

    eventidlist = []
    myring = Ring(config.username, config.password)
    doorbell = myring.doorbells[0]
    for doorbell in myring.doorbells:

        # listing the last 15 events of any kind
        for event in doorbell.history(limit=100):
            print('ID:       %s' % event['id'])
            eventidlist.append(event['id']) # appens the eventids to the eventidlist.
            print('--' * 50)
        print("the length of eventid list is " + str(len(eventidlist)))
        print("eventidlist is " + str(eventidlist))
        histroy = doorbell.history(limit=100, older_than=eventidlist[-1])

        while(len(eventidlist) < 1000):
            for event in histroy:
                # print('ID:       %s' % event['id'])
                eventidlist.append(event['id'])
            print("the length of eventid list is " + str(len(eventidlist)))
            print("event id list is " + str(eventidlist))




if __name__ == '__main__':
  main()
