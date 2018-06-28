"""
Import users for similar product engine
"""

import predictionio
import argparse


def import_events(client):
  count = 0
  print(client.get_status())
  print("Importing data...")

  # generate 1006778 users, with user ids 1,2,....,1000000
  user_ids = [i for i in range(1, 1000001)]
  for user_id in user_ids:
    print("Set user", user_id)
    client.create_event(
      event="$set",
      entity_type="user",
      entity_id=user_id
    )
    count += 1

print("events are imported.")

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
  description="Import sample data for similar product engine")
  parser.add_argument('--access_key', default='')
  parser.add_argument('--url', default="http://localhost:7070")

  args = parser.parse_args()
  print(args)

  client = predictionio.EventClient(
  access_key=args.access_key,
  url=args.url,
  threads=5,
  qsize=500)
  import_events(client)