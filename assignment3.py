import argparse
# other imports go here
import urllib3
import csv
import re

def main(url):
    print(f"Running main with URL = {url}...")
    csv_file = 'weblogs.csv'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    with open(csv_file, 'wb')as file:
        file.write(r.data)
    
    # image hits
    img_list = ['jpg', 'png', 'gif']
    no_of_images = 0
    with open(csv_file, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if any(re.findall('|'.join(img_list), row[0], re.IGNORECASE)):
                no_of_images += 1
            
    
    # popular browsers
    ie = 0
    firefox = 0
    chrome = 0
    safari = 0
    with open(csv_file, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if re.search('MSIE', row[2]):
                ie += 1
            elif re.search('Firefox', row[2]):
                firefox += 1
            elif re.search('Chrome', row[2]):
                chrome += 1
            elif re.search('Safari', row[2]):
                safari += 1



    fileObject = csv.reader(open('weblogs.csv'))
    row_count = sum(1 for row in fileObject)
    percentage = 100 * float(no_of_images)/float(row_count)
    print("Image requests account for {}% of all requests".format(percentage))


    browsers = {
        'Safari': safari,
        'Firefox': firefox,
        'Chrome': chrome,
        'IE': ie
    }
    popular = max(browsers, key=browsers.get)
    print("The most popular browser was {}".format(popular))

    


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
