import argparse
import requests

def DownloadFile(url,local_filename):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 

parser=argparse.ArgumentParser()
parser.add_argument("url",help="url of the file downlod")
parser.add_argument("output",help="by ehich name u want to save your file ")
args=parser.parse_args()
print(args.url)
print(args.output)
DownloadFile(args.url,args.output)      