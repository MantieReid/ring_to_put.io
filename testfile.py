import putiopy
from ring_doorbell import Ring
import config
from collections import Counter


def total_vide_count():
  print("getting the total number of videos in the ring account")

  user_total_videos = 0
  # gets the total amount of videos in the ring account.
  myring = Ring(config.username, config.password)
  doorbell = myring.doorbells[0]

  events = []
  counter = 0
  history = doorbell.history(limit=100)
  while (len(history) > 0):
    events += history
    counter += len(history) # tells us the total amount of videos in the account.
    history = doorbell.history(older_than=history[-1]['id'])
  print("total amount of videos is " + str(counter))
  return counter



def main():
    total_vide_count()
    a = total_vide_count()
    downloasdurl = []

    eventidlist = []
    myring = Ring(config.username, config.password)
    doorbell = myring.doorbells[0]
    counter1 = 0
    for doorbell in myring.doorbells:

        # listing the last 15 events of any kind
        for event in doorbell.history(limit=100):
            print('ID:       %s' % event['id'])
            eventidlist.append(event['id']) # appens the eventids to the eventidlist.
            print('--' * 50)
        print("the length of eventid list is " + str(len(eventidlist)))
        print("eventidlist is " + str(eventidlist))
        histroy = doorbell.history(limit=100, older_than=eventidlist[-1])

        while(len(eventidlist) < a):
            for event in histroy:
                # print('ID:       %s' % event['id'])
                eventidlist.append(event['id'])
            print("the length of eventid list is " + str(len(eventidlist)))
            print("event id list is " + str(eventidlist))




if __name__ == '__main__':
  main()
