import argparse
# other imports go here
import urllib3
import csv

def main(url):
    print(f"Running main with URL = {url}...")
    csv_file = 'weblogs.csv'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    with open(csv_file, 'wb')as file:
        file.write(r.data)
    
    with open(csv_file, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            print("Some user requested the file {} on {} using a {}. The status of the request was {}, and the file was {} bytes.\n".format(row[0], row[1], row[2], row[3], row[4]))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
