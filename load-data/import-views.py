import csv
import predictionio
import argparse

def import_events(client):
    print(client.get_status())
    print("Importing data...")

    with open('/Users/jimhahn/Desktop/spotify/spotify-corpus-50.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_parsed_csv = (row['spotify_user'])
            track_parsed_csv = (row['track_uri'])
            # push the items into the database
            user_ids = [user_parsed_csv]
            item_ids = track_parsed_csv
            for user_id in user_ids:
                    print("User", user_ids, "views item", item_ids)
                    client.create_event(
                    event="view",
                    entity_type="user",
                    entity_id=user_id,
                    target_entity_type="item",
                    target_entity_id=item_ids
                                    )

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